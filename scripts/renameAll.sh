#!/usr/bin/env sh

echo $"$(du -a .| cut -d$'\t' -f2- )"




	#| cut -d$'\t' -f2- | fzf | xargs -d '\n' -r rifle;}
