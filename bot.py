
from pickletools import pyunicode
import pyautogui
from time import sleep
import signal
import AppKit

from botclasses import StopWatch, Tree, Bank, Person, Bag

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


def main():

    kiko = Person()
    bag = Bag()
    tree = Tree()
    bank = Bank()
    timer = StopWatch()

    # while True:
    #     pyautogui.displayMousePosition()

    while True:
    # Check if bag is full
        while (bag.isbagfull() != True):
            # Check if right tree exists
            if (kiko.position == 0):
                kiko.tryCut()
                sleep(4)

            if (kiko.position == 0 and tree.checkAlive() == False):
                kiko.cutLeftTree()
            
            if (kiko.position == 1):
                pyautogui.click()
                sleep(4)

            if (bag.isbagfull()):
                break

            if (kiko.position == 1 and tree.checkAlive() == False):
                kiko.cutRightTree()
            
                
        if(kiko.position == 1):
            kiko.cutRightTree()

        kiko.walktobank()
        bank.deposit()
        kiko.gobacktotree()
        kiko.tryCut()
    
    timer.stop()
    print(timer.getElapsedTime())





# Catches Ctrl + C
def handler(signum, frame):
    res = input("Do you really want to exit? y/n ")
    if res == 'y':

        exit(1)

# signal.signal(signal.SIGINT, handler)

# while True:

#     if pyautogui.locateOnScreen('notification.png'):
#         AppKit.NSBeep()

# bank.deposit()
        
    



# DEBUG MODE
DEBUG = 0

if (DEBUG):
    debugTimer = StopWatch()
    debugTimer.start()
    pyautogui.displayMousePosition()
    # while True:
    #     kiko.tryCut()

    debugTimer.stop()
    print(debugTimer.getElapsedTime())



if __name__ == "__main__":
    main()