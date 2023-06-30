#!/usr/bin/env python3

import PySimpleGUI as sg
import os
from themeconfig import *
import subprocess

# Utility Function Definition
def run(command):
    return subprocess.run(
        command,
        shell=True,
    ).returncode

# Create an event loop
def build():
    sg.theme_background_color(windowBackgroundColor)  

    # define screens
    buildfailed = [
        [sg.Text('Build failed, try to build again', text_color=textColor, background_color=windowBackgroundColor), sg.Button('Ok', button_color=('white', bottomButtonColor))]
    ]
    branchselect = [
        [sg.Text("Select a Repository. (If you do not select a valid repo, the builder will automaticaly default to sm64ex-nightly).", text_color=textColor, background_color=windowBackgroundColor)],
        [sg.Combo(['sm64ex-nightly',
                   'sm64ex-master',
                   'sm64ex-coop',
                   'Render96ex-master',
                   'Render96ex-tester',
                   'Render96ex-tester_rt64alpha',
                   'Saturn',
                   'Saturn: Moon Edition',
                   'SM64Plus (Very Slightly Buggy)',
                   'sm64ex-alo'], background_color=boxColor,text_color=boxTextColor),],
        [sg.Text("Type the name of repo folder:", text_color=textColor, background_color=windowBackgroundColor)],
        [sg.In(background_color=boxColor, text_color=boxTextColor)],
        [sg.Text('Pick a Model Pack folder (optional):', text_color=textColor, background_color=windowBackgroundColor)],
        [sg.In(background_color=boxColor, text_color=boxTextColor),sg.FolderBrowse(button_color=("white",otherButtonColor))],
        [sg.Text('Pick a Texture Pack folder (optional):', text_color=textColor, background_color=windowBackgroundColor)],
        [sg.In(background_color=boxColor, text_color=boxTextColor),sg.FolderBrowse(button_color=('white',otherButtonColor))],
        [sg.Button("Ok", button_color=("white",bottomButtonColor))]
    ]
    buildoptions = [
        [sg.Text('specify build flags and jobs, you can see possible flags on your repo\'s wiki, if you use modelpack, use MODELPACK=1, if you use texturepack, use EXTERNAL_DATA=1',text_color=textColor, background_color=windowBackgroundColor)],
        [sg.In(text_color=boxTextColor, background_color=boxColor),sg.Button('Build', button_color=("white",otherButtonColor))],

    ]
    baseromselect = [[sg.Text("Select baserom of sm64 with extension .z64",text_color=textColor, background_color=windowBackgroundColor)],[
            sg.Text("baserom:", background_color=windowBackgroundColor, text_color=textColor),
            sg.In(background_color=boxColor, text_color=boxTextColor),
            sg.FileBrowse(button_color=("white",otherButtonColor)),
            sg.Text("region:", background_color=windowBackgroundColor,text_color=textColor),
            sg.Combo(['us','jp','eu'], background_color=boxColor,text_color=boxTextColor)

        ],[sg.Button("Ok",button_color=("white",bottomButtonColor))]]

    downloading = [[sg.Text('Downloading the repo (Do not close this window if it says "not responding")', text_color=textColor, background_color=windowBackgroundColor)]]
    building = [[sg.Text('Building... (Do not close this window if it says "not responding")', text_color=textColor, background_color=windowBackgroundColor)]]


    # Create the window
    window = sg.Window("SM64 Linux Builder", branchselect)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        if event == "Ok":
            repolink, branchname, repofolder, texturepack, modelpackfolder = values[0], values[0], values[1], values[3], values[2] # pattern matching for variable setup
            window.close() # close current window to start processing

            match repolink: # use new match statement starting python3.10
                case 'sm64ex-nightly':
                    repolink = 'https://github.com/sm64pc/sm64ex'
                    branchname = 'nightly'

                case 'sm64ex-master':
                    repolink = 'https://github.com/sm64pc/sm64ex'
                    branchname = 'master'

                case 'Render96ex-master':
                    repolink = 'https://github.com/Render96/Render96ex/'
                    branchname = 'master'

                case 'Render96ex-tester':
                    repolink = 'https://github.com/Render96/Render96ex'
                    branchname = "tester"

                case 'Render96ex-tester_rt64alpha':
                    repolink = 'https://github.com/Render96/Render96ex'
                    branchname = "tester_rt64alpha"

                case 'Saturn':
                    repolink = 'https://github.com/Llennpie/Saturn'
                    branchname = 'legacy'

                case 'Saturn: Moon Edition':
                    repolink = 'https://github.com/Llennpie/Saturn'
                    branchname = 'moon'

                case 'SM64Plus (Very Slightly Buggy)':
                    repolink = 'https://github.com/MorsGames/sm64plus'
                    branchname = 'master'

                case 'sm64ex-alo':
                    repolink = 'https://github.com/AloXado320/sm64ex-alo'
                    branchname = 'master'

                case 'sm64ex-coop':
                    repolink = 'https://github.com/djoslin0/sm64ex-coop'
                    branchname = 'coop'

                case other:
                    repolink = 'https://github.com/sm64pc/sm64ex'
                    branchname = 'nightly' 

            window = sg.Window('Downloading', downloading)

            while True: 
                event, values = window.read(1)
                if os.name == 'posix':
                    subprocess.run(f"git clone {repolink} {repofolder} --branch={branchname}", shell=True) # clone the repo
                    subprocess.run(f"cp -r '{modelpackfolder}/actors' '{repofolder}' && cp -r '{modelpackfolder}/src' '{repofolder}'", shell=True) # copy the modelpacks               
                window.close()
                break

            window = sg.Window("Select Baserom", baseromselect)
            # start the build loop
            while True:
                event, values = window.read()
                print(event, values)
                if event == 'Ok': 
                    baseromfolder, romregion = values[0], values[1]
                    window.close()

                    window = sg.Window('build options', buildoptions)
                    while True:
                        event, values = window.read()
                        if event == 'Build':

                            buildflags = values[0]

                            window.close()
                            window = sg.Window('Building', building)
                            while True:
                                event, values = window.read(1)
                                if os.name == 'posix':
                                    subprocess.run(f"cp {baseromfolder} {repofolder}/baserom.{romregion}.z64", shell=True) # copy the baserom 
                                    subprocess.run(f"cd {repofolder} && make {buildflags} VERSION={romregion}", shell=True) # run make
                                    subprocess.run(f"cp -r {texturepack}/gfx {repofolder}/build/{romregion}_pc/res", shell=True) # copy the texture pack

                                    if os.path.exists(f"{repofolder}/build/{romregion}_pc/sm64.{romregion}.f3dex2e") == False:
                                        window = sg.Window('Build failed! :(', buildfailed)
                                        while True:
                                            event, values = window.read()
                                            if event == sg.WIN_CLOSED or event == 'Ok':
                                                exit()
                                with open('builds.txt', 'r') as blist:
                                    builds = blist.read()
                                with open ('builds.txt', 'w') as bwrite:
                                    bwrite.write(repofolder+':'+romregion+'\n'+builds)
                                if os.name == 'posix':
                                    subprocess.run(f"./{repofolder}/build/{romregion}_pc/sm64.{romregion}.f3dex2e", shell=True) # run the executable
                                exit()
                        if event == sg.WIN_CLOSED:
                            exit()
                if event == sg.WIN_CLOSED:
                    exit()
