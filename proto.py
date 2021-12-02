
import time
import pynput.mouse
import keyboard
from pynput.mouse import Button, Controller
import sys
e_num=-1
def mains():
    #while True:
        if keyboard.is_pressed("x"):
            print('STOP THE CODE')
            sys.exit(0)
        if keyboard.is_pressed("s"):
            pass
            #run def
mains()
mouse= Controller()
mouse.position=(0,10)

def email_gen(og):
    global e_num +=1
    keyboard.write("cum")
#    keyboard.write(og.split('@',1)[0], "+",e_num,"og.split('@',1)[1])
    return 0
"""
x      x

xxxxxxxx"""

email_gen("test@gmail.com")
