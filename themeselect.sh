#!/bin/bash

until [[ ${ANSWER,,} == "default" ]] || [[ ${ANSWER,,} == "dark" ]] || [[ ${ANSWER,,} == "light" ]] || [[ ${ANSWER,,} == "oldschool" ]]; do
	read -p "Choose a theme (default, dark, light, oldschool " ANSWER
done

if [[ ${ANSWER,,} == "default" ]]; then
	echo "playButtonColor = 'green'
otherButtonColor = None
windowBackgroundColor = '#111111'
bottomButtonColor = None
boxColor = None
boxTextColor = None
textColor = None" >| /home/pi/Downloads/sm64ll-pi/src/themeconfig.py

elif [[ ${ANSWER,,} == "dark" ]]; then
	echo "playButtonColor = '#728adb'
otherButtonColor = '#24272b'
windowBackgroundColor = '#33363d'
bottomButtonColor = '#728adb'
boxColor = '#3e424a'
boxTextColor = 'white'
textColor = '#73777e'" >| /home/pi/Downloads/sm64ll-pi/src/themeconfig.py

elif [[ ${ANSWER,,} == "light" ]]; then
	echo "playButtonColor = 'white'
otherButtonColor = 'white'
windowBackgroundColor = 'white'
bottomButtonColor = 'white'
boxColor = 'white'
boxTextColor = 'light gray'
textColor = 'light gray'" >| /home/pi/Downloads/sm64ll-pi/src/themeconfig.py

elif [[ ${ANSWER,,} == "oldschool" ]]; then
	echo "playButtonColor = '#c4c4c4'
otherButtonColor = '#c4c4c4'
windowBackgroundColor = '#c4c4c4'
bottomButtonColor = '#c4c4c4'
boxColor = '#ffffd9'
boxTextColor = 'black'
textColor = 'black'" >| /home/pi/Downloads/sm64ll-pi/src/themeconfig.py

else
	echo "playButtonColor = 'green'
otherButtonColor = None
windowBackgroundColor = '#111111'
bottomButtonColor = None
boxColor = None
boxTextColor = None
textColor = None" >| /home/pi/Downloads/sm64ll-pi/src/themeconfig.py

fi
