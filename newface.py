# coding:utf8
import pytesseract
import cv2
import matplotlib.pyplot as plt
import dlib
import matplotlib.patches as mpatches
from skimage import io,draw,transform,color
import numpy as np
import pandas as pd
import re
import pytesseract

detector = dlib.get_frontal_face_detector()
image = io.imread("./2.jpg")
dets = detector(image, 2) #使用detector进行人脸检测 dets为返回的结果
## 将识别的图像可视化
# cv2.imshow('img',dets)
# cv2.waitKey()
plt.figure()
ax = plt.subplot(111)
ax.imshow(image)
plt.axis("off")

for i, face in enumerate(dets):
    # 在图片中标注人脸，并显示
    left = face.left()
    top = face.top()
    right = face.right()
    bottom = face.bottom()
    # rect = mpatches.Rectangle((left,bottom), (right - left)*2, (top - bottom)*2,fill=False, edgecolor='red', linewidth=1)
    # ax.add_patch(rect)
    width = right - left
    high = bottom - top
    left2 = np.uint(left - 0.4 * width)
    bottom2 = np.uint(bottom + 0.55 * high)
    rect = mpatches.Rectangle((left2, bottom2), 1.85 * width, -2.2 * high,fill=False, edgecolor='blue', linewidth=1)
    ax.add_patch(rect)
    # print(bottom2)
    # print(left2)

    x=int(left2+1.85*width)-1
    y=int(bottom2-2.2*high)-1
    # print(high,width)
    # print(x,y)
    # print(bottom2,left2)

    cross=image[y:bottom2,left2:x]
    cv2.imshow('ee',cross)
    cv2.waitKey()
    cv2.imwrite('./22.png', cross)
    img=cv2.imread('./2.jpg')
    img[0:bottom2,left2:-1]=255
    cv2.imshow('ee', img)
    cv2.waitKey()
    cv2.imwrite('./cut.png',img)
plt.show()




#
# ax.add_patch(rect)
# plt.show()
#
# ## 身份证上人的照片
# top2 = np.uint(bottom2+2.2*high)
# right2 = np.uint(left2+1.8*width)
# image3 = image[top2:bottom2,left2:right2]
# # plt.imshow(image3)
# plt.axis("off")
# plt.show()