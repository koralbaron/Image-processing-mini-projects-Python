import cv2
import numpy as np
In = cv2.imread(r'C:\Program Files\MATLAB\R2021a\toolbox\images\imdata\cameraman.tif', cv2.IMREAD_ANYDEPTH)
cv2.imshow('figure1', In) #show image
row, column = In.shape #get image width and height
out1 = In[0:row-1:2, 0:column-1:2]# skip by 2
cv2.imshow('figure2', out1)
out2 = np.zeros_like(In)
out2[:-1:2, :-1:2] = out1
out2[1::2, :-1:2] = out1
out2[:-1:2, 1::2] = out1
out2[1::2, 1::2] = out1
cv2.imshow('figure3', out2)
print(row)
cv2.waitKey(0)