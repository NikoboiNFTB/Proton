# Proton

Proton AG related stuff.

## Update Script

Automatically updates Proton Authenticator, Proton Mail and Proton Pass on Linux (Debian->), only if needed. Can be run locally ([download](/update/script)) or remotely:

```sh
bash <(wget -qO- https://proton.nikoboi.dev/update/script)
```

As per usual with my stuff you can just install it:

```sh
bash <(wget -qO- https://proton.nikoboi.dev/update/install)
```

Then run it using:

```sh
proton-update
```

---

Example result of an update:

```sh
user@pc:~/GitHub/NikoboiNFTB/Proton$ bash update
==> Pass
    Installed: 1.40.2
    Latest:    1.40.2
    Up to date.

==> Authenticator
    Installed: 1.1.6
    Latest:    1.1.6
    Up to date.

==> Mail
    Installed: 1.13.4
    Latest:    1.14.0
    Update available.
    Downloading...
######################################################################### 100.0%
    Verifying checksum...
    Checksum OK.
    Installing...
[sudo] password for user:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Note, selecting 'proton-mail' instead of '/tmp/tmp.sELdI4CDYd/proton-mail.deb'
Suggested packages:
  gir1.2-gnomekeyring-1.0 libgnome-keyring0
The following packages will be upgraded:
  proton-mail
1 upgraded, 0 newly installed, 0 to remove and 33 not upgraded.
Need to get 0 B/89,2 MB of archives.
After this operation, 21,2 MB of additional disk space will be used.
Get:1 /tmp/tmp.sELdI4CDYd/proton-mail.deb proton-mail amd64 1.14.0 [89,2 MB]
(Reading database… 691816 files and directories currently installed.)
Preparing to unpack …/tmp.sELdI4CDYd/proton-mail.deb…
Unpacking proton-mail (1.14.0) over (1.13.4)…
Setting up proton-mail (1.14.0)…
Processing triggers for desktop-file-utils (0.27-2build1)…
Processing triggers for gnome-menus (3.36.0-1.1ubuntu3)…
Processing triggers for mate-menus (1.26.1+mint1)…
Processing triggers for mailcap (3.70+nmu1ubuntu1.24.04.1)…
N: Download is performed unsandboxed as root as file '/tmp/tmp.sELdI4CDYd/proton-mail.deb' couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)
    Successfully updated to 1.14.0.

All Proton apps are up to date.
user@pc:~/GitHub/NikoboiNFTB/Proton$
```

Yeah pretty cool ig idk. Don't have to manually download from Proton every update anymore.

Example result of no updates available:

```sh
user@pc:~$ bash <(wget -qO- https://proton.nikoboi.dev/update/script)
==> Pass
    Installed: 1.40.2
    Latest:    1.40.2
    Up to date.

==> Authenticator
    Installed: 1.1.6
    Latest:    1.1.6
    Up to date.

==> Mail
    Installed: 1.14.0
    Latest:    1.14.0
    Up to date.

All Proton apps are up to date.
user@pc:~$
```

## VPN

Proton VPN related stuff.

> [!WARNING]
> Currently completely broken. Changed repo name and structure and I don't feel like fixing it now.

If you need to use anything VPN related from this repo, clone this repo at commit **4c288ac**.

```sh
git clone https://github.com/NikoboiNFTB/Proton ~/GitHub/NikoboiNFTB/Proton-VPN
cd ~/GitHub/NikoboiNFTB/Proton-VPN
git checkout 4c288ac
```

### [`install-icons`](/install-icons)

Install Proton SVG files as user or root, i.e. in `~/.local/share/icons/` or `/usr/share/icons/`. The folder name `ProtonAG` is used for the icons.

Proton's SVG files are visually superior to their app icons.

Run the script either from this repo or remotely;

```sh
bash <(wget -qO- https://proton.nikoboi.dev/install-icons)
```

> [!WARNING]
> Not working.

> [proton.nikoboi.dev](https://proton.nikoboi.dev/) resolves to this repository.

## [`setup`](/setup)

Does something idek anymore. Just ignore this one.

## Contributing

Feel free to fork this repository and submit issues or pull requests if you have any suggestions or improvements. If you encounter any bugs or have feature requests, please open an issue.

## Credits

Created by [**Nikoboi**](https://github.com/NikoboiNFTB/)

## License

This project is licensed under the GNU General Public License V3. See [LICENSE](/LICENSE) for details.
