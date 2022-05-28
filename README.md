# SM64LLPi
![made-for-raspberry-pi](https://user-images.githubusercontent.com/102569285/170807737-c7e19f08-ab89-4fd2-860f-d5c40641fbaf.svg)

A fork of SM64LinuxLauncher made for Raspberry Pi. Tested on Raspberry Pi 4B with Raspberry Pi OS 32 bit and 64 bit.
![sm64ll-pi](https://user-images.githubusercontent.com/102569285/169741647-66f9b1bb-ebdc-4223-b1dc-d8a649fb7e7c.png)

## Requirements
A rom of Super Mario 64 ending in .z64 and python 3, which is already included with Raspberry Pi OS. The rest of the packages will automatically be installed.

## Installation
IMPORTANT: MAKE SURE YOU CLONE IT IN THE DOWNLOADS DIRECTORY!!!
1. Open /home/pi/Downloads in terminal and run `git clone https://github.com/faizu396/sm64ll-pi`
2. cd into the sm64ll-pi folder
3. Run `sudo chmod 777 setup.sh` and `./setup.sh`


## Usage
### Running

Type in terminal `python3 launcher.py` (you must be in sm64ll-pi/src directory)
or  
Use the application from the games menu

### Using it

To build sm64, press "Build"  
To play, select existing build and click "Play"  

## How to build

In the drop down menu, select a repo. If you don't know what this means, just choose sm64ex-nightly.

In the second box, type any name you want for your repo folder. it will display like that in the launcher build selection.  

In the other two boxes you can specify modelpack and texture pack folder. These are optional and don't need to be chosen.

Click "Ok". it will freeze for a while this is because it is downloading the repo. 

Click "Browse" and find your Super Mario 64 rom ending with .z64. Select if it us a us, jp, or eu rom. Click "Ok"  

Specify the build flags, you can find which build flags are avaible for your repo by checking the makefile or checking your repo's wiki if it exists. If you don't know what this means, just leave it blank.

Click "Build". Now wait patiently for the build to finish. When it finishes, game should lauch shortly after. If you see a text box and the game does not launch for like 2 minutes, it means that your build failed. delete the repo folder and try to build again. If the game launches, it is ok. When you restart the launcher, it should show the new build on the list.

## Themes

In the themes folder, there are a couple of shell scripts for changing the themes. Run whichever one you want in terminal to choose that specific theme.
