from config import config
from abilities import abilities
import pyautogui
import pydirectinput
import time
import random
import math
import argparse
from pynput.mouse import Button, Controller

pydirectinput.PAUSE = 0.05
newStates = {
    "status": "inCity",
    "abilities": [],
    "abilityScreenshots": [],
    "bossBarLocated": False,
    "clearCount": 0,
    "fullClearCount": 0,
    "moveToX": config["screenCenterX"],
    "moveToY": config["screenCenterY"],
    "moveTime": 0,
    "botStartTime": None,
    "instanceStartTime": None,
    "deathCount": 0,
    "healthPotCount": 0,
    "timeoutCount": 0,
    "goldPortalCount": 0,
    "purplePortalCount": 0,
    "badRunCount": 0,
    "gameRestartCount": 0,
    "gameCrashCount": 0,
    "gameOfflineCount": 0,
    "minTime": config["timeLimit"],
    "maxTime": -1,
    "floor3Mode": False,
    "multiCharacterMode": False,
    "currentCharacter": config["mainCharacter"],
    "multiCharacterModeState": [],
}

mouse = Controller()

def main():
    print("swapping to char 5")
    switchToCharacter(5)

def switchToCharacter(index):
    sleep(1500, 1600)
    print("switching to {}".format(index))
    pydirectinput.press("esc")
    sleep(1000, 1200)
    mouseMoveTo(x=config["charSwitchX"], y=config["charSwitchY"])
    sleep(1000, 1200)
    pydirectinput.click(button="left")
    sleep(200, 300)
    pydirectinput.click(button="left")
    sleep(1000, 1200)
    pydirectinput.click(button="left")
    sleep(200, 300)
    pydirectinput.click(button="left")
    sleep(1000, 1200)
    realIndex = config["characters"][index]["index"]

    pyautogui.moveTo(x=config["charSwitchUpArrowX"], y=config["charSwitchUpArrowY"])
    sleep(300, 400)
    pydirectinput.click(button="left")
    sleep(300, 400)
    pydirectinput.click(button="left")
    sleep(300, 400)
    pydirectinput.click(button="left")
    sleep(300, 400)
    pydirectinput.click(button="left")
    sleep(1000, 1200)
 
    if realIndex >= 9 and realIndex < 12:       
        pyautogui.moveTo(x=config["charSwitchDownArrowX"], y=config["charSwitchDownArrowY"])
        sleep(300, 400)
        pydirectinput.click(button="left")
    elif realIndex >= 12 and realIndex < 15:
        pyautogui.moveTo(x=config["charSwitchDownArrowX"], y=config["charSwitchDownArrowY"])
        sleep(300, 400)
        pydirectinput.click(button="left")
        sleep(300, 400)
        pydirectinput.click(button="left")
    elif realIndex >= 15 and realIndex < 18:
        pyautogui.moveTo(x=config["charSwitchDownArrowX"], y=config["charSwitchDownArrowY"])
        sleep(300, 400)
        pydirectinput.click(button="left")
        sleep(300, 400)
        pydirectinput.click(button="left") 
        sleep(300, 400)
        pydirectinput.click(button="left")   
    elif realIndex >= 18 and realIndex < 21: 
        pyautogui.moveTo(x=config["charSwitchDownArrowX"], y=config["charSwitchDownArrowY"])
        sleep(300, 400)
        pydirectinput.click(button="left")
        sleep(300, 400)
        pydirectinput.click(button="left") 
        sleep(300, 400)
        pydirectinput.click(button="left")      
        sleep(300, 400)
        pydirectinput.click(button="left")  
    elif realIndex >= 21 and realIndex < 24: 
        pyautogui.moveTo(x=config["charSwitchDownArrowX"], y=config["charSwitchDownArrowY"])
        sleep(300, 400)
        pydirectinput.click(button="left")
        sleep(300, 400)
        pydirectinput.click(button="left") 
        sleep(300, 400)
        pydirectinput.click(button="left")      
        sleep(300, 400)
        pydirectinput.click(button="left") 
        sleep(300, 400)
        pydirectinput.click(button="left")          

    sleep(300, 400)
    pyautogui.moveTo(x=config["charPositions"][realIndex][0], y=config["charPositions"][realIndex][1])
    sleep(1000, 1100)
    pyautogui.click(button="left")
    sleep(300, 400)
    pyautogui.click(button="left")
    sleep(1000, 1100)    

    mouseMoveTo(x=config["charSelectConnectX"], y=config["charSelectConnectY"])
    sleep(1500, 1600)
    pydirectinput.click(button="left")
    sleep(300, 400)
    pydirectinput.click(button="left")
    sleep(1500, 1600)
    pydirectinput.click(button="left")
    sleep(300, 400)
    pydirectinput.click(button="left")
    sleep(300, 400)

    pydirectinput.click(button="left")
    sleep(1000, 1000)

    mouseMoveTo(x=config["charSelectOkX"], y=config["charSelectOkY"])
    sleep(1500, 1600)
    pydirectinput.click(button="left")
    sleep(300, 400)
    pydirectinput.click(button="left")
    sleep(1500, 1600)
    pydirectinput.click(button="left")
    sleep(300, 400)
    pydirectinput.click(button="left")
    sleep(1500, 1600)

    states["currentCharacter"] = index
    states["abilityScreenshots"] = []
    sleep(10000, 12000)
    if config["GFN"] == True:
        sleep(8000, 9000)

def mouseMoveTo(**kwargs):
    x = kwargs["x"]
    y = kwargs["y"]
    pydirectinput.moveTo(x=x, y=y)

def sleep(min, max):
    sleepTime = random.randint(min, max) / 1000.0
    if sleepTime < 0:
        return
    time.sleep(sleepTime)

if __name__ == "__main__":
    states = newStates.copy()
    main()