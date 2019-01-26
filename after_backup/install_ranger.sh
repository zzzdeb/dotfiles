#!/bin/sh


sudo apt install ranger

cd ~/.local/share/fonts && curl -fLo "Droid Sans Mono for Powerline Nerd Font Complete.otf"
https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/DroidSansMono/complete/Droid%20S
ans%20Mono%20Nerd%20Font%20Complete.otf

cd /tmp
git clone https://github.com/alexanderjeurissen/ranger_devicons
cd ./ranger_devicons
make install
