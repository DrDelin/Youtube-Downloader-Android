#!/bin/bash

termux-setup-storage -y
pkg up -y

pkg install python -y
pkg install ffmpeg -y
pip install mutagen
pip install --no-deps -U yt-dlp
pip3 install termux-apt-repo
pkg install x11-repo
pkg install wget -y
apt install transmission-gtk -y

mv "YTD_Android.py" "/data/data/com.termux/files/home/main.py"
mv "termux-url-opener" "/data/data/com.termux/files/home/termux-url-opener"
mv "updater.py" "/data/data/com.termux/files/home/updater.py"
mv "refresh.sh" "/data/data/com.termux/files/home/refresh.sh"
cd "/data/data/com.termux/files/home/"

mkdir bin
mv "termux-url-opener" "/data/data/com.termux/files/home/bin/termux-url-opener"

cd bin
chmod +x termux-url-opener

echo ###Installation Done Successfully...Select Termux in share option of youtube app..."###

rm "/data/data/com.termux/files/home/Youtube-Downloader-Android/install.sh"
rm "/data/data/com.termux/files/home/Youtube-Downloader-Android/README.md"
cd "/data/data/com.termux/files/home/"
rm -rf "/data/data/com.termux/files/home/Youtube-Downloader-Android"
