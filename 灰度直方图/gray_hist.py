# coding=utf-8
"""
计算一幅图片的灰度直方图
@author: libo
"""
import matplotlib.pyplot as plt
import numpy as np
import cv2

import sys

def calcGrayHist(image):
    """
    :param image:
    :return: 返回值是一个一维的 ndarray, 依次存放 0~255 之间每一个灰度级对应的像素个数
    """
    rows, cols = image.shape[:2]
    grayHist = np.zeros([256], np.uint64)   # 存储灰度直方图
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] += 1
    return grayHist

if __name__ == '__main__':
    image = cv2.imread('../test_img/gray_1.png')
    grayHist = calcGrayHist(image)
    # print(grayHist)

    # 画出灰度直方图
    x_range = range(256)
    plt.plot(x_range, grayHist, 'r', linewidth=2, c='red')
    # 设置坐标轴的范围
    y_maxValue = np.max(grayHist)
    plt.axis([0, 255, 0, y_maxValue])
    # 设置坐标轴的标签
    plt.xlabel('gray Level')
    plt.ylabel('number of pixels')
    # 显示灰度直方图
    plt.show()