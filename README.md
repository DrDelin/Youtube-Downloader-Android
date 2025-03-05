# Termux Downloader Android (aka Youtube-Downloader-Android)
  ### History of developement of this script
  Hi all! This script was once intended to download video and audio, only from youtube. Later it is extended to download videos from almost all sites and social media, torrents and Google drive. This script based on Termux app for downloading. Hence it is Termux Downloader. It supports almost all websites steaming videos (except sites with DRM), and also compatible with links from YouTube and YouTube Music app, also links from both app and website of social media(like Fb, twitter/X, Instagram, reddit etc..).
  
  ### Developers
  * Owner and Developer: **Dr.Delin @DrDelin**
  * Co-Developer and script optimizer: **Dr.Senthil Manikandan @Senthil360**
  * Script watcher and contributor: **Dr.Dhinesh cool**

## Installation(Stable version):
  1. Install termux from github https://github.com/termux/termux-app/releases (arm64 recommended ,use arm only for device lower than android 7)
  2. Type the commands or just copy or use the *copy button* provided and **Paste it on termux**:(Note)(For first time installation, type 'y' whenever it asks inbetween)
      ```
      pkg up -y -y -y -y
      pkg install git -y
      git clone https://github.com/DrDelin/Youtube-Downloader-Android/ -b master --single-branch
      cd Youtube-Downloader-Android
      sh install.sh
        ```
  3.  (Must)Press ALLOW to give storage permission or go to Termux app settings and give STORAGE permission
  4. (Important) For Android 10 or above users: Go to app settings -> Termux app settings -> Give ALLOW to "Display over other apps" permission for working of this script 

## Usage:
  ### How to download videos or audio:
  1. Open the desired video or audio or playlist or site in which the video is present, Including social media apps, browser pages etc..
  2. Select share option (used to share the link)
  3. Select TERMUX from the share list
  4. Thats all! Your video / audio / playlist will download (Location: Internal storage of your device -> Termux-Downloader)
  5. (For Youtube Download) Select Video / audio / best -> Select required resolution once, later it is set as default (can be changed if you type "y") -> skip next (unless if you want custom format) -> type "y" if you need subtitle(Subtitle only available if only youtube has..) -> Forget rest!... My script will take care
  6. (For Youtube Music / audio from youtube) Type your favourite audio codec (like mp3, m4a, aac, webm, flac...) for one time as default (can be changed later) -> Audio will be downloaded in your favourite codec
  7. Note: This script is completely automated, hence the program closes itself after downloading.. Hence, Share your link to Termux.. Go get some coffee..! See your file will be in internal storage of the device 

## Utilities:
Termux-Downloader has an utilities option with various features
  ### How to open utilities option:
  1. Open Termux app
  2. Type ```tools```
  3. From the available options, select whichever you need.

  ### Available Utilities:
  1. Copied Link - Manual Download
  2. Download History
  3. Backup History
  4. Import history file
  5. Delete History
  6. Manual Script Upgrade
  7. Factory Default Reset
  8. Script Build Info
  9. App and Script Developers Info
  10. Incognito Mode for Downloads

## Troubleshooting or repairing:
  Incase if the program not working properly or not downloading or showing errors, just follow these steps,
  1. Open termux app
  2. Type ```sh refresh.sh```
  3. Program gets clean installed or returned to factory default


## Features:
  ### History:
  1. The name, site of download, and URL of the files downloaded by this script are saved as history.
  2. History feature is created to:
      * Redownload the file which is previously downloaded  
      * Revisit the site from which the file is downloaded
  3. To view/re-download/re-visit/delete history, open utilities to do so(Open Termux app -> type ```tools```).

  ### Updates:
  1. Updates are completly automatic and you won't need to worry about it.
  2. Manuallly update can be done in utilities menu.
  3. If you are facing any issue on new update or having any suggestions on a new feature, make it a note in issue section

## (Not Recommended!)(Developers only)Beta Channel installation or switch over btw Stable and Beta:
  Warning! This Channel is only for DEVELOPER'S BETA TESTING! May have bugs and fatal flaws and may not contain many features. Hence, PROCEED WITH CAUTION.
  ## Beta channel fresh installation:
  
      pkg up -y -y -y -y
      pkg install git -y
      git clone https://github.com/DrDelin/Youtube-Downloader-Android/ -b Sigma-D --single-branch
      cd Youtube-Downloader-Android
      sh install.sh
  
  ### Switch between Stable and Beta:
  1. Open termux
  2. (For first time only) pkg install vim-gtk -y
  3. Edit refresh.sh file with ```vi refresh.sh```
  4. Change the 12th line,  
      a. Stable -> Beta: change ***master*** to ***Sigma-D***   
      b. Beta -> Stable: change ***Sigma-D*** to ***master***  
  5. Exit vim editor(esc -> :wq -> enter)
  6. Then, run ```sh refresh.sh```

  Warning!! Again this is strictly for developers.. So, Recommended to use Stable version.  
