#!/usr/bin/env bash
xrandr-invert-colors

xrdb ~/.Xdefaults

# xrdb ~/.Xdefaults_dark

i3-msg 'reload'
