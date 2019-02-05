#!/bin/sh

SCREENHOME=~/.screenlayout
ls $SCREENHOME | rofi -dmenu -p ARANDR -l 10 | { read tmp; $SCREENHOME/$tmp; }
# while read LINE; do
     # $SCREENHOME/$LINE
# done < /dev/stdin
