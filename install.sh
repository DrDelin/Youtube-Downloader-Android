#!/bin/bash
termux-setup-storage
pkg up -y
pkg install python -y
pkg install ffmpeg -y
pip install mutagen
pip install --no-deps -U yt-dlp
mv "YTD_Android.py" "/data/data/com.termux/files/home/ytdlp.py"
cd "/data/data/com.termux/files/home/"
echo ###Installation Done Successfully... Run the program with command "python ytdlp.py"###