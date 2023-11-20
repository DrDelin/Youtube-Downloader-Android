import os , json , sys

path = "/data/data/com.termux/files/home/default.json"

if os.path.isfile(path):
    with open(path, 'r') as js:
        jfile = json.load(js)

    if not "history_backup" in str(jfile):
        update = {"history_backup" : ""}
        for i in jfile['default']:
            i.update(update)
        with open(path, 'w') as js2:
            json.dump(jfile, js2, indent= 4)
        os.remove(sys.argv[0])
    else:
        os.remove(sys.argv[0])

else:
    os.remove(sys.argv[0])