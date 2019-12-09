#!/bin/sh

scriptsOptsDir="script-opts"
if [ ! -d $scriptsOptsDir ]; then
    echo "mkdir $scriptsOptsDir"
    mkdir $scriptsOptsDir
fi

scriptsDir="scripts"
if [ ! -d $scriptsDir ]; then
    echo "mkdir $scriptsDir"
    mkdir $scriptsDir
fi

pluginDirs="plugins"
if [ ! -d $pluginDirs ]; then
    echo "mkdir $pluginDirs"
    mkdir $pluginDirs
fi

# youtube quality
if [ -d $pluginDirs/mpv-youtube-quality ]; then
    echo "pulling"
    cd $pluginDirs/mpv-youtube-quality; git pull; cd ../..
else
    echo "cloning"
    git clone https://github.com/jgreco/mpv-youtube-quality.git $pluginDirs/mpv-youtube-quality
fi

cp ./$pluginDirs/mpv-youtube-quality/*.lua ./$scriptsDir
cp ./$pluginDirs/mpv-youtube-quality/*.conf ./$scriptsOptsDir


# sub translation
gitName="oltodosel/interSubs"
pluginName="interSubs"
if [ -d $pluginDirs/$pluginName ]; then
    echo "pulling"
    cd $pluginDirs/$pluginName git pull; cd ../..
else
    echo "cloning"
    git clone https://github.com/$gitName $pluginDirs/$pluginName
fi

cp ./$pluginDirs/$pluginName/*.lua ./$scriptsDir
cp ./$pluginDirs/$pluginName/*.py ./$scriptsDir
cp ./$pluginDirs/$pluginName/*.conf ./$scriptsOptsDir

# reload if stuck
gitName="4e6/mpv-reload"
pluginName="mpv-reload"
if [ -d $pluginDirs/$pluginName ]; then
    echo "pulling"
    cd $pluginDirs/$pluginName git pull; cd ../..
else
    echo "cloning"
    git clone https://github.com/$gitName $pluginDirs/$pluginName
fi

cp ./$pluginDirs/$pluginName/*.lua ./$scriptsDir

cd ./$scriptsDir
# autosub
wget https://raw.githubusercontent.com/DavidDeprost/mpv-autosub/master/autosub.lua
pip3 install --user subliminal

# nextfile
wget https://raw.githubusercontent.com/jonniek/mpv-nextfile/master/nextfile.lua
