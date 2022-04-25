#!/bin/bash
#Engine 2.1
rm main.py
rm updater.py
rm -rf Youtube-Downloader-Android
rm -rf bin
git clone https://github.com/DrDelin/Youtube-Downloader-Android
cd Youtube-Downloader-Android
sh install.sh
