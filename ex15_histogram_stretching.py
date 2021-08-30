import cv2
import numpy as np
from utill import montage
I = cv2.imread(r'C:\Program Files\MATLAB\R2021a\toolbox\images\imdata\kobi.png', cv2.IMREAD_COLOR)
cv2.imshow('I', I)
GrayI = cv2.cvtColor(I, cv2.COLOR_RGB2GRAY)
cv2.imshow('GrayI', GrayI)
HistI = np.zeros_like(GrayI)
cv2.equalizeHist(GrayI, HistI)
#cv2.imshow('HistI', HistI)
rgbImage = cv2.cvtColor(HistI, cv2.COLOR_GRAY2RGB)
cv2.imshow('rgbImage', rgbImage)
#montage([I, GrayI, HistI, rgbImage], (128,128,3), (2,2))
cv2.waitKey(0)