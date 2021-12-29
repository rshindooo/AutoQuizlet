import time
import keyboard
import pyautogui
import sys
import pathlib
import os
def mains():
    #while True:
        if keyboard.is_pressed("x"):
            print('STOP THE CODE')
            sys.exit(0)
        if keyboard.is_pressed("s"):
            autoSign()
mains()
e_num=0
print(os.getcwd()+"/{}")
currentPath=os.getcwd()+"/{}"
def email_gen(og):
    global e_num
    e_num +=1
    testi="{beforeat}+{e_n}@{afterat}".format(beforeat=og.split('@',1)[0],
                                            e_n=e_num, afterat=og.split('@',1)[1])
    return(testi)
email_gen("test@gmail.com")

def autoSign(sampleE):
    pyautogui.move(50,0)
    for i in ("signup1.png","month.png","monthS.png", "day.png","dayS.png","year.png","yearS.png","email.png","password.png","signup.png"):
        try:
            x,y=pyautogui.locateCenterOnScreen(currentPath.format(i))
        except TypeError:
            print("where")
        else:
            pyautogui.click(currentPath.format(i))
            print(i)
            time.sleep(.05)
            if(i=="signup1.png"):
                time.sleep(.4)
            if(i=="email.png"):
                keyboard.write(email_gen(sampleE))
                time.sleep(.4)
            if(i=="password.png"):
                keyboard.write("12345678a0")
                time.sleep(1)

autoSign("cumballs@gmail.com")

