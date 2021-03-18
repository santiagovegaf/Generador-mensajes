import pyautogui
import time
time.sleep(10)
f = open("script_bee_movie", "r")
for palabra in f:
    pyautogui.typewrite(palabra)
