import pyautogui as pg
import keyboard

while True:
    if keyboard.pressed('p'):
        print(pg.position())
        break

