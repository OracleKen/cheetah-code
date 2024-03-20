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
    mouseMoveTo(x=config["screenCenterX"], y=config["screenCenterY"])
    sleep(200, 300)
    pydirectinput.click(button=config["move"])

    sleep(500, 1000)
    if(config["enableUnaTasks"]):
        doUnaTasks()

def doUnaTasks(): 
    questsAccepted = acceptUnaTasks()

    if questsAccepted == False: 
        print("no quests to accept")
        return

    leapUnas = config["characters"][states["currentCharacter"]].get("leapUnas")
    if(leapUnas != None):
        #print("doing leap unas")
        #print(leapUnas)
        doLeapUnas(leapUnas)
    
    lopangUnas = config["characters"][states["currentCharacter"]].get("lopang")
    if(lopangUnas == True):
        doLopangUnas()

def doLopangUnas(): 
    return True

def doLeapUnas(leapUnas): 
    unaComplete = True
    for una in leapUnas: 
        unaLocation = una.get("leap")
        unaBifrost = una.get("bifrost")
        if(unaLocation == "hestera"): 
            unaComplete = unaComplete and doHesteraLeapUna(unaBifrost)
        elif(unaLocation == "voldis"):
            unaComplete = unaComplete and doVoldisLeapUna(unaBifrost)
        elif(unaLocation == "ghost"): 
            unaComplete = unaComplete and doGhostLeapUna(unaBifrost)
        elif(unaLocation == "moko"):
            unaComplete = unaComplete and doMokoLeapUna(unaBifrost)
        else: 
            print("Unable to determine correct Una leapstone location, aborting una processing")
            unaComplete = False
        
        if(unaComplete == False): 
            return False
    return unaComplete

def doHesteraLeapUna(bifrostPosition):
    bifrostAvailable = bifrostGoTo(bifrostPosition)
    if bifrostAvailable == False:
        return False

    sleep(500, 600)
    if gameCrashCheck():
        return False
    if offlineCheck():
        return False
    sleep(1500, 1600)
    
    pydirectinput.press("enter")
    sleep(300, 300)
    pydirectinput.press("/")
    sleep(100, 200)
    pydirectinput.press("s")
    sleep(100, 200)
    pydirectinput.press("i")
    sleep(100, 200)
    pydirectinput.press("t")
    sleep(100, 200)
    pydirectinput.press("enter")
    
    sleep(135000, 145000)
    
    mouseMoveTo(x=1700 , y=430)
    sleep(1000, 1200)
    pydirectinput.click(button="left")
    sleep(500, 600)
    pydirectinput.click(button="left")
    sleep(1000, 1200)
    
    okButton = pyautogui.locateCenterOnScreen(
        "./screenshots/complete.png",
        confidence=0.8
    )
    if okButton != None:
        x, y = okButton
        mouseMoveTo(x=x, y=y)
        sleep(200, 300)
        pydirectinput.click(button="left")
        sleep(100, 200)

    if gameCrashCheck():
        return False
    if offlineCheck():
        return False
    return True

def doVoldisLeapUna(bifrostPosition):
    bifrostAvailable = bifrostGoTo(bifrostPosition)
    if bifrostAvailable == False:
        return False
    
    #re-try max 20 times 
    retryCount = 0 
    maxRetries = 20
    npcFound = None
    while retryCount < maxRetries: 
        #print("pressing the g")
        pydirectinput.press("g")
        sleep(500, 600)

        closeButton = pyautogui.locateCenterOnScreen(
        "./screenshots/x.png",
        confidence=0.8)

        if closeButton != None: 
            #print("close button found")
            pydirectinput.press("esc")   

        npcFound = pyautogui.locateCenterOnScreen(
        "./screenshots/voldis_complete.png",
        confidence=0.65)

        if(npcFound != None): 
            break 

        retryCount = retryCount + 1
        sleep(5000, 5500)

    if(npcFound != None): 
        #print("npc found")
        x, y = npcFound
        print("x: {}, y: {}".format(x, y))
        mouseMoveTo(x=x, y=(y+200))
        sleep(200,300)
        pydirectinput.click(button=config["move"])
        sleep(2000,2200)
        pydirectinput.press("g")
        sleep(1000,1200)
        pydirectinput.keyDown("shift")
        sleep(100,200)
        pydirectinput.press("g")
        sleep(100,200)
        pydirectinput.keyUp("shift")
        sleep(300, 400)
        okButton = pyautogui.locateCenterOnScreen(
        "./screenshots/complete.png",
        confidence=0.8)
        if okButton != None:
            x, y = okButton
            mouseMoveTo(x=x, y=y)
            sleep(200, 300)
            pydirectinput.click(button="left")
            sleep(100, 200)
        return True
    
    if gameCrashCheck():
        return False
    if offlineCheck():
        return False
    return True

def doMokoLeapUna(bifrostPosition): 
    # bifrostAvailable = bifrostGoTo(bifrostPosition)
    # if bifrostAvailable == False:
    #     return False
    
    sleep(500, 600)
    if gameCrashCheck():
        return False
    if offlineCheck():
        return False
    sleep(1500, 1600)    

    pydirectinput.press("g")
    sleep(1000,1200)
    pydirectinput.keyDown("shift")
    sleep(100,200)
    pydirectinput.press("g")
    sleep(100,200)
    pydirectinput.keyUp("shift")
    sleep(500, 600)
    pydirectinput.press("g")
    sleep(500,1000)

    mouseMoveTo(x=540, y=760)
    sleep(100,200)
    pydirectinput.click(button=config["move"])
    sleep(2500, 3000)

    pydirectinput.press("g")
    sleep(3500,4000)

    mouseMoveTo(x=1120, y=820)
    sleep(100,200)
    pydirectinput.click(button=config["move"])
    sleep(2500, 3000)

    pydirectinput.press("g")
    sleep(3500,4000)

    mouseMoveTo(x=1160, y=730)
    sleep(100,200)
    pydirectinput.click(button=config["move"])
    sleep(2500, 3000)

    pydirectinput.press("g")
    sleep(3500,4000)

    mouseMoveTo(x=950, y=180)
    sleep(100,200)
    pydirectinput.click(button=config["move"])
    sleep(2500, 3000)

    mouseMoveTo(x=950, y=350)
    sleep(100,200)
    pydirectinput.click(button=config["move"])
    sleep(1000, 1200)

    pydirectinput.press("g")
    sleep(1000,1200)
    pydirectinput.keyDown("shift")
    sleep(100,200)
    pydirectinput.press("g")
    sleep(100,200)
    pydirectinput.keyUp("shift")
    sleep(500, 600)
    pydirectinput.press("g")
    sleep(500,1000)
 
    return True

def doGhostLeapUna(bifrostPosition):
    bifrostAvailable = bifrostGoTo(bifrostPosition)

    if bifrostAvailable == False:
        return False
    
    envelope = pyautogui.locateCenterOnScreen(
        "./screenshots/envelope.png",
        confidence=0.8
    )

    if envelope != None: 
        pydirectinput.press("F5")
        sleep(500, 600)

    #in case there's some stupid guide quest that's hostaging the F5 key...
    envelope = pyautogui.locateCenterOnScreen(
        "./screenshots/envelope.png",
        confidence=0.8
    )
    if envelope != None: 
        pydirectinput.press("F6")
        sleep(500, 600)

    mouseMoveTo(x=1700 , y=430)
    sleep(1000, 1200)
    pydirectinput.click(button="left")
    sleep(500, 600)
    pydirectinput.click(button="left")
    sleep(1000, 1200)

    okButton = pyautogui.locateCenterOnScreen(
        "./screenshots/complete.png",
        confidence=0.8
    )
    if okButton != None:
        x, y = okButton
        mouseMoveTo(x=x, y=y)
        sleep(200, 300)
        pydirectinput.click(button="left")
        sleep(100, 200)
    if gameCrashCheck():
        return False
    if offlineCheck():
        return False
     
    return True
 

def acceptUnaTasks():
    mouseMoveTo(x=1730, y=910) 
    sleep(200,300)
    pydirectinput.click(button="left")
    sleep(200,300)
    mouseMoveTo(x=1670,y=840)
    pydirectinput.click(button="left")
    sleep(500,600)

    mouseMoveTo(x=564, y=313)
    sleep(200, 300)
    pydirectinput.click(button="left")
    sleep(300, 400)

    mouseMoveTo(x=528, y=404)
    sleep(200, 300)
    pydirectinput.click(button="left")
    sleep(500, 600)

    dailyCompleted = pyautogui.locateCenterOnScreen(
        "./screenshots/dailyCompleted.png",
        confidence=0.75,
        region=(1143, 339, 110, 400),
    )

    if dailyCompleted != None:
        mouseMoveTo(x=1633, y=222)
        sleep(200, 300)
        pydirectinput.click(button="left")
        sleep(200, 300)
        return False

    mouseMoveTo(x=1206, y=398)
    sleep(200, 300)
    pydirectinput.click(button="left")
    sleep(200, 300)

    mouseMoveTo(x=1206, y=455)
    sleep(200, 300)
    pydirectinput.click(button="left")
    sleep(200, 300)

    mouseMoveTo(x=1206, y=515)
    sleep(200, 300)
    pydirectinput.click(button="left")
    sleep(200, 300)

    mouseMoveTo(x=1633, y=222)
    sleep(200, 300)
    pydirectinput.click(button="left")
    sleep(200, 300)
    # sleep(300, 400)
    # pydirectinput.press("esc")
    # sleep(300, 500)

def sleep(min, max):
    sleepTime = random.randint(int(min), int(max)) / 1000.0
    if sleepTime < 0:
        return
    time.sleep(sleepTime)

def mouseMoveTo(**kwargs):
    x = kwargs["x"]
    y = kwargs["y"]
    pydirectinput.moveTo(x=x, y=y)

def gameCrashCheck():
    return False

def offlineCheck(): 
    return False

def bifrostGoTo(option):
    print("bifrost to: {}".format(option))
    bifrostXY = [
        [1343, 425],
        [1343, 490],
        [1343, 550],
        [1343, 650],
        [1343, 710],
    ]
    pydirectinput.keyDown("alt")
    sleep(300, 400)
    pydirectinput.press("w")
    sleep(300, 400)
    pydirectinput.keyUp("alt")
    sleep(2500, 2600)

    mouseMoveTo(x=bifrostXY[option][0], y=bifrostXY[option][1])
    sleep(500, 600)
    pydirectinput.click(button="left")
    sleep(200, 300)
    pydirectinput.click(button="left")
    sleep(500, 600)

    # ok
    mouseMoveTo(x=918, y=617)
    sleep(1500, 1600)
    pydirectinput.click(button="left")
    sleep(500, 600)
    pydirectinput.click(button="left")
    sleep(500, 600)
    pydirectinput.click(button="left")

    # sleep(3000, 4000)
    # pydirectinput.press("esc")
    # sleep(200, 300)
    # pydirectinput.press("esc")

    # wait until loaded
    while True:
        if gameCrashCheck():
            return
        if offlineCheck():
            return
        sleep(1000, 1200)
        inTown = pyautogui.locateCenterOnScreen(
            "./screenshots/inTown.png",
            confidence=0.75,
            region=(1870, 133, 25, 30),
        )
        if inTown != None:
            print("city loaded")
            break
        sleep(1400, 1600)
    sleep(1500, 2500)
    if gameCrashCheck():
        return
    if offlineCheck():
        return
    sleep(2000, 3000)


if __name__ == "__main__":
    states = newStates.copy()
    main()