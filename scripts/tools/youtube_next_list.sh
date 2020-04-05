#!/usr/bin/env bash

URL_PLAYED=()
URL_CURRENT="$(youtube-dl --get-id --no-playlist "$1")"

[[ "$1" =~ "list=" ]] && LIST="$(echo "$1" | awk -v FS="(list=|&index)" '{print $2}')"

[[ -z "$LIST" ]] && URL_LIST=()
#  grep -m1 -oP 'href="\/watch\?v=\K.{11}'
TMP="$(wget -q -O- "https://www.youtube.com/watch?v=$URL_CURRENT&list=$LIST" | grep -o -P '.watch\?v=.{0,11}' | cut -d '=' -f2)"

# echo "TMP" = "${TMP[*]}"

for i in $TMP; do
  if [[ ! "${URL_LIST[@]}" =~ "https://www.youtube.com/watch?v=$i" ]]; then
    URL_LIST+=( "https://www.youtube.com/watch?v=$i" )
  fi
done

echo "${URL_LIST[@]:1}" | tr " " "\n"
