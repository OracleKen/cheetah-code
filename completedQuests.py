def clearCompletedQuests(): 
    sleep(300,400)
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

    while okButton != None: 
        x, y = okButton
        mouseMoveTo(x=x, y=y)
        sleep(200, 300)
        pydirectinput.click(button="left")
        sleep(200, 300)

        okButton = pyautogui.locateCenterOnScreen(
        "./screenshots/complete.png",
        confidence=0.8)
        sleep(200,300)