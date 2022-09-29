import os
import json

history = "history.txt"

histlist = []
with open(history, 'r+') as f:
    for jsonObj in f:
        Dict = json.loads(jsonObj)
        histlist.append(Dict)
histlist2 = str(histlist).replace("'",'"')
input_dict = json.loads(histlist2)

for i in input_dict:
    print(i["SNo"]+")", i["Name"]+"||", i["Site"])

print("What to do!? \n")
print("Select 1 to redownload from history: \nSelect 2 to clear history: \nSkip to close this script:\n")
choice = input("Your Choice:")
if choice=="1":
    ask = input("Enter the SNo:")
    output_dict = [a for a in input_dict if a["SNo"] == ask]
    for j in output_dict:
        print(j["SNo"]+")", j["Name"]+"||", j["Site"])
        url = j["URL"]
        os.system('python main.py "'+url+'"')
        exit()
elif choice=="2":
    os.remove(history)
else:
    exit()
