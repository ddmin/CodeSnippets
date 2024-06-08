# Frequently Encountered Problems

## 1. Ranger

### (1.1) Ranger returns an error code

I aliased ranger to 'ranger && wal'. Probably has something to do with wal

### (1.2) Navigate to last directory in Ranger

```console
alias ranger='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'
```

### (1.3) Change wallpaper in XFCE using ranger?

1. Run in Terminal: xfconf-query -c xfce4-desktop -m and change background.
2. `map bg shell wal --vte -q -i %f && xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitoreDP1/workspace0/last-image -s %d/%f`

## 2. Proton VPN

### (2.1) [ProtonVPN killswitch disables internet](https://askubuntu.com/questions/1319033/internet-stops-working-after-installing-protonvpn)
```console
nmcli device
sudo nmcli connection delete pvpn-killswitch
sudo nmcli connection delete pvpn-ipv6leak-protection
```

### (2.2) [Proton VPN asks for password](https://bbs.archlinux.org/viewtopic.php?id=270089)

(this might solve it, idk)
#### Add two lines to /etc/pam.d

```console
auth       optional     pam_gnome_keyring.so
session    optional     pam_gnome_keyring.so auto_start
```

## 3. Firefox

### (3.1) Firefox backspace to go back a page

1. about:config
2. browser.backspace_action = 0

### (3.2) [Firefox Touch Scrolling](https://superuser.com/questions/1151161/enable-touch-scrolling-in-firefox)

/etc/security/pam_env.conf

```console
 MOZ_USE_XINPUT2 DEFAULT=1
```

### (3.3) [Disable alt key to open menu](https://www.reddit.com/r/firefox/comments/129w85w/is_there_a_way_to_disable_firefox_alt_keyboard/)

about:config

```console
ui.key.menuAccessKey            0
ui.key.menuAccessKeyFocuses     false
```

### (3.4) [Disable WebRTC in Firefox](https://support.mozilla.org/en-US/questions/963501)

about:config

```console
media.peerconnection.enabled        false
media.navigator.enabled             false
```

### (3.5) [Firefox Contextual Identities](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities)

about:config
```console
privacy.userContext.enabled                                     true
privacy.userContext.newTabContainerOnLeftClick.enabled          true
privacy.userContext.ui.enabled          true
```

## 4. (Doom) Emacs

### (4.1) Running emacs as a daemon

Start daemon
```console
/usr/bin/emacs --daemon
```

Open emacsclient
```console
emacsclient -c -a 'emacs'
```

### (4.2) [Keyboard mapping doesn't work (Doom)](https://discourse.doomemacs.org/t/how-to-re-bind-keys/56)

#### (4.2.1) Major/Minor Mode overrides keybinding
```lisp
(after! mode
    (keybinding))
```

#### (4.2.2) [Evil Mode overrides keybinding](https://discourse.doomemacs.org/t/how-to-bind-keys-with-higher-precedence-than-evil-keybindings/3743/2)
```lisp
(map! :nvi "<KEY>" #'<KEYBINDING>)
```

```console
    :n  normal
    :v  visual
    :i  insert
    :e  emacs
    :o  operator
    :m  motion
    :r  replace
    :g  global
```

## 4. Virtual Machines

### (4.1) [QEMU Virt-Manager Shared Clipboard](https://unix.stackexchange.com/questions/109117/virt-manager-copy-paste-functionality-to-the-vm/435665#435665)

#### Ubuntu Virtual Machine: in the guest machine install:
```console
sudo apt install spice-vdagent
```

### (4.2) [Shared folders between guest and host](https://www.youtube.com/watch?v=9FBhcOnCxM8)

1. Click `Add Hardware` in virt-manager
2. `Filesystem`
3. Setup filesystem passthrough

```console
Type: mount
Mode: mapped
Source path: <SHARED FOLDER>
Target path: <MOUNT PATH>
```

4. Run command in guest machine

## TODO: Uncategorized

### Can't access Cinnamon settings

You have to downgrade the PIL to 5.4.1

### Weather info not displaying in the homepage

Set mixed content to false in about:config

### What's the command for rofi?

`rofi -show drun`

### Get rid of Gnome-Terminal titlebar?

run `gsettings set org.gnome.Terminal.Legacy.Settings headerbar "@mb false"`

### Gnome-Terminal doesn't recognized installed Nerd Font

Use Gnome-Tweak-Tools and change the monospace font globally

### [Set Google as default search engine in Linux Mint?](https://www.linuxmint.com/searchengines.php)

### Red error indication in powerline every time I open terminal

Probably because I didn't install fzf or node or something else

### Change screenshot to show more options

Set shortcut to `/usr/bin/gnome-screenshot --interactive`

### Go Autocomplete in YouCompleteMe

Run `./.vim/plugged/YouCompleteMe/install.py --go-completer`

### Applications not showing up in rofi

Add .desktop files to ~/.local/share/applications

### Icons for rofi?

`~/.icons`

### Connect to WiFi with redirect page.

[Try 192.168.1.1](https://unix.stackexchange.com/questions/89630/how-to-sign-into-an-open-wireless-network)

### Prettier not working / npm not found

Turn on node, `nvm use node`

### Wifi not detected on fresh install

[Copy b43 onto a flashdrive](https://askubuntu.com/questions/730799/installing-firmware-b43-installer-offline)

### Slow WiFi on iMac

[Install drivers](https://archived.forum.manjaro.org/t/solved-bcm4331-inconsistent-and-slow-wifi-on-mac/95386/2)

### SSH not working in rofi?

[Add ~/.ssh/config file](https://linuxize.com/post/using-the-ssh-config-file/)

### [No sound from iMac headphone jack](https://linux-tips.com/t/how-to-fix-apple-imac-headphone-sound-problem/285)

Add `options snd-hda-intel model=imac27_122` to `/etc/modprobe.d/sound.conf`

### Connect to wifi automatically (wpa_supplicant)

```
https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant
```

### Automatic updates on Ubuntu

```console
1. apt install unattended-upgrades
2. dpkg-reconfigure --priority=low unattended-upgrades
```

### Ctrl-G for fzf?

#### Bash

```bash
bind '"\C-t": transpose-chars'
bind -x '"\C-g": fzf-file-widget'
```

#### ZSH

```zsh
bindkey '^G' fzf-file-widget
bindkey '^T' transpose-chars
```

### No emojis on Arch?

Install `extra/noto-fonts-emoji`

### SSH permission denied?

Probably an issue on my end.
```console
# /etc/ssh/ssh_config
PasswordAuthentication yes
```

### rsync into mobile?

```console
rsync -e 'ssh -p 8022' <FILES> u0_a500@192.168.1.XXX:/data/data/com.termux/files/home/storage/
```

### Set folding in files

Add this to the bottom of the file

```vim
# vim: foldmethod=marker:foldlevel=0
```

### Trouble converting images to PDF with ImageMagick

[Cache exhausted](https://stackoverflow.com/questions/31407010/cache-resources-exhausted-imagemagick)

```console
# /etc/ImageMagick-6/policy.xml
<policy domain="resource" name="disk" value="8GiB"/>
<policy domain="resource" name="area" value="1GiB"/>
```

[PDF blocked security policy](https://stackoverflow.com/questions/52998331/imagemagick-security-policy-pdf-blocking-conversion)

```console
# /etc/ImageMagick-6/policy.xml
...
<policy domain="coder" rights="read | write" pattern="PDF" />
...
</policymap>
```

### Bluetooth `org.bluez.Error.Failed`

[Possibly missing packages](https://unix.stackexchange.com/questions/258074/error-when-trying-to-connect-to-bluetooth-speaker-org-bluez-error-failed)

```console
sudo apt install pulseaudio-module-bluetooth
pulseaudio -k
pulseaudio --start
```

### Bluetooth `Failed to pair: org.bluez.Error.AlreadyExists`

Try restarting bluetooth

```console
sudo service bluetooth restart
```

Or maybe [rfkill is blocking bluetooth](https://stackoverflow.com/questions/54387985/bluetooth-blocked-through-rfkill)

```console
# check status
sudo service bluetooth status
sudo rfkill unblock bluetooth
```

### Bluetooth [a2dp-sink profile connect failed. Protocol not available](https://askubuntu.com/questions/1172000/a2dp-sink-profile-connect-failed)

```console
sudo apt-get install pulseaudio-module-bluetooth
sudo killall pulseaudio
pulseaudio --start
sudo service bluetooth restart
```

### [Multiple Github Accounts Using SSH](https://gist.github.com/oanhnn/80a89405ab9023894df7)

```console
# Account 1
Host github-1
   HostName github.com
   IdentityFile ~/.ssh/key_1
   IdentitiesOnly yes

# Account 2
Host github-2
   HostName github.com
   IdentityFile ~/.ssh/key_2
   IdentitiesOnly yes
```

### [Render Japanese UTF8 in Vim](https://stackoverflow.com/questions/5166652/how-to-view-utf-8-characters-in-vim-or-gvim)

.vimrc
```console
    set encoding=utf-8
    set fileencodings=iso-2022-jp,euc-jp,sjis,utf-8
    set fileformats=unix,dos,mac
```

### [Open CBZ containing WEBP with evince](https://gitlab.gnome.org/GNOME/evince/-/issues/925)
[Install webp-pixbuf-loader](https://github.com/aruiz/webp-pixbuf-loader/)

### [Install Anki on Ubuntu](https://askubuntu.com/questions/1404353/how-to-install-qt6-on-ubuntu-21-10)

```console
sudo apt install qt6-base-dev
sudo apt install libxcb-cursor0
```

### Sound not working on Galaxy Book

[necessary-verbs.sh](https://github.com/joshuagrisham/galaxy-book2-pro-linux)

### Website stuck on debugger while using Inspect Element

[Set ```debugger``` ```Conditional breakpoint``` to ```false```](https://devtoolstips.org/tips/en/disable-abusive-debugger-statement/)

### rofi application not changing after editing .desktop file

For snaps check ```/var/lib/snapd/desktop/applications```

### Don't count underscores (_) as part of a word in Vim

```:set iskeyword-=_```

### Source virtualenv from bash script

[Source from .bashrc instead](https://stackoverflow.com/a/13122219)

```bash
activate () {
  . ../.env/bin/activate
}
```

### [Failed to connect: org.bluez.Error.NotReady br-connection-adapter-not-powered](https://unix.stackexchange.com/a/676973)

```console
/etc/bluetooth/main.conf
```

```console
[Policy]
# ... snip ...
AutoEnable=true
```

### Ctrl + Backspace

[vim](https://www.reddit.com/r/neovim/comments/prp8zw/comment/hdkdd7a/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

```console
imap <C-H> <C-W>
```

[bash](https://unix.stackexchange.com/a/264871)
```console
~/.inputrc
```

```console
"\C-h": backward-kill-word
"\e[3;5~": kill-word
```

### [KeepassXC Unlock on Login](https://github.com/keepassxreboot/keepassxc/issues/1267)

```console
# store a new password:
secret-tool store --label='Keepass' database pass.xdbx

# query and start keepassxc:
secret-tool lookup database pass.xdbx | keepassxc --pw-stdin ~/pass.xdbx
```

### [Remove snap from Ubuntu](https://askubuntu.com/a/1035917)

```console
sudo apt autoremove --purge snapd
sudo apt-mark hold snapd

# or [this answer](https://askubuntu.com/questions/1345385/how-can-i-stop-apt-from-installing-snap-packages/1345401#1345401)

cat <<EOF | sudo tee /etc/apt/preferences.d/nosnap.pref
# To prevent repository packages from triggering the installation of Snap,
# this file forbids snapd from being installed by APT.
# For more information: https://linuxmint-user-guide.readthedocs.io/en/latest/snap.html

Package: snapd
Pin: release a=*
Pin-Priority: -10
EOF
```

### [Remap Alt in Vim](https://vim.fandom.com/wiki/Fix_meta-keys_that_break_out_of_Insert_mode)

```console
:set <M-A>=<press Ctrl-V><press Meta-A>
:imap <press Ctrl-v><press Esc>a <M-A>
```
### [Display title in mpv playing youtube video](https://unix.stackexchange.com/questions/298492/make-mpv-display-name-of-youtube-link-when-playing-just-audio)

```console
mpv --term-playing-msg='${media-title}' <URL>
```

### [xmodmap Key Names](https://wiki.linuxquestions.org/wiki/List_of_Keysyms_Recognised_by_Xmodmap)
