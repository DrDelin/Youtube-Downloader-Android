#!/bin/bash
#Engine 5.0
rm main.py
rm updater.py
rm history.py
rm -rf Youtube-Downloader-Android
rm -rf bin
git clone https://github.com/DrDelin/Youtube-Downloader-Android
cd Youtube-Downloader-Android
sh install.sh
