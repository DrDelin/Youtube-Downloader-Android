#Version 10.2.0.0
#Engine 10.2
#Stable version

#(Master) imports
import os
import sys
import linecache
import json
from termcolor import colored
from datetime import date

#Version Info:
version = (linecache.getline(linecache.sys.argv[0],1))
print(version.replace("#", ""))
linecache.clearcache()

#Engine info:
engine = (linecache.getline(linecache.sys.argv[0],2))
print(engine.replace("#", ""))
linecache.clearcache()

#Build info:
build = (linecache.getline(linecache.sys.argv[0],3))
print("Build: "+ build.replace("#", ""))
linecache.clearcache()

#(Default) JSON file creation or verification:
json_path = "/data/data/com.termux/files/home/default.json"


if os.path.isfile(json_path):
    pass
else:
    t_date = date.today().strftime("%d/%m/%Y")
    jsonnew = {
        "default" : [
            {
                "code" : "",
                "codec" : "",
                "last_upgrade": t_date,
                "incognito": "off" 
            }],
        "1" : [
            {
                "height" : "2160",
                "res" : "4k"
            }],
        "2" : [
            {               
                "height" : "1440",
                "res" : "2k"
            }],
        "3" : [
            {
                "height" : "1080",
                "res" : "1080p"
            }],
        "4" : [
            {
                "height" : "720",
                "res" : "720p"
            }],
        "5" : [
            {
                "height" : "480",
                "res" : "480p"
            }],
        "6" : [
            {
                "height" : "360",
                "res" : "360p"
            }],
        "7" : [
            {
                "height" : "240",
                "res" : "240p"
            }],
        "8" : [
            {
                "height" : "144",
                "res" : "144p"
            }]
    }
    file = json.dumps(jsonnew, indent=4)
    with open(json_path, "w") as out:
        out.write(file)
    out.close

#Incognito status:
with open(json_path, 'r') as file:
        data = json.load(file)
        state = (data["default"][0]["incognito"]).capitalize()
        file.close()
print(f"Incognito Mode: {state}\n") 

#Update news:
print("(Changelog)Whats new...!\n")
print("   >(Main)Fatal Bugs fixed\n   >(Feature)New Utility mode\n   >(Utility)Open Termux app and type 'tools' to open Termux downloader utilities\n   >(Utilities)New Incognito Mode\n   >(Engine)Removed Unwanted Binaries and Maintenance\n")

#(Master) Verification of dependencies
def dependency():
    try:
        import ffmpeg
    except ModuleNotFoundError:
        os.system('pip install ffmpeg')
    try:
        import yt_dlp
    except ModuleNotFoundError():
        os.system('pip install --no-deps -U yt-dlp')

dependency()

#(Master) Automated link grabbing from Termux url Opener
link = sys.argv[1]

#Temp file:
temp_loc = "/data/data/com.termux/files/home/temp.txt"
    #Purging previous temp file:
if os.path.isfile(temp_loc):
    os.remove(temp_loc)
else:
    pass

    #Creating new temp file:
with open(temp_loc,"x") as temp:
    temp.write(link)
    temp.close()

#General Path
genPath = "/storage/emulated/0/"

#(Master) History:
def history(title, site):
    history = "/data/data/com.termux/files/home/history.txt"
    Title0 = title.replace('"',"`")
    Title = Title0.replace("'", "`")
    with open(history, 'a+') as file:
        with open(history, 'r') as fp:
            line = len(fp.readlines())
            fp.close()
        x = (int(line) + int("1"))
        No = str(x)
        set = {"SNo": No , "Name": Title[:50], "URL": link, "Site": site}
        file.write(json.dumps(set)+str("\n"))
    file.close()
    os.remove(temp_loc)

#(YT-DLP) Downloader:
def downloader(opt, site):
    import yt_dlp
    with yt_dlp.YoutubeDL(opt) as yt:
        info = yt.extract_info(link, download=True)
        title = info.get('title', None)
        with open(json_path,'r') as file:
            data = json.load(file)
            state = data["default"][0]["incognito"]
        if state == "off":
            history(title, site)
        else:
            os.remove(temp_loc)
            exit()

#(Youtube) Video
def video(mode):
    if "playlist" in link:
        path = genPath+'Termux_Downloader/Youtube/%(playlist)s/%(title)s.%(ext)s'
        thumb = bool(True)
    else:
        path = genPath+'Termux_Downloader/Youtube/%(title)s.%(ext)s'
        thumb = bool(True)
    if mode == "Youtube":
        print("Downloading video from YouTube:\n")
        #Default creation, import and modification segment:
        with open(json_path, "r") as defaultFile:
            data  = json.load(defaultFile)

            if data["default"][0]["code"] == "":
                print('Enter the respective code for Required Resolution:')
                print('[code] - [Resolution]')
                print('1 - 4k')
                print('2 - 2k')
                print('3 - 1080p')
                print('4 - 720p')
                print("5 - 480p")
                print('6 - 360p')
                print('7 - 240p')
                print('8 - 144p')

                i = input('Resolution Code: ')
                print("\n")  
                data["default"][0]["code"] = i
                
                with open(json_path, "w") as defaultFile:
                    json.dump(data, defaultFile)
                defaultFile.close

                with open(json_path, "r") as default:
                    data = json.load(default)
                    code = data["default"][0]["code"]
                    j = data[code][0]["height"]
                    k = data[code][0]["res"]
                default.close
                
            else:
                with open(json_path, "r") as default:
                    data = json.load(default)
                    code = data["default"][0]["code"]
                    k = data[code][0]["res"]
                    choice = input("Default resolution is " +k+ ". If you want to download in different resolution type (y) or skip:" )
                    print("\n")
                    if choice =="y":
                        print('Enter the respective code for Required Resolution:')
                        print('[code] - [Resolution]')
                        print('1 - 4k')
                        print('2 - 2k')
                        print('3 - 1080p')
                        print('4 - 720p')
                        print("5 - 480p")
                        print('6 - 360p')
                        print('7 - 240p')
                        print('8 - 144p')

                        i = input('Resolution Code: ')
                        print("\n")  
                        data["default"][0]["code"] = i
                    
                        with open(json_path, "w") as defaultFile:
                            json.dump(data, defaultFile)
                        defaultFile.close

                        with open(json_path, "r") as default:
                            data = json.load(default)
                            code = data["default"][0]["code"]
                            j = data[code][0]["height"]
                            k = data[code][0]["res"]
                        default.close
                
                    else:
                        j = data[code][0]["height"]
                        k = data[code][0]["res"]
                default.close

        print('Note: The video will download in '+k+' Resolution if youtube has such resolution. If not it will download the Best of resolution available in URL.\n')
        format = 'bestvideo[height<='+j+']+bestaudio[ext=m4a]/best[height<='+j+']/best[ext=m4a]'
    elif mode == "best":
        print("Downloading best one from YouTube:\n")
        format = 'best'
    elif mode == "advanced":
        print("Downloading from YouTube - Advanced mode:\n")
        os.system("yt-dlp -F " +link)
        if "youtube" in link or "youtu.be" in link:
            vid = input('Video id: \n')
            aid = input('Audio id: \n')
            format = str(vid)+" + "+str(aid)
        else:
            format = input("Enter the format code from above list:")
            print("\n")
    else:
        linkDistributor()

    if input("Do you need subtitle? If yes, type 'y' or skip! :") == "y":
        choice = bool(True)
    else:
        choice = bool(False)
    print("\n")
    opt = {
                'external_downloader' : 'aria2c',
                'outtmpl' : path,
                'writesubtitles' : choice,
                'writeautomaticsub' : choice,
                'merge_output_format' : 'mp4',
                'writethumbnail' : thumb,
                'format' : format,
                'postprocessors' :
                                    [
                                        {
                                            'key' : 'FFmpegEmbedSubtitle',
                                            'already_have_subtitle' : False
                                        },
                                        {
                                                'key' : 'FFmpegMetadata',
                                                'add_metadata' : True
                                        },
                                        {
                                                'key' : 'EmbedThumbnail',
                                                'already_have_thumbnail' : False
                                        }
                                    ]
            }   
    downloader(opt, site = mode) 

#(Youtube) Audio
def audio(dir):
    print("Downloading songs from "+dir+": \n")
    with open(json_path, "r") as defaultFile:
        data = json.load(defaultFile)
        
    #json key first time allotment
    if data["default"][0]["codec"] == "":
        print('Enter the Format of audio (mp3, aac, m4a, flac....)')
        firstCodec = input('Enter the format: ')
        data["default"][0]["codec"] = firstCodec
    
        with open(json_path, "w") as defaultFile:
            json.dump(data, defaultFile)
        defaultFile.close

        with open(json_path, "r") as default:
            data = json.load(default)
            codec = data["default"][0]["codec"]
        default.close
    
    #json key for later use
    else:
        with open(json_path, "r") as default:
            data = json.load(default)
            notification = data["default"][0]["codec"]
            choice = input("Default audio codec is " +notification+ ". If you need to download in different codec type (y) or else skip:")
            print("\n")
            if choice == "y":
                print('Enter the Format of audio (mp3, aac, m4a, flac....)\n')
                lateCodec = input('Enter the format: ')
                print("\n")                
                with open(json_path, "r") as defaultFile:
                    data = json.load(defaultFile)
                    data["default"][0]["codec"] = lateCodec
                
                with open(json_path, "w") as defaultFile:
                    json.dump(data, defaultFile)
                defaultFile.close

                with open(json_path, "r") as defa:
                    data = json.load(defa)
                    codec = data["default"][0]["codec"]
                defa.close
            
            else:
                codec = data["default"][0]["codec"]
            default.close
    
    path = genPath+"Termux_Downloader/"+dir+"/"
    exist = os.path.isdir(path)
    if exist:
        pass
    else:
        os.mkdir(path)
        
    if "playlist" in link:
        op_path =  path + '/%(playlist)s/%(title)s.%(ext)s'
        thumb = bool(True)
    else:
        op_path =  path + '%(title)s.%(ext)s'     
        thumb = bool(True)
        
    opt = {
            'format' : 'bestaudio/best',
            'writethumbnail' : thumb,
            'ignoreerrors': True,
            'outtmpl': op_path,
            'postprocessors' :
                [
                    {
                        'key' : 'FFmpegExtractAudio',
                        'preferredcodec' : codec,
                    },
                    {
                        'key': 'FFmpegMetadata',
                        'add_metadata' : True,     
                    },
                    {
                        "key" : 'EmbedThumbnail',
                        'already_have_thumbnail'  : False,
                    }
                ]
             }
    if dir == "YTmusic":
        site = "Youtube Music"
    else:
        site = "Youtube"
    downloader(opt, site= site) 

#(Others) Social Media and download supported video steaming sites:
def others():
    if "www" in link:
        l1 = link.split("www.")
    else:
        l1 = link.split("://")
    l2 = l1[1].split(".")
    dir_name = l2[0].capitalize()
    print("Downloading from " +colored(dir_name,'magenta'))
    print("\n")
    path = genPath+'Termux_Downloader/'+ dir_name +'/'
    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path)

    opt = {                
                    'outtmpl': path + "%(title).50s.%(ext)s",
                    'external_downloader': 'aria2c',
                    'writesubtitles' : True,
                    'writeautomaticsub' : True, 
                }
    try: #Try the video is downloadable from the site           
        downloader(opt,site = dir_name)   
    except: #Else delete the folder created to download if only site is not downloadable
        os.rmdir(path)

#(General Downloader)From FTP links and Torrent:
def genDown():
    if "magnet" in link:
        print("Downloading Torrent file from Magnet link:\n")
        path = genPath+"Termux_Downloader/Torrents/"
    else:
        print("Downloading from FTP link:")
        path = genPath+"Termux_Downloader/Downloads/"

    code = "aria2c -d '"+ path + "' '"+ link + "' --file-allocation=none"
    if os.path.isdir(path):
        os.system(code)
    else:
        os.mkdir(path)
        os.system(code)

#(Drive) Google Drive:
def drive():
    id1 = link.replace("https://drive.google.com/file/d/", "")
    split = id1.split("/", 1)
    id = split[0]
    path = genPath+"Termux_Downloader/Gdrive/"
    code = "gdown -O '" + path + "' --id '" + id + "'"
    exist = os.path.isdir(path)
    if exist:
        os.system(code)
    else:
        os.mkdir(path)
        os.system(code)
  
#(Master) Link Assortment (Distributor)
def linkDistributor():
    if "drive" in link:
        drive()
    elif "magnet" in link:
        genDown()
    elif "music" in link:
        audio(dir= "YTmusic")
    elif "youtube" in link or "youtu.be" in link:
        path = genPath + 'Termux_Downloader/Youtube/'
        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)
        print('Enter \n*(v) for Video \n*(a) for audio \n*(m) for advanced \n*(b) for best')
        T = input('v or a or m or b: ')
        print("\n") 
        if T=="v":
            video(mode= "Youtube")
        elif T=="m":
            video(mode = "advanced")
        elif T=="a":
            print("Downloading Audio track from YouTube:")
            audio(dir= "Youtube")
        elif T=="b":
            video(mode= "best")
        else:
            linkDistributor()  
    else:
        try:
            others()
        except:
            genDown()

#(Master) General Directory in Internal Storage
def masterDirectory():
    path = genPath + "Termux_Downloader/"
    exist = os.path.isdir(path)
    if exist:
        #Empty directory scanner and remover
        def list():
            empty_Dir = []
            for root, dirs, files in os.walk(path):
                if not len(dirs) and not len(files):
                    empty_Dir.append(root)
            
            if not len(empty_Dir) == int("0"):
                for x in empty_Dir:
                    os.rmdir(x + "/")
                empty_Dir.clear()
                list()
            else:
                pass
        list()      
        linkDistributor()
    else:
        os.mkdir(path)
        linkDistributor()

masterDirectory()
