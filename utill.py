import numpy as np
import cv2
def montage(imgList : list, convDim : tuple, finalDim : tuple, mode = None):
    convDim = np.array(convDim)
    montageDim = convDim[:2] * finalDim

    row = 0
    column = 0
    if convDim[2] == 1:
        montageImg = np.zeros((montageDim[0], montageDim[1]), dtype=np.float32)
    else:
        montageImg = np.zeros((montageDim[0], montageDim[1], convDim[2]), dtype=np.float32)
    for i in range(len(imgList)):
        if imgList[i].shape[2] == 1 and convDim[2] == 3:
            img = cv2.cvtColor(imgList[i], cv2.COLOR_GRAY2RGB)
        elif imgList[i].shape[2] == 3 and convDim[2] == 1:
            img = cv2.cvtColor(imgList[i], cv2.COLOR_RGB2GRAY)
        else:
            img = cv2.cvtColor(imgList[i], cv2.COLOR_BGR2RGB)

        img = cv2.resize(img, (convDim[0], convDim[1]))

        if convDim[2] == 1:
            montageImg[row * convDim[0]:(row + 1) * convDim[0], column * convDim[1]:(column + 1) * convDim[1]] = img
        else:
            montageImg[row * convDim[0]:(row + 1) * convDim[0], column * convDim[1]:(column + 1) * convDim[1], :] = img

        if column == finalDim[1] -1:
            column = 0
            row += 1
        else:
            column += 1
    if mode is not None:
        montageImg = cv2.cvtColor(montageImg, mode)
    return montageImg
