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

#Local Version No:
l_version = linecache.getline(r"/data/data/com.termux/files/home/main.py", 1)
#Local Engine No:
l_engine = linecache.getline(r"/data/data/com.termux/files/home/main.py", 2)

#Update Failsafe Bypasser
try:
    #Cloud Version No:
    def cv(soup):
        vindex = soup.find("#Version")
        ver = soup[vindex + len("#Version"):vindex + len("#Version") + 9]
        c_version = "#Version" +ver+"\n"

        #Version number pattern verification:
        v = ver.replace(" ","")
        v_pattern = r"^\d+.\d+.\d+.\d+$"
        if re.match(v_pattern, v):
            return c_version
        else:
            print(colored('\n__Update_server_timeout__','red'))
            return l_version
    
    #Cloud Engine No:
    def ce(soup):
        eindex = soup.find("#Engine")
        eng = soup[eindex + len("#Engine"):eindex + len("#Engine") + 5]
        c_engine = "#Engine"+eng+"\n"

        #Engine number pattern verification:
        e = eng.replace(" ","")
        e_pattern = r"^\d+.\d+$"
        if re.match(e_pattern, e):
            return c_engine
        else:
            print(colored('\n__Update_server_timeout__','red'))   
            return l_engine

    #Getting cloud edition's version and engine number
    url = "https://github.com/DrDelin/Youtube-Downloader-Android/blob/master/YTD_Android.py"
    request  = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser').text
    
    c_version = cv(soup)
    c_engine = ce(soup)
    
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
            print("\nNo new update...\n")
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