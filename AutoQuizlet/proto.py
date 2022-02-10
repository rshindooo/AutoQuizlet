import time
import keyboard
import pyautogui
import sys
import random
import string
import pathlib
import os
e_num=0
isToggled = False
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
        for i in ("signup1.png","month.png","monthS.png", "day.png","dayS.png","year.png","yearS.png","email.png","password.png","face.png","signup.png"):
            try:
                x,y=pyautogui.locateCenterOnScreen(currentPath.format(i), confidence=0.7)
            except TypeError:
                print("where")
            else:
                
                time.sleep(.15)
                pyautogui.click(currentPath.format(i))
                print(i)
                if(i=="signup1.png"):
                    time.sleep(2)
                if(i=="email.png"):
                    keyboard.write(email_gen(sampleE))
                    time.sleep(.4)
                if(i=="password.png"):
                    keyboard.write("asfa2!!!3*6")
                    time.sleep(1)
                    keyboard.write("u")
                    time.sleep(.5)
def mains():
    letters = string.ascii_lowercase
    rGen= ( ''.join(random.choice(letters) for i in range(10)) )
    while True:
        if keyboard.is_pressed("x"):
            print('STOP THE CODE')
            sys.exit(0)
        if keyboard.is_pressed("s"):
            autoSign(rGen+"@gmail.com")



print("TO USE THIS BOT RUN IT, THEN PRESS S TO MAKE 1 ACCOUNT. PRESS X TO EXIT AFTER BOT HAS FINISHED MAKING CODE. TO DISABLE BOTMAKING PRESS Q")
mains()
