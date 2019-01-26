#!/bin/sh

sudo apt-get install curl network-manager-openvpn-gnome
cd /tmp
wget https://www.privateinternetaccess.com/installer/pia-nm.sh
sudo bash ./pia-nm.sh
