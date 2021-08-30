import cv2
import numpy as np
from utill import montage
def Colors(R, G, B):
    img = np.zeros((64, 64, 3), dtype=np.uint8)
    img[:,:,0] = R
    img[:, :, 1] = G
    img[:, :, 2] = B
    return img

colors = [[255,0,0],
          [0,255,0],
          [0,0,255],
          [255,255,0],
          [255,0, 255],
          [0,255,255],
          [255,255,255],
          [0,0,0]]

imgList = []
for ch in colors:
    imgList.append(Colors(ch[0],ch[1],ch[2]))

img = montage(imgList,(256,256,3),(2,4))
cv2.imshow('dd',img)
cv2.waitKey(0)


