#!/usr/bin/python3

import PySimpleGUI as sg
import os
from themeconfig import *
from urllib.request import urlopen
sg.theme_background_color(windowBackgroundColor)  
with open('builds.txt', 'r') as blist:
    builds = blist.readlines()


url = "https://raw.githubusercontent.com/faizu396/sm64ll-pi/main/repos.txt"
newstext = urlopen(url).read().decode("utf-8")

news=[
    [sg.Text('Repos', font=(1), background_color=windowBackgroundColor, text_color=textColor)],
    [sg.Multiline(newstext, disabled=True, size=(36, 16), background_color=boxColor, text_color=boxTextColor)]
    ]
options=[
    [sg.Button('Play', size=(10, 2), button_color=("white", playButtonColor),font=(1),disabled=True)],
    [sg.Button('Build', size=(14, 1), button_color=('white', otherButtonColor))]
]
buildselect=[[
    sg.Text('Select your SM64 PC Port build:', background_color=windowBackgroundColor, text_color=textColor),

],
[
    sg.Listbox(
        values=builds, enable_events=True,select_mode='single', size=(40, 20), key="buildlist", bind_return_key = True, background_color=boxColor, text_color=boxTextColor
    )
]
]
   
layout = [
    [
        sg.Column(buildselect, size=(300, 300)),
        sg.VSeperator(),
        sg.Column(options,size=(140, 300)),
        sg.VSeparator(),
        sg.Column(news, size=(300, 300)),
    ]
]
    
window = sg.Window('sm64ll-pi', layout)
while True:
    event, values = window.read()
    if event == 'buildlist':
        buildselected = os.path.join(
            values['buildlist'][0]
        )

        buildselected = buildselected.rstrip("\n")
        if buildselected == "":
            window['Play'].update(disabled=True)
        if not buildselected == "":
            window["Play"].update(disabled=False)
    if event == "Play":
        buildfolder, sep, region = buildselected.partition(':')
        if os.name == 'nt':
            os.system('"'+buildfolder+'\\build\\'+region+'_pc\\sm64.'+region+'.f3dex2e.exe"')
        if os.name == 'posix':
            os.system('cd "'+buildfolder+'/build/'+region+'_pc/" && ./sm64.'+region+'.f3dex2e')
        break
        
    if event == 'Build':
        import builder
        exit() 
    if event == sg.WIN_CLOSED:
        exit()

        
