#!/bin/bash
#
#git submodule init
#git submoudle update --recursuve
#

set -e
set -o

cd meta
sudo bash ./larbs.sh -p progs.csv
chsh -s /bin/zsh
./install-profile all
cd ../submodules/fzf
./install --xdg --all
pip install pyyaml virtualenvwrapper ranger-fm pyperclip
sudo pip install i3ipc
