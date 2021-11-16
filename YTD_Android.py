#Version 2.0.0.0

#(Master) imports
import os
import sys

#Version Info:
with open(sys.argv[0]) as m:
    a = m.readline().rstrip()
    ver = a.replace("#", "")
print(ver)
m.close()

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

#(Torrent) Downloader
def torrentCodec():
    magnet = "'" +link +"'"
    code = "transmission-cli -w '/storage/emulated/0/Termux_Downloader/Torrent/' " +magnet
    os.system(code)

#(Facebook) Facebook Download Directory:
def facebook():
    path = "/storage/emulated/0/Termux_Downloader/Facebook/"
    exist = os.path.isdir(path)
    code = "yt-dlp -o '/storage/emulated/0/Termux_Downloader/Facebook/%(title)s.%(ext)s' " +link
    if exist:
        os.system(code)
    else:
        os.mkdir(path)
        os.system(code)

#(Twitter) Twitter Download Directory:
def twitter():
    path = "/storage/emulated/0/Termux_Downloader/Twitter/"
    exist = os.path.isdir(path)
    code = "yt-dlp -o '/storage/emulated/0/Termux_Downloader/Twitter/%(title)s.%(ext)s' " +link
    if exist:
        os.system(code)
    else:
        os.mkdir(path)
        os.system(code)

#(Instagram) Instagram Download Directory:
def instagram():
    path = "/storage/emulated/0/Termux_Downloader/Instagram/"
    exist = os.path.isdir(path)
    code = "yt-dlp -o '/storage/emulated/0/Termux_Downloader/Instagram/%(title)s.%(ext)s' " +link
    if exist:
        os.system(code)
    else:
        os.mkdir(path)
        os.system(code)

#(Random Sites) Random Download Directory:
def others():
    path = "/storage/emulated/0/Termux_Downloader/Others/"
    exist = os.path.isdir(path)
    code = "yt-dlp -o '/storage/emulated/0/Termux_Downloader/Others/%(title)s.%(ext)s' " +link
    if exist:
        os.system(code)
    else:
        os.mkdir(path)
        os.system(code)

#(Youtube) Advanced download
def advanced():  
    os.system("yt-dlp -F " +link)
    vid = input('Video id: ')
    aid = input('Audio id: ')
    sub = input("Subtitle y/n: ")
    fit = ' -f "'
    format = fit+str(vid)+" + "+str(aid)
    
    def nsv():
        code = "yt-dlp --embed-thumbnail --add-metadata -o "+output_directory+format+'" --merge-output-format mp4 ' +link
        os.system(code)
    
    def sv():
        print("Note: If the video doesn't have default subtitle on URL, Subtitle won't available")
        code = "yt-dlp --embed-thumbnail --add-metadata -o "+output_directory+" -ci "+format+'" --write-sub --sub-lang en --embed-subs --merge-output-format mp4 ' +link
        os.system(code)

    if sub=="y":
        sv()

    elif sub=="n":
        nsv()

    else:
        advanced()

#(Youtube) Best
def best():
    code = "yt-dlp --embed-thumbnail --add-metadata -o "+output_directory+" --format best " +link
    os.system(code)

#(Youtube) Video
def video(): 
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
    
    if i== "1":
        j = '2160'
        k = '4k'
    elif i== "2":
        j = "1440"
        k = '2k'
    elif i== "3":
        j = "1080"
        k = '1080p'
    elif i== "4":
        j = "720"
        k = '720p'
    elif i== "5":
        j = "480"
        k = '480p'
    elif i== "6":
        j = "360"
        k = '360p'
    elif i== "7":
        j = "240"
        k = '240p'
    elif i== "8":
        j = "144"
        k = '144p'
    
    else:
        print('Wrong Code :(')
        return video()
    
    print('Note: The video will download in '+k+' Resolution if youtube has such resolution. If not it will download the Best of resolution available in URL. And if you want to get list of available formats and different fps and quality go to advanced')

    usr = input("Do you need to go advanced mode (y/n): ")
    
    if usr=="y":
        advanced()

    elif usr=="n":

        def nsv():
            format = '"bestvideo[height<='+j+']+bestaudio[ext=m4a]/best[height<='+j+']/best[ext=m4a]" --merge-output-format mp4 '
            code = "yt-dlp --embed-thumbnail --add-metadata -o "+output_directory+" -f "+format +link
            os.system(code)

        def sv():
            format = '"bestvideo[height<='+j+']+bestaudio[ext=m4a]/best[height<='+j+']/best[ext=m4a]" --write-sub --sub-lang en --embed-subs --merge-output-format mp4 '
            code = "yt-dlp --embed-thumbnail --add-metadata -o "+output_directory+" -ci -f "+format +link
            os.system(code)

        subs = input('With Subtilte (y) or without subtitle (n): ')

        if subs=="y":
            sv()
        elif subs=="n":
            nsv()
        else:
            video()

    else:
        return video()

#(Youtube Music) Directory creation
def YTmusicDirectory():
    path = "/storage/emulated/0/Termux_Downloader/YTmusic/"
    exist = os.path.isdir(path)
    if exist:
        audio()
    else:
        os.mkdir(path)
        audio()

#(Youtube) Audio
def audio():

    print('Enter the Format of audio (mp3, aac, m4a, flac....)')
    codec = input('Enter the format: ')
    code = "yt-dlp --embed-thumbnail --add-metadata -o "+output_directory+" -x --audio-format "+codec+" '"+link + "'"
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
    elif "music" in link:
        YTmusicDirectory()
    elif "facebook" in link:
        facebook()
    elif "twitter" in link:
        twitter()
    elif "instagram" in link:
        instagram()
    elif "youtube" or "youtu.be" or "youtu" in link:
        youtubeDirectory()
    else:
        others()

#(Master) General Directory in Internal Storage
def masterDirectory():
    path = "/storage/emulated/0/Termux_Downloader/"
    exist = os.path.isdir(path)
    if exist:
        linkDistributor()
    else:
        os.mkdir(path)
        linkDistributor()

masterDirectory()