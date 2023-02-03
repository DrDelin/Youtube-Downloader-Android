#Version 5.0.0.0
#Engine 5.0

#(Master) imports
import os
import sys
import linecache
import json

#Version Info:
version = (linecache.getline(linecache.sys.argv[0],1))
print(version.replace("#", ""))
linecache.clearcache()

#Engine info:
engine = (linecache.getline(linecache.sys.argv[0],2))
print(engine.replace("#", ""))
linecache.clearcache()

#Update news:
print("(Changelog)Whats new...!\n")
print("(Engine) New Update and Upgrade Mechanism \n(Engine) Update server changed \n(Main) Downloader performance optimized \n")

#(Default) JSON file creation or verification:
json_path = "/data/data/com.termux/files/home/default.json"

if os.path.isfile(json_path):
    pass
else:
    jsonnew = {
        "default" : [
            {
                "code" : "",
                "codec" : ""
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
    try:
        import mutagen
    except ModuleNotFoundError():
        os.system('pip install mutagen')

dependency()

#(Master) Automated link grabbing from Termux url Opener
link = sys.argv[1]

#Output Directory

if "music" in link:
    output_directory = "'/storage/emulated/0/Termux_Downloader/YTmusic/%(title)s.%(ext)s' "
else:
    output_directory = "'/storage/emulated/0/Termux_Downloader/Youtube/%(title)s.%(ext)s' "

#(Master) History:
def history(link, site):
    import yt_dlp
    history = "/data/data/com.termux/files/home/history.txt"

    opt =  {
        'skip_download' : True,
        'quiet' : True
    }
    with yt_dlp.YoutubeDL(opt) as ytd:
        info = ytd.extract_info(link)
        N = info.get('title', None)
        Title0 = N.replace('"',"`")
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

#(Master) History 2.0:
def history_2(title, site):
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

#(Others) Social Media and download supported video steaming sites:
def others():
    if "www" in link:
        l1 = link.split("www.")
    else:
        l1 = link.split("://")
    l2 = l1[1].split(".")
    dir_name = l2[0].capitalize()
    print("Downloading from " +dir_name)
    path = '/storage/emulated/0/Termux_Downloader/'+ dir_name +'/'
    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path)
    import yt_dlp
    ytd_opts = {                
                    'outtmpl': path + "%(title).50s.%(ext)s",
                    'external_downloader': 'aria2c', 
                }
    try: #Try the video is downloadable from the site           
        with yt_dlp.YoutubeDL(ytd_opts) as ydl:
                info = ydl.extract_info(link, download=True)
                title = info.get('title', None)
        history_2(title, site= dir_name)   
    except: #Else delete the folder created to download if only site is not downloadable
        os.rmdir(path)

#(Torrent) Downloader
def torrentCodec():
    print("Downloading a torrent:")
    magnet = "'" +link +"'"
    engine = input(" a for aria (or) t for transmission: ")
    if engine=="a":
        code = "aria2c -d '/storage/emulated/0/Termux_Downloader/Torrent/' " +magnet+ " --file-allocation=none"
    elif engine=="t":
        code = "transmission-cli -w '/storage/emulated/0/Termux_Downloader/Torrent/' " +magnet
    else:
        torrentCodec()
    os.system(code)

#(Seedr)From Seedr ftp:
def seedr():
    print("Downloading from seedr:")
    path = "/storage/emulated/0/Termux_Downloader/Seedr/"
    code = "aria2c -d '"+ path + "' '"+ link + "' --file-allocation=none"
    if os.path.isdir(path):
        os.system(code)
    else:
        os.mkdir(path)
        os.system(code)

#(Youtube) Advanced download
def advanced():
    print("Downloading from YouTube - Advanced mode:")
    os.system("yt-dlp -F " +link)
    vid = input('Video id: ')
    aid = input('Audio id: ')
    sub = input("Subtitle y/n: ")
    format = str(vid)+" + "+str(aid)
    path = '/storage/emulated/0/Termux_Downloader/Youtube/%(title)s.%(ext)s'
    
    if sub=="y":
        print("Note: If the video doesn't have default subtitle on URL, Subtitle won't available")
        opt = {
                'external_downloader' : 'aria2c',
                'outtmpl' : path,
                'writesubtitles' : True,
                'subtitle' : "--sub-lang en-en-US --sub-lang en-GB --sub-lang en --convert-sub srt --write-sub --embed-subs",
                'merge_output_format' : 'mp4',
                'writethumbnail' : True,
                'format' : format,
                'postprocessors' :
                                    [
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
    elif sub=="n":
        opt = {
            'external_downloader' : 'aria2c',
            'outtmpl' : path,
            'merge_output_format' : 'mp4',
            'writethumbnail' : True,
            'format' : format,
            'postprocessors' :
                                [
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
    else:
        advanced()
    
    import yt_dlp
    
    with yt_dlp.YoutubeDL(opt) as yt:
        info = yt.extract_info(link, download=True)
        title = info.get('title', None)
        history_2(title, site= "Youtube Advanced")


#(Youtube) Best
def best():
    print("Downloading best one from YouTube:")
    history(link, site="Youtube (Best)")
    code = "yt-dlp --external-downloader aria2c --embed-thumbnail --add-metadata -o "+output_directory+" --format best " + "'" + link + "'"
    os.system(code)

#(Youtube) Video
def video():
    print("Downloading video from YouTube:")
    history(link, site="Youtube")
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
    
    print('Note: The video will download in '+k+' Resolution if youtube has such resolution. If not it will download the Best of resolution available in URL. And if you want to get list of available formats and different fps and quality go to advanced')

    usr = input("Do you need to go advanced mode type (y) else skip: ")
    
    if usr=="y":
        advanced()

    else:
        def nsv():
            format = '"bestvideo[height<='+j+']+bestaudio[ext=m4a]/best[height<='+j+']/best[ext=m4a]" --merge-output-format mp4 '
            code = "yt-dlp --external-downloader aria2c --embed-thumbnail --add-metadata -o "+output_directory+" -f "+format + "'" + link + "'"
            os.system(code)

        def sv():
            format = '"bestvideo[height<='+j+']+bestaudio[ext=m4a]/best[height<='+j+']/best[ext=m4a]" --sub-lang en-en-US --sub-lang en-GB --sub-lang en --write-auto-subs --convert-subs srt --write-sub --embed-sub --merge-output-format mp4 '
            code = "yt-dlp --external-downloader aria2c --embed-thumbnail --add-metadata -o "+output_directory+" -ci -f "+format + "'" +link + "'"
            os.system(code)

        subs = input('With Subtitle (y) or skip: ')

        if subs=="y":
            sv()
        else:
            nsv()


#(Youtube Music) Directory creation
def YTmusicDirectory():
    print("Downloading songs from YouTube Music:")
    path = "/storage/emulated/0/Termux_Downloader/YTmusic/"
    exist = os.path.isdir(path)
    if exist:
        audio()
    else:
        os.mkdir(path)
        audio()

#(Youtube) Audio
def audio():
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
    
            if choice == "y":
                print('Enter the Format of audio (mp3, aac, m4a, flac....)')
                lateCodec = input('Enter the format: ')
                
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
    
    if "playlist" in link:
        import yt_dlp
        path = "/storage/emulated/0/Termux_Downloader/YTmusic/"     
        ytd_opts = {
                    'format' : 'bestaudio/best',
                    'writethumbnail' : 'True',
                    'ignoreerrors': True,
                    'outtmpl': path + '/%(playlist)s/%(title)s.%(ext)s',
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
        with yt_dlp.YoutubeDL(ytd_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            title = info.get('title', None)
        history_2(title, site="Youtube Music")

    else:
        import yt_dlp
        path = "/storage/emulated/0/Termux_Downloader/YTmusic/"             
        ytd_opts = {
                            'format' : 'bestaudio/best',
                            'writethumbnail' : 'True',
                            'ignoreerrors': True,
                            'outtmpl': path + '%(title)s.%(ext)s',
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
        with yt_dlp.YoutubeDL(ytd_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            title = info.get('title', None)
        history_2(title, site="Youtube Music")     

#(Drive) Google Drive:
def drive():
    id1 = link.replace("https://drive.google.com/file/d/", "")
    split = id1.split("/", 1)
    id = split[0]
    path = "/storage/emulated/0/Termux_Downloader/Gdrive/"
    code = "gdown -O '" + path + "' --id '" + id + "'"
    exist = os.path.isdir(path)
    if exist:
        os.system(code)
    else:
        os.mkdir(path)
        os.system(code)

#(Youtube) Assortment of media to download
def codec():
  
    #(Youtube Music) Redirection to Audio Function Without confirmation for Youtube music links
    if "music" in link:
          audio()
  
    else:
        print('***Enter \n(v) for Video \n(a) for audio \n(m) for advanced \n(b) for best')
   
        T = input('v or a or m or b: ')
   
        if T=="v":
            video()
        elif T=="m":
            advanced()
        elif T=="a":
            print("Downloading Audio track from YouTube:")
            audio()
        elif T=="b":
            best()
        elif T=="dev":    #For developers
            code = "sh '/data/data/com.termux/files/home/refresh.sh'"
            os.system(code)
            quit()
        else:
            codec()

#(Youtube) Youtube Download Directory
def youtubeDirectory():
    path = "/storage/emulated/0/Termux_Downloader/Youtube/"
    if os.path.isdir(path):
        codec()
    else:
        os.mkdir(path)
        codec()

#(Torrent) Download Directory creation and verification
def torrentDownload():
    path = '/storage/emulated/0/Termux_Downloader/Torrent/'
    if os.path.isdir(path):
        torrentCodec()
    else:
        os.mkdir(path)
        torrentCodec()

#(Master) Link Assortment (Distributor)
def linkDistributor():
    if "magnet" in link:
        torrentDownload()
    elif "seedr" in link:
        seedr()
    elif "drive" in link:
        drive()
    elif "music" in link:
        YTmusicDirectory()
    elif "youtube" in link:
        youtubeDirectory()
    elif "youtu.be" in link:
        youtubeDirectory()
    else:
        others()

#(Master) General Directory in Internal Storage
def masterDirectory():
    path = "/storage/emulated/0/Termux_Downloader/"
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