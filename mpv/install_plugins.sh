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

# find sub
pluginName="find_subtitles"
if [ -d $pluginDirs/$pluginName ]; then
    echo "pulling"
    cd $pluginDirs/$pluginName git pull; cd ../..
else
    echo "cloning"
    git clone https://github.com/directorscut82/$pluginName $pluginDirs/$pluginName
fi

cp ./$pluginDirs/$pluginName/*.lua ./$scriptsDir
cp ./$pluginDirs/$pluginName/*.conf ./$scriptsOptsDir

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

# sub translation
gitName="Eisa01/mpv-scripts"
pluginName="mpv-scripts"
if [ -d $pluginDirs/$pluginName ]; then
    echo "pulling"
    cd $pluginDirs/$pluginName git pull; cd ../..
else
    echo "cloning"
    git clone https://github.com/$gitName $pluginDirs/$pluginName
fi

cp ./$pluginDirs/$pluginName/scripts/*.lua ./$scriptsDir
cp ./$pluginDirs/$pluginName/scripts/*.py ./$scriptsDir
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


# sub menu
gitName="nezumisama/mpvmenu"
pluginName="mpvmenu"
if [ -d $pluginDirs/$pluginName ]; then
    echo "pulling"
    cd $pluginDirs/$pluginName git pull; cd ../..
else
    echo "cloning"
    git clone https://github.com/$gitName $pluginDirs/$pluginName
fi

sudo apt install python-gobject
pip3 install --user subdownloader
