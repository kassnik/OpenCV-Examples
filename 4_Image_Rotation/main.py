#!/usr/bin/python
import cv2
import numpy as np

img = cv2.imread('lena.jpg',0)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2),32,-1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
