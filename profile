# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
[ -n "$BASH_VERSION" ] && [ -f "$HOME/.bashrc" ] && . "$HOME/.bashrc"
[ -n "$ZSH_VERSION" ] && [ -f "$HOME/.zshrc" ] && . "$HOME/.zshrc"

[ -d "$HOME/.Xdefaults" ] && xrdb $HOME/.Xdefaults

# set PATH so it includes user's private bin if it exists
[ -d "$HOME/.local/bin" ] && PATH="$HOME/.local/bin:$PATH"
export PATH="$PATH:$(du "$HOME/.scripts/" | cut -f2 | tr '\n' ':' | sed 's/:*$//')"

export EDITOR="nvim"
export TERMINAL="st"
export BROWSER="qutebrowser"
export READER="zathura"
export FILE="ranger"
export SUDO_ASKPASS="$HOME/.scripts/tools/dmenupass"
export NOTMUCH_CONFIG="$HOME/.config/notmuch-config"
export GTK2_RC_FILES="$HOME/.config/gtk-2.0/gtkrc-2.0"
export DMENU="rofi -dmenu -i"
export MANPAGER="sh -c 'col -bx | bat -l man -p'"

# less/man colors
export LESS=-R
export LESS_TERMCAP_mb="$(printf '%b' '[1;31m')"; a="${a%_}"
export LESS_TERMCAP_md="$(printf '%b' '[1;36m')"; a="${a%_}"
export LESS_TERMCAP_me="$(printf '%b' '[0m')"; a="${a%_}"
export LESS_TERMCAP_so="$(printf '%b' '[01;44;33m')"; a="${a%_}"
export LESS_TERMCAP_se="$(printf '%b' '[0m')"; a="${a%_}"
export LESS_TERMCAP_us="$(printf '%b' '[1;32m')"; a="${a%_}"
export LESS_TERMCAP_ue="$(printf '%b' '[0m')"; a="${a%_}"

[ ! -f ~/.shortcuts ] && shortcuts >/dev/null 2>&1

# Start graphical server if i3 not already running. && Change Keyboard Layout
[ "$(tty)" = "/dev/tty1" ] && ! pgrep -x i3 >/dev/null && exec startx && remaps

# Switch escape and caps if tty:
sudo -n loadkeys ~/.scripts/ttymaps.kmap 2>/dev/null
