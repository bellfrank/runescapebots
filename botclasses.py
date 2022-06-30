import pyautogui
from time import sleep
import time
import random

class Bank:
    def __init__(self):
        self.logs = 0

    def deposit(self):
        pyautogui.moveTo(881, 384)
        pyautogui.click()

class Tree:
    def __init__(self):
        self.alive = False
    
    def checkAlive(self):
        if (pyautogui.locateOnScreen('notification.png', confidence=0.9) != None):
            self.alive = True
        else:
            self.alive = False
        
        return self.alive


class Person:
    def __init__(self):
        self.position = 0
    
    def walktobank(self):
        if self.position == 0:
            pyautogui.moveTo(263, 277)
            print("hi")
            pyautogui.doubleClick()
            print("bye")
            sleep(9)
        else:
            pyautogui.moveTo(396, 225)
            pyautogui.click()
            sleep(9)
    
    def gobacktotree(self):
        pyautogui.moveTo(1366, 145)
        pyautogui.click()
        sleep(8)
        pyautogui.moveTo(857, 354)
        pyautogui.click()

    def cutRightTree(self):
        self.position = 0
        pyautogui.moveTo(876, 403)
        pyautogui.click()
        pyautogui.moveTo(772, 481)
    
    def cutLeftTree(self):
        self.position = 1
        pyautogui.moveTo(532, 530)
        pyautogui.click()
        pyautogui.moveTo(663, 448)
        
    def tryCut(self):
        pyautogui.moveTo(772, 481)
        pyautogui.click()



class Bag:
    def __init__(self):
        self.full = False
        self.logs = 0

    def isbagfull(self):
        self.full = (pyautogui.locateOnScreen('full.png', confidence=0.95) != None)
        return self.full


class StopWatch:
    def __init__(self):
        self.__startTime = time.time()

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime
    
    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__endTime = time.time()
    
    def getElapsedTime(self):
        return int(1* (self.__endTime - self.__startTime))