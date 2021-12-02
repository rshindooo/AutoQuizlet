import time
import pynput.mouse
import keyboard
from pynput.mouse import Button, Controller
from pynput import keyboard
import sys
def exit():
    while True:
        if keyboard.is_pressed("x"):
            print('es')
            sys.exit()
mouse= Controller()
mouse.position=(0,10)

timex=10
while timex>0:
    exit()
    time.sleep(1)
    timex-=1
"""

xxxxxxxx"""
