#!/bin/sh

echo -e 'hdmi\nanalog\nh2\nsink' | rofi -dmenu -p ALSA| { read tmp;  
case $tmp in
    analog|hdmi) pacmd set-card-profile alsa_card.pci-0000_00_1f.3 output:$tmp-stereo+input:analog-stereo;;
    h2) pacmd set-card-profile alsa_card.pci-0000_00_1f.3 output:hdmi-stereo-extra1+input:analog-stereo;;
    sink) switch-audio-sink
esac
}
# while read LINE; do
     # $SCREENHOME/$LINE
# done < /dev/stdin
