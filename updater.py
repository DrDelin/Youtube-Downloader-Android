import os
import sys
import json
import linecache
import requests
import re
from termcolor import colored , cprint
from bs4 import BeautifulSoup
from datetime import date , datetime
import time
start = time.time()

cprint("WELCOME TO TERMUX DOWNLOADER","cyan","on_red",attrs=["bold"])

#Update Server URL:
url = "https://raw.githubusercontent.com/DrDelin/Youtube-Downloader-Android/refs/heads/beta/YTD_Android.py"

#Local Version No:
l_version = linecache.getline(r"/data/data/com.termux/files/home/main.py", 1)
#Local Engine No:
l_engine = linecache.getline(r"/data/data/com.termux/files/home/main.py", 2)

#Update Failsafe Bypasser
try:
    response = requests.get(url, timeout=10)  # timeout in seconds
    # Split into lines
    lines = response.text.splitlines()
    c_version = (lines[0] if len(lines) > 0 else "")+"\n"
    c_engine = (lines[1] if len(lines) > 1 else "")+"\n" 
    print("\nUpdate Server: "+colored('ACTIVE','green')+"\nFailsafe Update Verification System By-Passer: "+colored('DEACTIVATED','green')+"\nAuto Upgrade System: "+colored('ACTIVE','green')+"\nDownloader: "+colored('ACTIVE & RUNNING','green')+"\n")

except:
    print("\nFailsafe Update Verification System By-Passer: "+colored('ACTIVATED','red')+"\nUpdate Server: "+colored('BROKEN OR DOWN','red')+"\nAuto Upgrade System: "+colored('ACTIVE','green')+" \nServer repair: "+colored('ONGOING','red')+"\nDownloader: "+colored('ACTIVE & RUNNING','green')+"\n")
    c_version = l_version
    c_engine = l_engine 

#Ping:
end = time.time()
print(f"\n[Ping: {(end-start)*10**3:.02f}mS]\n")

#Code to pass link to the downloader / Manual upgrader
if not sys.argv[1] == "forced":
    code = "python '/data/data/com.termux/files/home/main.py' '" +sys.argv[1] +"'"
    
    if c_engine == l_engine:
        print("\n"+colored("No Engine upgrade available from developer...","yellow")+"\n")

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
                    print("Script previously upgraded on: "+colored(date2,'blue'))
                    defaultFile.close
            dates = datetime.strptime(date1, "%d/%m/%Y")  - datetime.strptime(date2, "%d/%m/%Y")
            if int(dates.days) > int("28"):
                print("\nOutdated Binaries, auto upgrading...\n")
                with open(path, "r") as defaultFile:
                    data = json.load(defaultFile)
                    data["default"][0]["last_upgrade"] = date1
                    with open(path, "w") as defaultFile:
                        json.dump(data, defaultFile, indent=4)
                        defaultFile.close
                    os.system("sh refresh.sh auto")
            else:
                print("\nBinaries seems to be new. Auto upgrade skipped...\n\nChecking version update...\n")
        else:
            print("\nChecking version update...\n")

        if c_version == l_version:
            print("\n"+colored('No new update...','yellow')+"\n")
            os.system(code)
        else:
            print("\nNew version available...\n\nUpdating...\n\n")
            open('/data/data/com.termux/files/home/noobjection.temp', 'a').close()
            os.system("sh refresh.sh auto")
            print("\nUpdated...!\n")
            os.system(code)
    else:
        print("\nNew Engine Upgrade available...\n\nUpgrading...\n")

        #Upgrade date recording:
        path = "/data/data/com.termux/files/home/default.json"
        date1 = date.today().strftime("%d/%m/%Y")
        with open(path, "r") as defaultFile:
                    data = json.load(defaultFile)
                    data["default"][0]["last_upgrade"] = date1
                    with open(path, "w") as defaultFile:
                        json.dump(data, defaultFile, indent=4)
                        defaultFile.close

        #Upgrade                
        os.system("sh refresh.sh auto")
        print("Upgraded...!\n")
        os.system(code)

#Forced Manual upgrade / Troubleshoot date recorder
else:
    path = "/data/data/com.termux/files/home/default.json"
    if os.path.isfile(path):
        date1 = date.today().strftime("%d/%m/%Y")
        with open(path, "r") as defaultFile:
                    data = json.load(defaultFile)
                    data["default"][0]["last_upgrade"] = date1
                    with open(path, "w") as defaultFile:
                        json.dump(data, defaultFile, indent=4)
                        defaultFile.close
    else:
        pass
