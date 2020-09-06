# coding=utf-8
"""
计算一幅图片的灰度直方图，利用 matplotlib 内置函数 hist 实现
@author: libo
"""
import matplotlib.pyplot as plt
import numpy as np
import cv2

import sys

if __name__ == '__main__':
    image = cv2.imread('../test_img/gray_1.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
    rows, cols = image.shape[:2]
    print('rows=%d, cols=%d, rows*cols=%d' % (rows, cols, rows*cols))
    print('image.size=%d' % image.size)

    pixelSquence = image.reshape([rows*cols, ])     # 将二维的图像矩阵变为一维的数组，便于计算灰度直方图
    numberBins = 256    # 组数
    histogram, bins, patch = plt.hist(pixelSquence, numberBins, facecolor='red', histtype='bar')

    plt.xlabel(u'gray Level')
    plt.ylabel(u'number of pixels')

    y_maxValue = np.max(histogram)
    plt.axis([0, 255, 0, y_maxValue])

    plt.show()
