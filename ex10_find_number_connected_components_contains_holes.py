import cv2
import numpy as np
import matplotlib.pyplot as plt

imgUrl = "holes.jpg"
imgUrl = 'u.jpg'

img = cv2.imread(imgUrl, cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY)

#img = cv2.resize(img, (300, 300))
cv2.imshow("original", img)
imgNeg = 255 - img
#imgNeg = img
imgSmooth = cv2.GaussianBlur(imgNeg, (3, 3), cv2.BORDER_DEFAULT)
lablesNum, labledImg = cv2.connectedComponents(imgSmooth)
holesComponents = 0
for i in range(lablesNum):
    tempImg = np.ones_like(labledImg) * 255
    tempImg[labledImg == i] = 0
    tempImg = np.array(tempImg, dtype=np.uint8)
    tempLablesNum, tempLabledImg = cv2.connectedComponents(tempImg)
    cv2.imshow(str(i), cv2.resize(tempImg, (300, 300)))
    print(tempLablesNum)
    print("/////////")
    if i != 0 and tempLablesNum > 2:
        holesComponents += 1
print("Num of component with holes:" + str(holesComponents))

cv2.imshow("neg", imgNeg)
cv2.waitKey(0)