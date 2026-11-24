#!/usr/bin/env python3
# Vibecoded background remover script, using original files as input.

from pathlib import Path
import math
import re
import sys
import xml.etree.ElementTree as ET

ICON_DIR = Path.home() / ".local/share/icons/hicolor/scalable/apps"

SVG_NS = "http://www.w3.org/2000/svg"

ET.register_namespace("", SVG_NS)


def local_name(element):
    return element.tag.split("}")[-1]


def is_background_path(element):
    """Recognise the full-icon rounded-square background path."""

    d = re.sub(r"\s+", " ", element.get("d", "").replace(",", " ")).strip()

    # Background paths start near the left edge, 10 units below
    # the top, and close at the same vertical position.
    start = re.match(
        r"M\s*([-+\d.eE]+)\s+([-+\d.eE]+)",
        d,
    )

    end = re.search(
        r"V\s*([-+\d.eE]+)\s*Z$",
        d,
        re.IGNORECASE,
    )

    if not start or not end:
        return False

    x, y = map(float, start.groups())
    end_y = float(end.group(1))

    # Allow small coordinate differences, e.g. proton-b2b.
    return (
        abs(x) <= 0.2
        and abs(y - 10) <= 0.2
        and abs(end_y - y) <= 0.2
        and "36" in d
        and "26" in d
    )


def find_background(root):
    """Find the first visible full-icon background."""

    def search(parent):
        for child in parent:
            tag = local_name(child)

            # Never modify definitions or clipping/masking geometry.
            if tag in ("defs", "clipPath", "mask", "metadata"):
                continue

            if tag == "path" and is_background_path(child):
                return parent, child

            if tag == "rect":
                try:
                    x = float(child.get("x", "0"))
                    y = float(child.get("y", "0"))
                    width = float(child.get("width", "0"))
                    height = float(child.get("height", "0"))

                    viewbox = root.get("viewBox", "0 0 36 36")
                    _, _, vb_width, vb_height = map(float, viewbox.split())

                    if (
                        math.isclose(x, 0)
                        and math.isclose(y, 0)
                        and math.isclose(width, vb_width)
                        and math.isclose(height, vb_height)
                    ):
                        return parent, child
                except (ValueError, TypeError):
                    pass

            result = search(child)
            if result:
                return result

        return None

    return search(root)


def main():
    if not ICON_DIR.is_dir():
        sys.exit(f"Directory not found: {ICON_DIR}")

    files = sorted(ICON_DIR.glob("proton-*.svg"))

    files = [file for file in files if not file.stem.endswith("-nobg")]

    if not files:
        print("No matching SVG files found.")
        return

    processed = 0
    skipped = 0

    for file in files:
        output = file.with_name(f"{file.stem}-nobg.svg")

        try:
            tree = ET.parse(file)
            root = tree.getroot()

            result = find_background(root)

            if result is None:
                print(f"SKIPPED: {file.name} (background not recognised)")
                skipped += 1
                continue

            parent, background = result
            parent.remove(background)

            tree.write(
                output,
                encoding="utf-8",
                xml_declaration=True,
            )

            print(f"CREATED: {output.name}")
            processed += 1

        except (ET.ParseError, OSError) as error:
            print(f"ERROR: {file.name}: {error}", file=sys.stderr)
            skipped += 1

    print(f"\nFinished: {processed} processed, {skipped} skipped.")


if __name__ == "__main__":
    main()
