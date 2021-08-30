import cv2
import numpy as np

def Error_diffusion(img):
    row, column = np.shape(img)
    err = np.zeros((row+2, column+2), dtype=np.float32)
    Ib = np.zeros_like(img, dtype=np.uint8)
    orig = img[:]
    for c in range(1, column):
        for r in range(1, row):
            if (orig[r, c] + err[r, c]) < 128:
                Ib[r, c] = 0
            else:
                Ib[r, c] = 255
            diff = (orig[r, c] + err[r, c]) - Ib[r, c]
            err[r+1, c] = err[r+1, c] + diff*5/16
            err[r, c+1] = err[r, c+1] + diff*7/16
            err[r+1, c+1] = err[r+1, c+1] + diff*1/16
            err[r+1, c-1] = err[r+1, c-1] + diff*3/16
    return Ib # np.uint8(Ib)

I= cv2.imread(r'C:\Users\Koral\Desktop\girlface.jpg', cv2.IMREAD_ANYDEPTH)
print(I.shape)
cv2.imshow('orig', I)
Ib = Error_diffusion(I)
cv2.imshow('Error_diffusion', Ib)
cv2.waitKey(0)
