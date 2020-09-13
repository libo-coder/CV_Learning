# coding=utf-8
"""
直方图均衡化
@author: libo
"""
import cv2
import numpy as np

img = cv2.imread('../test_img/003.jpg', 1)
cv2.imshow('src', img)
cv2.waitKey(0)

######## 方式一：对单通道图像进行均衡化
# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('gray', gray)
# cv2.waitKey(0)

# # 对灰度图进行均衡化
# dst = cv2.equalizeHist(gray)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)


######## 方式二：对多通道图像进行均衡化
# b, g, r = cv2.split(img)
# bH = cv2.equalizeHist(b)
# gH = cv2.equalizeHist(g)
# rH = cv2.equalizeHist(r)
# dst = cv2.merge((bH, gH, rH))
# cv2.imshow('dst', dst)
# cv2.waitKey(0)


######## 方式三：对 YUV 图像进行均衡化
imgYUV = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
cv2.imshow('imgYUV', imgYUV)
cv2.waitKey(0)

channelYUV = cv2.split(imgYUV)
channelYUV[0] = cv2.equalizeHist(channelYUV[0])
channels = cv2.merge(channelYUV)
dst = cv2.cvtColor(channels, cv2.COLOR_YCrCb2RGB)
cv2.imshow('dst', dst)
cv2.waitKey(0)