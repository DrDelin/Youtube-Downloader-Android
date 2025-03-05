import os , json , sys
path = "/data/data/com.termux/files/home/default.json"
if os.path.isfile(path):
    with open(path, 'r') as js:
        jfile = json.load(js)
    if not "incognito" in str(jfile):
        with open(path,'r') as f:
            content = f.read()
        content = content.replace('"history_backup": ""','"incognito": "off"')
        with open(path,'w') as f:
            f.write(content)
            f.close()
        os.remove(sys.argv[0])
    else:
        os.remove(sys.argv[0])
else:
    os.remove(sys.argv[0])