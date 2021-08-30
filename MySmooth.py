import cv2
import numpy as np

def MySmooth(img):
    rows, columns = np.shape(img)
    Ismooth = np.zeros((rows+2, columns+2), dtype=np.uint8)
    Ismooth[1:rows+1, 1:columns+1] = img
    for r in range(1,rows+1):
        for c in range(1, columns+1):
            avg = np.sum(Ismooth[r-1:r+2:1, c-1:c+2:1])/9
            Ismooth[r, c] = avg
    return Ismooth
I = cv2.imread(r'C:\Program Files\MATLAB\R2021a\toolbox\images\imdata\bag.png', cv2.IMREAD_ANYDEPTH)
cv2.imshow('figure1', I)
Ismooth = MySmooth(I)
cv2.imshow('figure1-smooth', Ismooth)
Ismooth = MySmooth(Ismooth)
cv2.imshow('figure1-smooth2', Ismooth)
cv2.waitKey(0)

