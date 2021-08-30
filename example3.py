import cv2
import numpy as np

I = np.zeros((64, 64), dtype=np.uint8)
I1 = I[:]
print(I1.shape)
I1[24:40, 24:40] = 128
I2 = I+200
I[24:40, 24:40] = 128
print(I1.shape)

imgMontage = np.zeros((I.shape[0], I.shape[1]*2), dtype=np.uint8)
imgMontage[:, : 64] = I1
imgMontage[:, 64:] = I2
cv2.imshow('montage', imgMontage)
cv2.waitKey(0)
