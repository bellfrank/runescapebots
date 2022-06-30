from pickletools import pyunicode
import pyautogui
import time
from time import sleep


def bank():
    pyautogui.doubleClick(1276, 179)
    sleep(12)
    pyautogui.click(762, 512)
    sleep(1)
    pyautogui.click(876, 509)
    sleep(1)
    pyautogui.click(1383, 61)
    sleep(11)
    pyautogui.click(944, 435)
    sleep(3)

pyautogui.doubleClick(764, 454)
while True:
    while (pyautogui.locateOnScreen('notification2.png')):
        print("cutting right")
        pyautogui.click(764, 454)
        sleep(4)
    
    pyautogui.moveTo(449, 420)
    while (pyautogui.locateOnScreen('notification2.png') == None):
        print("waiting to cut left")
        pass

    pyautogui.click(449, 420)
    sleep(1)
    pyautogui.moveTo(661, 461)
    sleep(1)
    while(pyautogui.locateOnScreen('notification2.png') != None):
        print("waiting till tree is gone")
        if (pyautogui.locateCenterOnScreen('fullbag2.png')):
            bank()
        pass
    
    pyautogui.moveTo(1004, 504)
    sleep(1)
    while (pyautogui.locateOnScreen('notification2.png') == None):
        print("waiting till right tree exists")
        pass


    while (pyautogui.locateOnScreen('notification2.png')):
        sleep(1)
        print("Cutting right!")
        pyautogui.click()
        pyautogui.moveTo(764,454)
        sleep(3)

    sleep(3)
