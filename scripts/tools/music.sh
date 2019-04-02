#!/bin/bash

browser=${BROWSER:-firefox}

if [ !-v $DMENU ]
then
  DMENU='dmenu -i -l 20'
fi
choice=$(echo "🦆" | $DMENU -i -p "Youtube:") || exit 1
output=$(ddgr -w youtube.com --json "$choice")
selectionTitle=$(echo $output | jq '.[].title' | $DMENU)
# selectionUrl=$(echo '[{"title": "a", "url":"b"}]' | jq '.[] | select(.title == "a").url')
# echo $output
eval "selectionUrl=\$(echo \$output | jq '.[] | select(.title ==
"$selectionTitle").url')"
echo $selectionUrl
eval $browser $selectionUrl

# choice=$(echo "🦆" | $DMENU -i -p "Search DuckDuckGo:") || exit 1

# if [ "$choice" = "🦆"  ]; then
    # $browser "https://duckduckgo.com"
# else
    # Detect if url
    # if [[ "$choice" =~ ^(http:\/\/|https:\/\/)?[a-zA-Z0-9]+\.[a-zA-Z]+(/)?.*$ ]]; then
        # $browser "$choice"
    # else
        # $browser "https://duckduckgo.com/?q=$choice&t=ffab&atb=v1-1"
    # fi
# fi
