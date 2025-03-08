import os
import json
import time

history = "history.txt"
temp = 'temp.txt'

def history_mod():
    if not os.path.isfile(history):
        print("History is Not Yet Created! or History got deleted!!\nDownload atleast once to create history and make sure Incognito Mode turned off!!\n")
        exit()
    start = time.time()
    histlist = []
    with open(history, 'r+') as f:
        for jsonObj in f:
            Dict = json.loads(jsonObj)
            histlist.append(Dict)
    histlist2 = str(histlist).replace("'",'"')
    histlist3 = histlist2.replace("\\","/")
    input_dict = json.loads(histlist3)
    print("\nHistory: \n")
    for i in input_dict:
        print(i["SNo"]+")", i["Name"]+"||", i["Site"])
    end = time.time()
    end = time.time()
    print(f"\nListing time: {(end-start)*10**3:.02f}mS\n")
    print("\nWhat to do!? \n")
    print("Select 1 to redownload from history: \nSelect 2 to revisit the site of download: \nSelect 3 to clear history: \nSkip to close this script:\n")
    choice = input("Your Choice:")
    if choice=="1":
        ask = input("\nEnter the SNo:")
        output_dict = [a for a in input_dict if a["SNo"] == ask]
        for j in output_dict:
            print(j["SNo"]+")", j["Name"]+"||", j["Site"])
            url = j["URL"]
            print("\n")
            os.system('python main.py "'+url+'"')
            exit()
    elif choice=="2":
        ask = input("\nEnter the SNo:")
        output_dict = [a for a in input_dict if a["SNo"] == ask]
        for j in output_dict:
            url = j["URL"]
            os.system('termux-open-url "' + url + '"')
            exit()
    elif choice=="3":
        confirm = input("\nType YES to confirm clear history:\n")
        if confirm=="YES":
            os.remove(history)
            exit()
        else:
            exit()
    else:
        exit()

def temp_mod():
    temp_link = open(temp,'r').readlines()[0]
    print("\nPreviously failed link:")
    print("\n"+temp_link+"\n")
    print("What to do:\n 1.To Resume or attempt redownload\n 2.To open the site with link\n >Skip to exit\n")
    sel = input("Enter: ")
        
    if sel == "1":
        print("Attempting Redownload.....")
        os.system('python main.py "'+temp_link+'"')
    elif sel == "2":
        print("Opening the link in browser or supported app.....")
        os.system('termux-open-url "' +temp_link+ '"')
    else:
        print("Skipping....")
        exit()

if os.path.isfile(temp):
    if input("\n    Previously failed to download exists..Want to resume it(type 'y') or skip to view history: ") == "y":
        temp_mod()
    else:
        history_mod()
else:
    history_mod()