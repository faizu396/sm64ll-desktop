# SM64LLPi
A fork of SM64LinuxLauncher made for Raspberry Pi
![screenshot](https://cdn.discordapp.com/attachments/886701656488697878/919333674229583923/Zrzut_ekranu_z_2021-12-11_22-02-23.png)

## Requirements
Just python 3. The rest of the packages will automatically be installed.

## Linux installation
1. Download Source Code zip and unpack
2. Open the folder in terminal
3. Run `sudo chmod 777 setup.sh` and `./setup.sh`


## Usage
### Running on Linux

Type in terminal `python3 launcher.py` (you must be in laucnher directory)
or  
Use the application from the games menu

### Using it

To build sm64, press "Build"  
To play, select existing build and click "Play"  

## How to build

In the drop down menu, select a repo. If you don't know what this means, just choose sm64ex

In the second box, type any name you want for your repo folder. it will display like that in the launcher build selection.  

In the other two boxes you can specify modelpack and texture pack folder. Note: when you browse for the folder, you have to be in this folder to select it.  

Click "Ok". it will freeze for a while this is because it is downloading the repo. 

Click "Browse" and find your Super Mario 64 rom. Select if it us a us, jp, or eu rom. Click "Ok"  

Specify the build flags, you can find which build flags are avaible for your repo by checking the makefile or checking your repo's wiki if it exists. Remember to add "-j4" for faster building speed. 

Click "Build". Now wait patiently for the build to finish. When it finishes, game should lauch shortly after. If you see a text box and the game does not launch for like 2 minutes, it means that your build failed. delete the repo folder and try to build again. If the game launches, it is ok. When you restart the launcher, it should show the new build on the list.
