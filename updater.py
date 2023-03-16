import os
import sys
import json
import linecache
import requests
from bs4 import BeautifulSoup
from datetime import date , datetime

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
    print("\nNo Engine upgrade available from developer...\n")

    #Auto Upgrade segment
    path = "/data/data/com.termux/files/home/default.json"
    if os.path.isfile(path):
        date1 = date.today().strftime("%d/%m/%Y")
        with open(path, "r") as defaultFile:
            data = json.load(defaultFile)
            if data["default"][0]["last_upgrade"] == "":
                print("Script upgrading on: " + date1)
                data["default"][0]["last_upgrade"] = date1
                date2 = date1
                with open(path, "w") as defaultFile:
                        json.dump(data, defaultFile, indent=4)
                defaultFile.close
            else:
                date2 = data["default"][0]["last_upgrade"]
                print("Script previously upgraded on: "+date2)
                defaultFile.close
        dates = datetime.strptime(date1, "%d/%m/%Y")  - datetime.strptime(date2, "%d/%m/%Y")
        print(dates.days)
        if int(dates.days) > int("28"):
            print("Outdated Binaries, auto upgrading...")
            with open(path, "r") as defaultFile:
                data = json.load(defaultFile)
                data["default"][0]["last_upgrade"] = date1
                with open(path, "w") as defaultFile:
                    json.dump(data, defaultFile, indent=4)
                    defaultFile.close
                os.system("sh refresh.sh")
        else:
            print("\nBinaries seems to be new. Auto upgrade skipped...\n\nChecking version update...\n")
    else:
        print("\nChecking version update...\n")

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
    print("\nNew Engine Upgrade available...\n\nUpgrading...\n")
    os.system("sh refresh.sh")
    print("Upgraded...!\n")
    os.system(code)
