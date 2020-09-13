# coding=utf-8
"""
彩色图像直方图
@author: libo
"""
import cv2
import numpy as np

def ImageHist(image, type):
    color = (255, 255, 255)
    windowName = 'Gray'
    if type == 31:
        color = (255, 0, 0)
        windowName = 'B Hist'
    elif type == 32:
        color = (0, 255, 0)
        windowName = 'G Hist'
    elif type == 33:
        color = (0, 0, 255)
        windowName = 'R Hist'

    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    minV, maxV, minL, maxL = cv2.minMaxLoc(hist)

    histImg = np.zeros([256, 256, 3], np.uint8)
    for h in range(256):
        intenNormal = int(hist[h] * 256 / maxV)
        cv2.line(histImg, (h, 256), (h, 256-intenNormal), color)
    cv2.imshow(windowName, histImg)

    return histImg


if __name__ == '__main__':
    img = cv2.imread('../test_img/002.jpg')
    channels = cv2.split(img)       # B G R
    for i in range(3):
        ImageHist(channels[i], 31 + i)
    cv2.waitKey(0)
