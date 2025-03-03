#!/data/data/com.termux/files/usr/bin/env python3
import os
from termcolor import colored
print("\n")
print(colored("TERMUX DOWNLOADER UTILITIES",'red')+"\n")

#History Import
def his_imp():
    des_path = '/data/data/com.termux/files/home/history.txt'
    imp_path = '/storage/emulated/0/Termux_Downloader/'
    def x(imp_path):
        for file in os.listdir(imp_path):
            if file.lower().endswith('.txt'):
                return True
        return False
    if not x(imp_path):
         print("No History File to import available in Termux Downloader folder!!")
         exit()
    
    print("\nKeep only one history Text file in Termux Downloader folder and click enter !!\n")
    if input("") == "":
        count = [f for f in os.listdir(imp_path) if f.endswith('.txt')]
        if len(count) > 1:
            exit()
    
    from pathlib import Path
    imp_his_file = (list(Path(imp_path).glob("*.txt")))[0]
    if not os.path.isfile(des_path):
        import shutil
        shutil.move(imp_his_file,des_path)
        exit()
        
    import json
    with open(des_path, 'r') as fp:
        lines = len(fp.readlines())
        fp.close()
    num = str(int(lines)+ int("1"))
    
    def appender(no,title,url,site):
        with open(des_path,'a+') as fp:
            st = {"SNo": no , "Name": title, "URL": url, "Site":site}
            fp.write(json.dumps(st)+str("\n"))
            fp.close()
            
    with open(imp_his_file, 'r+') as f:
         for jsonObj in f:
             histlist = []
             Dict = json.loads(jsonObj)
             histlist.append(Dict)
             histlist1 = str(histlist).replace("'",'"').replace("\\","/")
             input_dict = json.loads(histlist1)
             for x in input_dict:
                 appender(no=num,title=x["Name"],url=x["URL"],site=x["Site"])
                 num = str(int(num)+ int("1"))
    f.close()
    os.remove(imp_his_file)
        
def down():
    link = input("Enter the Link: \n")
    print("\n")
    os.system("python '/data/data/com.termux/files/home/main.py' '" +link +"'")
    
print("Tools:\n1. Manual Link download\n\nHistory:\n2. View Download History\n3. Backup History\n4. Import History\n5. Delete History\n\nTroubleshooting:\n6. Manual Upgrade\n7. Factory Reset\n\nInfo:\n8. Script Build Info\n9. Developers info\n")
choice = input("Choice:")
print("\n")

#Manual Downloader  
if choice == "1":
    down()

# View History
elif choice == "2":
    os.system("python '/data/data/com.termux/files/home/history.py'")

# Backup History
elif choice == "3":
    from datetime import datetime
    dest = '/storage/emulated/0/Termux_Downloader/history_backup_'+datetime.now().strftime("%d%m%y_%H%M%S")+".txt'"
    os.system("cp '/data/data/com.termux/files/home/history.txt' '"+dest)
    print("History Backup Done !!\nLocation: "+dest.replace("/storage/emulated/0/","Internal Storage > /")+"\n")

# Import History
elif choice == "4":
    his_imp()
    
#Delete History
elif choice == "5":
    os.remove('/data/data/com.termux/files/home/history.txt')
    
#Factory Default Reset            
elif choice == "6" or choice == "7":
    os.system("sh refresh.sh")
    
#Script Info
elif choice == "8":
    import json
    from datetime import date , datetime
    sc_path = '/data/data/com.termux/files/home/main.py'
    j_path = '/data/data/com.termux/files/home/default.json'
    linex = []
    with open(sc_path,"r") as fy:
        for _ in range(3):
            line = fy.readline().strip()
            linex.append(line)
        fy.close()
    with open(j_path,"r") as j:
        data = json.load(j)
        date_old = data["default"][0]["last_upgrade"]
        j.close()
    
    date_new = date.today().strftime("%d/%m/%Y")
    days = str(int("28") - int((datetime.strptime(date_new,"%d/%m/%Y") - datetime.strptime(date_old,"%d/%m/%Y")).days))
    
    print("Version: "+ linex[0].replace("#Version ","") )
    print("Engine: "+ linex[1].replace("#Engine ",""))
    print("Build: " +linex[2].replace("#",""))
    print("Script previously upgraded on: "+ date_old)
    print(f'Script auto-upgrades in {days} days')
    print("\n")
    
#Developer info
elif choice == "9":
    print("Choose to go to the page:\n1. Official Termux App GitHub page\n2. Official Terumux app download page\n3. Script Developer's GitHub page\n4. Script bugs/errors/feedback reporting page\n")
    i = input("Choice: ")
    if i == "1":
        os.system("termux-open-url https://github.com/termux/termux-app")
    elif i == "2":
        os.system("termux-open-url https://github.com/termux/termux-app/releases")
    elif i == "3":
        os.system("termux-open-url https://github.com/DrDelin/Youtube-Downloader-Android")
    elif i == "4":
        os.system("termux-open-url https://github.com/DrDelin/Youtube-Downloader-Android/issues")
    else:
         exit()

else:
    exit()