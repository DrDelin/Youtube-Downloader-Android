import os
import sys

print("WELCOME TO TERMUX DOWNLOAD MANAGER")

url = "https://github.com/DrDelin/Youtube-Downloader-Android/blob/master/YTD_Android.py"

import requests
from bs4 import BeautifulSoup

r  = requests.get(url)
data = r.text

soup = BeautifulSoup(data, 'html.parser')
ver = soup.find(id="LC1")
update = ver.text.strip()

with open("/data/data/com.termux/files/home/main.py") as m:
    main = m.readline().rstrip()
if update==main:
    print("\nNo New Update...\n")
    code = "python '/data/data/com.termux/files/home/main.py' '" +sys.argv[1] +"'"
    os.system(code)
else:
    print("\nUpdating......\n")
    open('/data/data/com.termux/files/home/noobjection.temp', 'a').close()
    os.system("sh refresh.sh")
    code = "python '/data/data/com.termux/files/home/main.py' '" +sys.argv[1] +"'"
    os.system(code)
    m.close()
    
quit()
