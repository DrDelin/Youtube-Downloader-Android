# Termux Downloader Android (BETA VERSION)
  ## FOR DEVELOPER USE ONLY
 
  ## Beta channel fresh installation:
  
      pkg up -y -y -y -y
      pkg install git -y
      git clone https://github.com/DrDelin/Youtube-Downloader-Android/ -b beta --single-branch
      cd Youtube-Downloader-Android
      sh install.sh
  
  ### Switch between Stable and Beta:
  1. Open termux
  2. (For first time only) pkg install vim-gtk -y
  3. Edit refresh.sh file with ```vi refresh.sh```
  4. Change the 12th line,  
      a. Stable -> Beta: change ***master*** to ***beta***   
      b. Beta -> Stable: change ***beta*** to ***master***  
  5. Exit vim editor(esc -> :wq -> enter)
  6. Then, run ```sh refresh.sh```

  Warning!! Again this is strictly for developers.. So, Recommended to use Stable version.  
