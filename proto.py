import time
import pynput.mouse
import keyboard
import pyautogui
from pynput.mouse import Button, Controller
import sys
def mains():
    #while True:
        if keyboard.is_pressed("x"):
            print('STOP THE CODE')
            sys.exit(0)
        if keyboard.is_pressed("s"):
            autoSign()
mains()
mouse= Controller()
mouse.position=(0,10)
e_num=0
x="C:/Python Stuff/{}"
def email_gen(og):
    global e_num
    e_num +=1
    testi="{beforeat}+{e_n}@{afterat}".format(beforeat=og.split('@',1)[0],
                                            e_n=e_num, afterat=og.split('@',1)[1])
    print(testi)
    return(0)
"""
x      xxxxx
xxxxxxxx"""
email_gen("test@gmail.com")
email_gen("test@gmail.com")

def autoSign():
    #pyautogui.click(x.format("signup.png"))
    #time.sleep(1)
    pyautogui.click(x.format("day.png"))

autoSign()
