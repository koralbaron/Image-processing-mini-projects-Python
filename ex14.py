import cv2
import numpy as np
from utill import montage

#red
R1 = np.zeros((64, 64, 3), np.float32)
R1[:, :, 0] = 0.333 * 255
R1[:, :, 1] = 1 * 255
R1[:, :, 2] = 1 * 255
#R1 = cv2.cvtColor(R1, cv2.COLOR_HSV2BGR)
#cv2.imshow('rf', R1)
#cv2.waitKey(0)
#light red
R2 = np.zeros((64, 64, 3), np.float32)
R2[:, :, 0] = 0 * 255  #hue
R2[:, :, 1] = 0.5 * 255 #saturation
R2[:, :, 2] = 1 * 255 #value
R2 = cv2.cvtColor(R2, cv2.COLOR_HSV2RGB)

#green
G1 = np.zeros((64, 64, 3), np.float32)
G1[:, :, 0] = 0.333
G1[:, :, 1] = 1
G1[:, :, 2] = 1
G1 = cv2.cvtColor(G1, cv2.COLOR_HSV2RGB)
#light green
G2 = np.zeros((64, 64, 3), np.float32)
G2[:, :, 0] = 0.333 #hue
G2[:, :, 1] = 0.5 #saturation
G2[:, :, 2] = 1 #value
G2 = cv2.cvtColor(G2, cv2.COLOR_HSV2RGB)

#blue
B1 = np.zeros((64, 64, 3), np.float32)
B1[:, :, 0] = 0.666
B1[:, :, 1] = 1
B1[:, :, 2] = 1
B1 = cv2.cvtColor(B1, cv2.COLOR_HSV2RGB)
#light blue
B2 = np.zeros((64, 64, 3), np.float32)
B2[:, :, 0] = 0.666 #hue
B2[:, :, 1] = 0.5 #saturation
B2[:, :, 2] = 1 #value
B2 = cv2.cvtColor(B2, cv2.COLOR_HSV2RGB)

imgList = [R1, R2, G1, G2, B1, B2]


colorMontage = montage(imgList, (64, 64, 3), (3, 2), )
cv2.imshow('montage', colorMontage)
cv2.waitKey(0)