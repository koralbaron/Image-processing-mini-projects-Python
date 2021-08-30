import cv2
import numpy as np
def convToYIQ(I):
    rows, columns, channels = np.shape(I)
    yiqI = np.zeros_like(I)
    for r in range(rows):
        for c in range(columns):
            R = np.array(I[r, c, 0])
            G = np.array(I[r, c, 1])
            B = np.array(I[r, c, 2])
            for i, metrixRow in enumerate(M):
                yiqI[r, c, i] = R * metrixRow[0] + G * metrixRow[1] + B * metrixRow[2]
    return yiqI

I = cv2.imread(r'C:\Program Files\MATLAB\R2021a\toolbox\images\imdata\kobi.png', cv2.IMREAD_COLOR)
cv2.imshow('orig', I)
M = np.array([[0.299, 0.587, 0.114],
            [0.596, -0.275, -0.321],
            [0.212, -0.523, 0.311]])
yiqI = convToYIQ(I)
yiqI[:, :, 0] = 255
cv2.imshow('histI-with-YIQ', yiqI)
cv2.waitKey(0)

