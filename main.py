### PURPOSE
# Simple fun passtime program I made to test out securites of my home network (WPA-2, basic bruteforcing)
# Tested on: Python 3.10.9 64-bit
# Mac M1, Asahi Linux, developed on VSCODE (frontend in browser)
# Goal is to put this onto a Raspberri Pi Zero W once project is finished

### IMPORTS
from password_functions.gen_pas import generatepass
from am_random import random as ran #ran() generates random num from 0-9
from random_check import RCheck as rcheck #rcheck() made for analysis of my random function
from readify import TFormat as tfor, TRead as tread
import os
import subprocess
import time


### VARS
wificommand = subprocess.check_output(["nmcli", "device", "wifi", "list"], universal_newlines=True, bufsize=1) 
output = wificommand
output = output.split('\n')
output = tfor(output)

### MAIN
print(tread(output))
#print(ran())