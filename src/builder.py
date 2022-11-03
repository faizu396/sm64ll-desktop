#!/usr/bin/python3

from gettext import install
import PySimpleGUI as sg
import os
from themeconfig import *
import subprocess
import shlex
sg.theme_background_color(windowBackgroundColor)  

msys2depends = False
buildfailed = [
    [sg.Text('Build failed, try to build again', text_color=textColor, background_color=windowBackgroundColor), sg.Button('Ok', button_color=('white', bottomButtonColor))]
]
branchselect = [
    [sg.Text("Select a Repository. (If you do not select a valid repo, the builder will automaticaly default to sm64ex-nightly).", text_color=textColor, background_color=windowBackgroundColor)],
    [sg.Combo(['sm64ex-nightly','sm64ex-master','sm64ex-coop','','Render96ex-master','Render96ex-tester','Render96ex-tester_rt64alpha','','Saturn','Saturn: Moon Edition','','SM64Plus (Very Slightly Buggy)', '','sm64ex-alo',''], background_color=boxColor,text_color=boxTextColor),],
    [sg.Text("Add a name for the repo folder", text_color=textColor, background_color=windowBackgroundColor)],
    [sg.In(background_color=boxColor, text_color=boxTextColor)],
    [sg.Text('modelpack folder (optional)', text_color=textColor, background_color=windowBackgroundColor)],
    [sg.In(background_color=boxColor, text_color=boxTextColor),sg.FolderBrowse(button_color=("white",otherButtonColor))],
    [sg.Text('Texture pack folder (optional)', text_color=textColor, background_color=windowBackgroundColor)],
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

msys2folderselect=[
    [sg.Text('Select your msys2 folder', text_color=textColor, background_color=windowBackgroundColor)],
    [
        sg.In(background_color=windowBackgroundColor, text_color=boxTextColor),
        sg.FolderBrowse(button_color=("white", otherButtonColor))
    ],[sg.Checkbox(text='install msys2 dependencies (check if you are building for the first time)', key='msys2depends', text_color=textColor)],
    [sg.Button('Ok',button_color=("white", bottomButtonColor))]
]
downloading = [[sg.Text('Downloading the repo... (Do not close this window if it says "not responding")', text_color=textColor, background_color=windowBackgroundColor)]]
building = [[sg.Text('Building... (Do not close this window if it says "not responding")', text_color=textColor, background_color=windowBackgroundColor)]]
if os.name == "nt":
    window = sg.Window('Windows detected', msys2folderselect)
    while True:
        event,  values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        if event == "Ok":
            msys2folder = values[0].replace('/', '\\')
            window.close()
            msys2depends = values['msys2depends']
            break
            





def run(command):
    if os.name == "nt":
        return subprocess.run(
            [
                msys2folder+"/usr/bin/bash.exe",
                "--login",
                "-c",
                command,
            ],
            encoding="utf-8",
            env={**os.environ, "MSYSTEM": "MINGW64", "CHERE_INVOKING": "yes"},
        ).returncode
    else:
        return subprocess.run(
            command,
            shell=True,
        ).returncode
if os.name == 'nt' and msys2depends == True:
    run('pacman -S git --noconfirm')
    run('pacman -S make --noconfirm')
    run('pacman -S python3 --noconfirm')
    run('pacman -S mingw-w64-x86_64-gcc --noconfirm')
    run('pacman -S mingw-w64-x86_64-glew --noconfirm')
    run('pacman -S mingw-w64-x86_64-SDL2 --noconfirm')

# Create the window
window = sg.Window("SM64 Linux Builder", branchselect)


# Create an event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        exit()
    if event == "Ok":
        repolink=values[0]
        branchname=values[0]
        repofolder=values[1]
        texturepack=values[3]
        modelpackfolder=values[2]
        window.close()


        if repolink == 'sm64ex-nightly':
            repolink = 'https://github.com/sm64pc/sm64ex'
            branchname = 'nightly'

        elif repolink == 'sm64ex-master':
            repolink = 'https://github.com/sm64pc/sm64ex'
            branchname = 'master'

        elif repolink == 'Render96ex-master':
            repolink = 'https://github.com/Render96/Render96ex/'
            branchname = 'master'

        elif repolink == 'Render96ex-tester':
            repolink = 'https://github.com/Render96/Render96ex'
            branchname = "tester"

        elif repolink == 'Render96ex-tester_rt64alpha':
            repolink = 'https://github.com/Render96/Render96ex'
            branchname = "tester_rt64alpha"

        elif repolink == 'Saturn':
            repolink = 'https://github.com/Llennpie/Saturn'
            branchname = 'legacy'

        elif repolink == 'Saturn: Moon Edition':
            repolink = 'https://github.com/Llennpie/Saturn'
            branchname = 'moon'

        elif repolink == 'SM64Plus (Very Slightly Buggy)':
            repolink = 'https://github.com/MorsGames/sm64plus'
            branchname = 'master'

        elif repolink == 'sm64ex-alo':
            repolink = 'https://github.com/AloXado320/sm64ex-alo'
            branchname = 'master'

        elif repolink == 'sm64ex-coop':
            repolink = 'https://github.com/djoslin0/sm64ex-coop'
            branchname = 'coop'

        else:
            repolink = 'https://github.com/sm64pc/sm64ex'
            branchname = 'nightly'


        window = sg.Window('Downloading', downloading)
        
        
        while True:
            event, values = window.read(1)
            if os.name == 'posix':
                os.system('git clone "'+repolink+'" "'+repofolder+'" --branch='+branchname)
                os.system('cp -r "'+modelpackfolder+'/actors" "'+repofolder+'" && cp -r "'+modelpackfolder+'/src" "'+repofolder+'"')
            if os.name == 'nt':
                run('git clone "'+repolink+'" "'+repofolder+'" --branch='+branchname)
                run('cp -r "'+modelpackfolder+'/actors" "'+repofolder+'" && cp -r "'+modelpackfolder+'/src" "'+repofolder+'"')
            window.close()
            break

        


        window = sg.Window("Select Baserom", baseromselect)
        
        while True:
            event, values = window.read()
            if event == 'Ok': 
                baseromfolder=values[0]
                romregion=values[1]
                
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
                                os.system('cp "'+baseromfolder+'" "'+repofolder+'/baserom.'+romregion+'.z64"')
                                os.system('cd "'+repofolder+'" && make '+buildflags+' VERSION='+romregion)
                                os.system('cp -r "'+texturepack+'/gfx" "'+repofolder+'/build/'+romregion+'_pc/res"')
                            if os.name == 'nt':
                                run('dir')
                                run('cp "'+baseromfolder+'" "'+repofolder+'/baserom.'+romregion+'.z64"')
                                run('cd "'+repofolder+'" && make '+buildflags)
                                run('cp -r "'+texturepack+'/gfx" "'+repofolder+'/build/'+romregion+'_pc/res"')

                            if os.name == 'nt':
                                if os.path.exists(repofolder+'/build/'+romregion+'_pc/sm64.'+romregion+'.f3dex2e.exe') == False:
                                    window = sg.Window('Build failed! :(', buildfailed)
                                    while True:
                                        event, values = window.read()
                                        if event == sg.WIN_CLOSED or event == 'Ok':
                                            exit()
                            if os.name == 'posix':
                                if os.path.exists(repofolder+'/build/'+romregion+'_pc/sm64.'+romregion+'.f3dex2e') == False:
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
                                os.system('."/'+repofolder+'/build/'+romregion+'_pc/sm64.'+romregion+'.f3dex2e"')
                            if os.name == 'nt':
                                os.system('"'+repofolder+'\\build\\'+romregion+'_pc\\sm64.'+romregion+'.f3dex2e.exe"')

                            exit()
                        
                    if event == sg.WIN_CLOSED:
                        exit()
            if event == sg.WIN_CLOSED:
                exit()



    



    
