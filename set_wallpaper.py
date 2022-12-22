import numpy as np
import cv2
import os
import random
import ctypes
# from wallpaper import set_wallpaper, get_wallpaper

def getRandomFrame(folderPath='./videos/'):
    videoList = os.listdir(folderPath)
    video = random.choice(videoList)
    cap = cv2.VideoCapture(f'{folderPath}{video}')
    numFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameNum = random.randint(0, numFrames-1)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frameNum)
    ret, frame = cap.read()
    if ret:
        return frame
    return None

if __name__ == '__main__':
    for _ in range(10):
        frame = getRandomFrame()
        if (frame is not None) and (frame.mean() > 10):
            cv2.imwrite('to_set.png', frame)
            filepath = os.path.abspath('to_set.png')
            SPI_SETDESKWALLPAPER = 20 
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filepath , 0)