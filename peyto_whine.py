from config import config
from abilities import abilities
from datetime import datetime
import pyautogui
import pydirectinput
import time
import random
import math
import argparse
from pynput.mouse import Button, Controller

def main():
    print("buying your fucking whine until you stop the script")
    while(True):      
        #get next to the npc dumbass 
        pydirectinput.press("g")
        sleep(500, 1000)
        #make your mouse move click around on the buttons
        mouseMoveTo(x=100, y=200)
        sleep(300, 400)
        pydirectinput.click(button="left")

        mouseMoveTo(x=100, y=200)
        sleep(300, 400)
        pydirectinput.click(button="left")

        #sleep for over a minute and fuggin do it again 
        sleep(60000, 65000)



def mouseMoveTo(**kwargs):
    x = kwargs["x"]
    y = kwargs["y"]
    pydirectinput.moveTo(x=x, y=y)

def sleep(min, max):
    sleepTime = random.randint(int(min), int(max)) / 1000.0
    if sleepTime < 0:
        return
    time.sleep(sleepTime)

if __name__ == "__main__":
    main()