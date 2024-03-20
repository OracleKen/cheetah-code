def sendToStronghold():
    pyautogui.press("F2")
    sleep(400,500)
    musicButton = pyautogui.locateCenterOnScreen(
            "./screenshots/home_music.png",
            confidence=0.7)
    if(musicButton != None):
        x,y = musicButton
        mouseMoveTo(x=x,y=y)
        pyautogui.click(button="left")
        playButton = pyautogui.locateCenterOnScreen(
            "./screenshots/play_music.png",
            confidence=0.7)
        if(playButton != None):
            playX, playY = playButton
            mouseMoveTo(x=playX,y=playY)
            pyautogui.click(button="left")

    sleep(8000,10000)
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
            print("back in stronghold")
            break
        sleep(1400, 1600)    
