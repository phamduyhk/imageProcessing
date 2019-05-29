import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import os
import numpy as np
os.chdir('../')

def showImg(img,ave,med,gaussian):
    plt.subplot(221),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(ave),plt.title('average')
    plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(med),plt.title('median')
    plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(med),plt.title('gaussian')
    plt.xticks([]), plt.yticks([])
    plt.show()

def averageBlur(img):
    kernel3x3 = np.ones((3,3),np.float32)/9
    print("kernel3x3:")
    print(kernel3x3)
    dst = cv2.filter2D(img,-1,kernel3x3)
    return dst

def medianBlur(img):
    median = cv2.medianBlur(img,3) # 3 is kernel size
    return median

def GaussianBlur(img):
    blur = cv2.GaussianBlur(img,(3,3),0)  # (3,3) is kernel size
    return blur

def main():
    imgArray = np.array([[48,46,2,7,14],
                        [50,52,3,8,15],
                        [42,58,9,11,17],
                        [34,30,14,18,20],
                        [25,31,39,30,24]])
    gen = np.array(imgArray ,dtype=np.uint8)

    average = averageBlur(gen)
    median = medianBlur(gen)
    gaussian = GaussianBlur(gen)
    print("average 行列：")
    print(average)
    print("median 行列：")
    print(median)
    print("gaussian 行列：")
    print(gaussian)

    img = cv2.imread('./picture/mountain.png')
    average = averageBlur(img)
    median = medianBlur(img)
    gaussian = GaussianBlur(img)
    showImg(img,average,median,gaussian)

if __name__ == '__main__':
    main()
    