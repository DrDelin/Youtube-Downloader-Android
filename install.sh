#!/bin/bash

#Installing scripts:
mv "refresh.sh" "/data/data/com.termux/files/home/refresh.sh"
mv "YTD_Android.py" "/data/data/com.termux/files/home/main.py"
mv "termux-url-opener" "/data/data/com.termux/files/home/termux-url-opener"
mv "updater.py" "/data/data/com.termux/files/home/updater.py"
mv "history.py" "/data/data/com.termux/files/home/history.py"
mv "patch-0.2.py" "/data/data/com.termux/files/home/patch-0.2.py"

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
    python patch-0.2.py
else
    termux-setup-storage
    rm -rf patch-0.2.py
fi

#Binaries installation:
if [ -e '/data/data/com.termux/files/home/noobjection.temp' ]; then
    rm -rf '/data/data/com.termux/files/home/noobjection.temp'
    #Completion msg:
    echo
    echo UPDATE / UPGRADE SUCCESSFUL!
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
    pip install termcolor
    pip install requests
    pip install wheel
    pip install yt-dlp -U
    pip install ffmpeg
    pip install gdown
    apt install rclone -y
    
    #Removed Features
    pip3 uninstall termux-apt-repo -y
    pkg remove x11-repo -y
    pkg remove wget -y
    apt remove transmission-gtk -y

    #Updates and upgrades:
    apt update -y -y -y
    apt upgrade -y -y -y
    apt update -y -y -y
    apt autoremove -y -y -y
    cat /data/data/com.termux/files/home/Youtube-Downloader-Android/README.md
    
        
    #Setup package purging:
    rm -rf "/data/data/com.termux/files/home/Youtube-Downloader-Android"
    
    #Installation completion message
    echo
    echo INSTALLTION SUCCESSFUL!
    sleep 5
    exit
fi

exit
