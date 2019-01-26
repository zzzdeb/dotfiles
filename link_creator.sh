#!/bin/sh

# for var in "$@"
# do
  # ln -s /mnt/all/home/zzz/$var ~/$var
# done

DOTPATH="/home/zzz/.dotfiles"

ln -s $DOTPATH/polybar/config $HOME/.config/polybar/config
ln -s $DOTPATH/polybar/launch.sh $HOME/.config/polybar/launch.sh

