import cv2
import numpy as np

def MyThresholding(I,T):
    Ibin = np.ones_like(I)*255
    row, column = np.shape(I)
    for r in range(row):
        for c in range(column):
            if I[r, c] < T:
                Ibin[r, c] = 0
    return Ibin

I = cv2.imread(r'C:\Program Files\MATLAB\R2021a\toolbox\images\imdata\pout.tif', cv2 .IMREAD_ANYDEPTH)
cv2.imshow('figure1', I)
T = 105;
Ibin = MyThresholding(I,T)
cv2.imshow('figure1-binary', Ibin)
cv2.waitKey(0)
