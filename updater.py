import os
import sys
import linecache
import requests
from bs4 import BeautifulSoup

print("WELCOME TO TERMUX DOWNLOADER")

#Getting cloud edition's version and engine number
url = "https://github.com/DrDelin/Youtube-Downloader-Android/blob/master/YTD_Android.py"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

#Cloud Version No:
ver = soup.find(id="LC1")
c_version = ver.text.strip() + "\n"
#Cloud Engine No:
eng = soup.find(id="LC2")
c_engine = eng.text.strip() + "\n"

#Local Version No:
l_version = linecache.getline(r"/data/data/com.termux/files/home/main.py", 1)
#Local Engine No:
l_engine = linecache.getline(r"/data/data/com.termux/files/home/main.py", 2)

#Code to pass link to the downloader
code = "python '/data/data/com.termux/files/home/main.py' '" +sys.argv[1] +"'"

if c_engine == l_engine:
    print("\nNo Engine upgrade available...\nChecking Version Update...\n")
    if c_version == l_version:
        print("\nNo new update...\n")
        os.system(code)
    else:
        print("\nNew version available...\n\nUpdating...\n\n")
        open('/data/data/com.termux/files/home/noobjection.temp', 'a').close()
        os.system("sh refresh.sh")
        print("\nUpdated...!\n")
        os.system(code)
else:
    print("/nNew Engine Upgrade available.../n/nUpgrading.../n")
    os.system("sh refresh.sh")
    print("Upgraded...!")
    os.system(code)
