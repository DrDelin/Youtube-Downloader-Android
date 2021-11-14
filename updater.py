#imports
import os
import sys

#Update
os.remove("main.py")
os.rename('YTD_Android.py' 'main.py')

#Back to process
code = "main.py" +sys.argv[1]
os.system(code)
quit()