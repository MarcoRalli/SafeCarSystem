from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll
import cv2 as cv
import numpy
from time import time
from PIL import Image
import os
import pyautogui

windowId = None
windowName = 'Try2Catch'
count = 0

def findWindowId():
    global windowId

    print('searching window id')

    windowList = CGWindowListCopyWindowInfo(
        kCGWindowListOptionAll, kCGNullWindowID)

    for window in windowList:
        print(window.get('kCGWindowName', ''))
        if(windowName.lower() in window.get('kCGWindowName', '').lower()):
            windowId = window['kCGWindowNumber']
            print('found window id %s' % windowId)
            return True

    print('unable to find window id')
    return False


def takeScreenshot(count):
    if windowId is None:
        if findWindowId() is False:
            return
   
    # -x mutes sound and -l specifies windowId
    pyautogui.screenshot("image/"+str(count)+".png")

    # os.system('screencapture -x -l %s %s' % (windowId, imageFileName))
    # img = Image.open(imageFileName)
    # print(img)
    # img = numpy.array(img)
    # os.remove(imageFileName)
    return None


