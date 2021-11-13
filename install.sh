#!/bin/bash

termux-setup-storage
pkg up -y

pkg install python -y
pkg install ffmpeg -y
pip install mutagen
pip install --no-deps -U yt-dlp
pip3 install termux-apt-repo
pkg install x11-repo
apt install transmission-gtk

mv "YTD_Android.py" "/data/data/com.termux/files/home/main.py"
mv "termux-url-opener" "/data/data/com.termux/files/home/termux-url-opener"

cd "/data/data/com.termux/files/home/"

mkdir bin
mv "termux-url-opener" "/data/data/com.termux/files/home/bin/termux-url-opener"

cd bin
chmod +x termux-url-opener

echo ###Installation Done Successfully...Select Termux in share option of youtube app..."###