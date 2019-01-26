#!/bin/sh

BUILDDIR="$HOME/softwares"

cd "$BUILDDIR"

git clone https://github.com/FedeDP/libmodule.git
cd libmodule
mkdir build
cd build
cmake ..
sudo checkinstall

sudo apt install libpolkit-gobject-1-dev libudev-dev libxrandr-dev libxss-dev libx11-dev

cd "$BUILDDIR"
git clone https://github.com/FedeDP/Clightd
cd Clightd
mkdir build
cd build
cmake -DENABLE_DDC=1 -DENABLE_GAMMA=1 -DENABLE_IDLE=1 -DENABLE_DPMS=1 ../
sudo checkinstall


sudo apt install ddcutil 
