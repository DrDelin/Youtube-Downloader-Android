#!/bin/bash

#Installing scripts:
mv "refresh.sh" "/data/data/com.termux/files/home/refresh.sh"
mv "YTD_Android.py" "/data/data/com.termux/files/home/main.py"
mv "termux-url-opener" "/data/data/com.termux/files/home/termux-url-opener"
mv "updater.py" "/data/data/com.termux/files/home/updater.py"
mv "history.py" "/data/data/com.termux/files/home/history.py"
mv "patch0.1.py" "/data/data/com.termux/files/home/patch0.1.py"

#Bin file creation and permission elevation:
cd "/data/data/com.termux/files/home/"
mkdir bin
mv "termux-url-opener" "/data/data/com.termux/files/home/bin/termux-url-opener"
cd bin
chmod +x termux-url-opener
cd "/data/data/com.termux/files/home/"

#Storage permission:
if [ -e '/data/data/com.termux/files/home/default.json' ]; then
    termux-setup-storage -y
    python patch0.1.py
else
    termux-setup-storage
    rm -rf patch0.1.py
fi

#Binaries installation:
if [ -e '/data/data/com.termux/files/home/noobjection.temp' ]; then
    rm -rf '/data/data/com.termux/files/home/noobjection.temp'
    #Completion msg:
    echo ###Installation Done Successfully...Select Termux in share option of youtube app..."###
    #Setup package purging:
    rm -rf "/data/data/com.termux/files/home/Youtube-Downloader-Android"
    sleep 5
    exit
else
    pkg up -y -y -y -y
    pkg install python -y
    pkg install aria2 -y
    pkg install ffmpeg -y
    pip install beautifulsoup4
    pip install requests
    pip install mutagen
    pip install wheel
    pip install --no-deps -U yt-dlp
    pip install yt-dlp
    pip3 install termux-apt-repo
    pkg install x11-repo
    pkg install wget -y
    apt install transmission-gtk -y
    pip install gdown
    #Updates and upgrades:
    apt update -y -y -y
    apt upgrade -y -y -y
    apt update -y -y -y
    cat /data/data/com.termux/files/home/Youtube-Downloader-Android/README.md
    #Completion msg:
    echo ###Installation Done Successfully...Select Termux in share option of youtube app..."###
    #Setup package purging:
    rm -rf "/data/data/com.termux/files/home/Youtube-Downloader-Android"
    sleep 5
    exit
fi

exit
