import cv2
import numpy as np

def MyNegative(I):
    row, column = np.shape(I)
    for r in range(row):
        for c in range(column):
            I[r, c] = 255 - I[r, c]
    return I
I = cv2.imread(r'C:\Program Files\MATLAB\R2021a\toolbox\images\imdata\cameraman.tif', cv2.IMREAD_ANYDEPTH)
cv2.imshow('figure1', I)
Ineg = MyNegative(I)
cv2.imshow('figure1-neg', Ineg)
cv2.waitKey(0)


