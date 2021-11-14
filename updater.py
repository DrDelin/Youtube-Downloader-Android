#imports
import os
import sys

#temp Download
os.system(wget -P '/data/data/com.termux/files/home/' -q 'https://raw.githubusercontent.com/DrDelin/Youtube-Downloader-Android/master/YTD_Android.py')
   
#updator
with open("/data/data/com.termux/files/home/YTD_Android.py") as u:
    update = u.readline().rstrip()

with open("/data/data/com.termux/files/home/main.py") as m:
    main = m.readline().rstrip()

if update==main:
    os.remove("/data/data/com.termux/files/home/YTD_Android.py")
    print("No New Update...")
    code = "python '/data/data/com.termux/files/home/main.py' '" +sys.argv[1] +"'"
    os.system(code)
else:
    print("Updating......")
    os.remove("/data/data/com.termux/files/home/main.py")
    os.system("mv YTD_Android.py main.py")
    print("Updated..!")
    code = "main.py '" +sys.argv[1] +"'"
    os.system(code)

m.close()
u.close()

quit()
