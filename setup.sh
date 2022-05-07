#!/bin/bash

sudo apt-get install -y python3 python3-pip python3-tk libsdl2-dev git gcc-mips-linux-gnu
pip3 install pysimplegui
sudo mv ~/Downloads/sm64ll-pi/sm64launcher.desktop ~/.local/share/applications
