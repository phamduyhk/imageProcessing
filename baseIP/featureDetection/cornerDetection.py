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




def main():
    imgArray = np.array([[48,46,2,7,14],
                        [50,52,3,8,15],
                        [42,58,9,11,17],
                        [34,30,14,18,20],
                        [25,31,39,30,24]])
    gen = np.array(imgArray ,dtype=np.uint8)


if __name__ == '__main__':
    main()
    