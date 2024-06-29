import pyautogui
# import threading
import time
import datetime
import math

screenSize = pyautogui.size()

def moveMouse(x: int):
    pyautogui.moveTo(x, screenSize[1], duration = 1)

def clickMouse():
    pyautogui.click()

def moveInCircle():
    # Radius 
    R = 400
    # measuring screen size
    (x,y) = pyautogui.size()
    # locating center of the screen 
    (X,Y) = pyautogui.position(x/4,y/4)
    # offsetting by radius 
    pyautogui.moveTo(X+R,Y)

    for i in range(360):
        # setting pace with a modulus 
        if i%6==0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))


def main():
    while (True):
        moveInCircle()
        time.sleep(60*60)


    # while(True):
    #     time.sleep(10)
    #     moveMouse(1)
    #     time.sleep(10)
    #     moveMouse(-1)
    # hour = datetime.datetime.now().hour
    # min = datetime.datetime.now().minute
    
    
    # if min < min + 1:
    #     print("1 min pass")
    # threading.Timer(5.0, moveMouse).start()
    # threading.Timer(10.0, clickMouse).start()
    # else:



if __name__ == "__main__":
    main()