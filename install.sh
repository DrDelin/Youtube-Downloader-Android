#!/bin/bash
termux-setup-storage
pkg up -y
pkg install python -y
pkg install ffmpeg -y
pip install yt-dlp
mv "YTD_Android.py" "/data/data/com.termux/files/home/ytdlp.py"
echo ###Installation Done Successfully... Run the program with command "python ytdlp.py"###