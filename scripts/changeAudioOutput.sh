#!/bin/sh

echo 'hdmi\nanalog' | rofi -dmenu -p ALSA| { read tmp;  pacmd set-card-profile alsa_card.pci-0000_00_1f.3 output:$tmp-stereo;}
# while read LINE; do
     # $SCREENHOME/$LINE
# done < /dev/stdin
