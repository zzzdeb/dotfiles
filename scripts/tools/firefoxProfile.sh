#!/usr/bin/env bash

dmenu_command="dmenu -l 20 -i"

if [ "$#" -gt 2 ]; then
  echo "usage: firefoxProfile.sh create $profilename \
               firefoxProfile.sh open"
  exit 1
fi

case $1 in
  create )
    dirname=$(/usr/bin/find $HOME/.mozilla/firefox -name "*\.$2")
    [ -z "$dirname" ] || { echo "$dirname found"; exit 1; }

    firefox -P "$2" || return
    dirname=$(/usr/bin/find $HOME/.mozilla/firefox -name "*\.$2")
    [ -z "$dirname" ] && { echo "$2 not found in ~/.mozilla/firefox"; exit 1; }
    filename="$dirname/prefs.js"

    while IFS= read -r line
    do
       ## take some action on $line
       regline=$(echo "$line" | sed "s/\s/\\\ /g")
       grep -q "$regline" "$filename" || echo "$line" >> "$filename"
    done < ~/.mozilla/firefox/prefs.js

    cat ~/.mozilla/extensions/firstlinks.txt | xargs firefox -P "$2"
    ;;
  open )
    var="$(capture.zsh "firefox -P " | $dmenu_command | tr -cd '[:print:]')"
    echo $var
    firefox -P "$var"
    ;;
esac
