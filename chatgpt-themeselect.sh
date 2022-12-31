#!/bin/bash

read -p "Choose a theme (default, dark, light, oldschool, terminal)" 
ANSWER

theme_config_map = {
    "default": {
        "playButtonColor": "green",
        "otherButtonColor": None,
        "windowBackgroundColor": "#111111",
        "bottomButtonColor": None,
        "boxColor": None,
        "boxTextColor": None,
        "textColor": None,
    },
    "dark": {
        "playButtonColor": "#728adb",
        "otherButtonColor": "#24272b",
        "windowBackgroundColor": "#33363d",
        "bottomButtonColor": "#728adb",
        "boxColor": "#3e424a",
        "boxTextColor": "white",
        "textColor": "#73777e",
    },
    "light": {
        "playButtonColor": "white",
        "otherButtonColor": "white",
        "windowBackgroundColor": "white",
        "bottomButtonColor": "white",
        "boxColor": "white",
        "boxTextColor": "light gray",
        "textColor": "light gray",
    },
    "oldschool": {
        "playButtonColor": "#c4c4c4",
        "otherButtonColor": "#c4c4c4",
        "windowBackgroundColor": "#c4c4c4",
        "bottomButtonColor": "#c4c4c4",
        "boxColor": "#ffffd9",
        "boxTextColor": "black",
        "textColor": "black",
    },
    "terminal": {
        "playButtonColor": "black",
        "otherButtonColor": "black",
        "windowBackgroundColor": "black",
        "bottomButtonColor": "black",
        "boxColor": "black",
        "boxTextColor": "#00ff00",
        "textColor": "#00ff00",
    },
}

theme_config = theme_config_map.get(ANSWER.lower(), 
theme_config_map["default"])

with open("/home/pi/Downloads/sm64ll-pi/src/themeconfig.py", "w") as f:
    f.write(f"{' '.join(f'{k} = {v!r}' for k, v in 
theme_config.items())}")

