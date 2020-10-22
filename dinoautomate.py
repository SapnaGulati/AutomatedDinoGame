import pyautogui
from PIL import Image,ImageGrab
import time

def hit(key):
    pyautogui.press(key)

def isCollide(data):
    for i in range(670,750):
        for j in range(170,275):
            if (data[i, j] > 70 and data[i,j] < 90):
                hit("down")
                return

        for k in range(275,330):
            if (data[i, k] > 70 and data[i,k] < 90):
                hit("up")
                return
    return 

if __name__ == "__main__":
    print("Whooo!!!!! Dino Game is going to be start within 2 seconds")
    time.sleep(2)
    hit("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
    # init = time.time()
    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    # for i in range(670,750):
    #     for j in range(170,280):
    #         data[i, j] = 0
               
    #     for k in range(280,330):
    #         data[i, k] = 170
    # image.show()
    # final = time.time() - init
    # print(final)