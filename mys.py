from pyautogui import moveTo as move
import random

while True:
    x = random.randint(100,500)
    y = random.randint(100,500)
    print(x,y)
    move(x,y, duration=0.25)
    move(x,y, duration=0.25)
    move(x,y, duration=0.25)
    move(x,y, duration=0.25)

