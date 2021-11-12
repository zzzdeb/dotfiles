#!/bin/sh

# xinitrc runs automatically when you run startx.

# There are some small but important commands that need to be run when we
# start
# the graphical environment. I keep those commands in ~/.xprofile because that
# file is run automatically if someone uses a display manager (login screen)
# and so they are needed there. To prevent doubling up commands, I source them
# here with the line below.
[ -f ~/.zshenv ] && . ~/.zshenv
export $(dbus-launch)
export XDG_CURRENT_DESKTOP=i3
export WORKSPACE2="2: "
export WORKSPACE3="3: 日本"
export WORKSPACE4="4: "
export WORKSPACE6="6: "
export WORKSPACE7="7: "
export WORKSPACE8="8: "
export WORKSPACE0="10: "
[ -f ~/.xprofile ] && . ~/.xprofile
exec i3
