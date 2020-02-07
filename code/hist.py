import cv2
import time
import sys
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1205-1502-b.jpg')
cv2.imshow("frame1",img)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.ylim([0,6])

    
plt.show()