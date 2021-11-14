#imports
import os
import sys

#Update
os.remove("/data/data/com.termux/files/home/main.py")
os.rename('/data/data/com.termux/files/home/YTD_Android.py' '/data/data/com.termux/files/home/main.py')

#Back to process
code = "main.py " +sys.argv[1]
os.system(code)
quit()