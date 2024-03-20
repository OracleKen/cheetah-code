import time
import pyautogui
import pydirectinput
import random
from pynput.mouse import Button, Controller

mouse = Controller()

def main():  
    pydirectinput.press("esc")
    sleep(500, 600)
    pydirectinput.press("esc")  
    walkLopang()

# def walkLopang():
#     pydirectinput.PAUSE = 0.1
#     #sleep(500, 600)
#     #spamG(700)

#     walkWithAlt(450, 430, 1800)
    # walkWithAlt(407, 679, 1600)
    # walkWithAlt(584, 258, 1300)
    # walkWithAlt(1043, 240, 1500)
    # walkWithAlt(1339, 246, 1600)
    # walkWithAlt(1223, 406, 1100)
    # walkWithAlt(1223, 406, 1100)
    # walkWithAlt(1263, 404, 1100)
    # console = pyautogui.locateCenterOnScreen(
    #     "./screenshots/lopang_console.png",
    #     confidence=0.75)
    
    # if(console != None):
    #     x,y = console
    #     mouseMoveTo(x=x,y=(y+160))
    #     pydirectinput.click(button="right")
    #     sleep(500,700)
    # spamG(700)
    # # nowTime = int(time.time_ns() / 1000000)
    # # lopangDebug = pyautogui.screenshot()
    # # lopangDebug.save("./debug/lopangDebug_" + str(nowTime) + ".png")
    # walkWithAlt(496, 750, 1100)
    # walkWithAlt(496, 750, 1100)
    # walkWithAlt(496, 750, 1100)
    # walkWithAlt(653, 737, 1100)
    # walkWithAlt(653, 737, 1100)
    # walkWithAlt(674, 264, 1100)
    # walkWithAlt(573, 301, 1500)
    # walkWithAlt(820, 240, 1100)
    # console = pyautogui.locateCenterOnScreen(
    #     "./screenshots/lopang_console.png",
    #     confidence=0.75)
    
    # if(console != None):
    #     x,y = console
    #     mouseMoveTo(x=x,y=(y+160))
    #     pydirectinput.click(button="right")
    #     sleep(500,700)
    # spamG(700)
    # # nowTime = int(time.time_ns() / 1000000)
    # # lopangDebug = pyautogui.screenshot()
    # # lopangDebug.save("./debug/lopangDebug_" + str(nowTime) + ".png")
    # sleep(500, 600)
    # pydirectinput.PAUSE = 0.05
    # sleep(500, 600)



# def doLopangUnas():
#     sleep(500, 600)
#     if gameCrashCheck():
#         return False
#     if offlineCheck():
#         return False
#     sleep(1500, 1600)

#     # goto lopang island
#     bifrostAvailable = bifrostGoTo(0)
#     if bifrostAvailable == False:
#         return
#     if gameCrashCheck():
#         return
#     if offlineCheck():
#         return
#     sleep(1000, 1200)
#     walkLopang()
#     sleep(500, 600)
#     bifrostGoTo(1)
#     if gameCrashCheck():
#         return
#     if offlineCheck():
#         return
#     spamG(2000)
#     sleep(500, 600)
#     bifrostGoTo(3)
#     if gameCrashCheck():
#         return
#     if offlineCheck():
#         return
#     spamG(2000)
#     sleep(500, 600)
#     bifrostGoTo(4)
#     if gameCrashCheck():
#         return
#     if offlineCheck():
#         return
#     spamG(2000)


def mouseMoveTo(**kwargs):
    x = kwargs["x"]
    y = kwargs["y"]
    pydirectinput.moveTo(x=x, y=y)


def spamG(milliseconds):
    timeCount = milliseconds / 100
    while timeCount != 0:
        pydirectinput.press("g")
        sleep(90, 120)
        timeCount = timeCount - 1

def sleep(min, max):
    sleepTime = random.randint(int(min), int(max)) / 1000.0
    if sleepTime < 0:
        return
    time.sleep(sleepTime)

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
    sleep(1000, 1200)

    mouseMoveTo(x=bifrostXY[option][0], y=bifrostXY[option][1])
    sleep(500, 600)
    pydirectinput.click(button="left")
    sleep(200, 300)
    pydirectinput.click(button="left")
    sleep(600, 800)

    # potentially unnecessary check
    if checkBlueCrystal():
        pydirectinput.press("esc")
        sleep(1500, 1600)
        pydirectinput.press("esc")
        sleep(1500, 1600)
        return False
    else:
        # ok
        mouseMoveTo(x=918, y=617)
        sleep(500, 600)
        pydirectinput.click(button="left")
        sleep(200, 300)
        pydirectinput.click(button="left")
        sleep(200, 300)

    sleep(5000, 6000)

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
        sleep(500, 600)
    sleep(500, 800)
    if gameCrashCheck():
        return
    if offlineCheck():
        return
    sleep(500, 1000)

def checkBlueCrystal(): 
    return False


def gameCrashCheck(): 
    return False

def offlineCheck(): 
    return False

def walkWithAlt(lopangX, lopangY, milliseconds):
    lopangX = lopangX
    lopangY = lopangY
    # pydirectinput.keyDown("alt")
    mouseMoveTo(x=lopangX, y=lopangY)
    sleep(100, 100)
    pydirectinput.click(button="right")
    sleep(milliseconds, milliseconds)


def walkLopang(): 
    pydirectinput.PAUSE = 0.1
    sleep(500, 600)
    spamG(700)

    walkWithAlt(450, 430, 1800)   
    walkWithAlt(250, 850, 2000)
    walkWithAlt(620, 185, 1300)
    walkWithAlt(1100, 240, 1800)
    walkWithAlt(1430, 240, 2000)
    walkWithAlt(1500, 285, 2000)
    spamG(700)

    walkWithAlt(550, 700, 1200)
    walkWithAlt(550, 700, 1200)
    walkWithAlt(600, 800, 1200)
    walkWithAlt(675, 700, 1200)
    walkWithAlt(600, 650, 1200)
    walkWithAlt(700, 200, 1500)
    walkWithAlt(450, 200, 2500)
    walkWithAlt(1025, 400, 1000)
    spamG(700)
    
    sleep(500, 600)
    pydirectinput.PAUSE = 0.05
    sleep(500, 600)
    

if __name__ == "__main__":
    main()