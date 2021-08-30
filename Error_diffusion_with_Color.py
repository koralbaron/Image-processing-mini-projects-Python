import cv2
import numpy as np
import sys

THRESHOLD = 256/8

# Description: Convert 256 levels to 8 levels with value of 0-255 and return this value.
def convNewToLevel(value):
    newLevel = value//THRESHOLD # divide with floor in range of [0, 7]
    return newLevel * (255/7)

# Description: Convert input image with 256 levels to 8 levels image and return this new image
def colorErrorDiffusion(img):
    row, column, channels = np.shape(img)
    err = np.zeros((row+2, column+2, channels), dtype=np.float32)
    newImg = np.zeros_like(img)
    #orig = img[:]
    for r in range(0, row):
        for c in range(0, column):
            for ch in range(channels):
                newImg[r, c, ch] = convNewToLevel(img[r, c, ch] + err[r, c, ch])
                diff = (img[r, c, ch] + err[r, c, ch]) - newImg[r, c, ch]
                err[r + 1, c, ch] = err[r + 1, c, ch] + diff * 5 / 16
                err[r, c + 1, ch] = err[r, c + 1, ch] + diff * 7 / 16
                err[r + 1, c + 1, ch] = err[r + 1, c + 1, ch] + diff * 1 / 16
                err[r + 1, c - 1, ch] = err[r + 1, c - 1, ch] + diff * 3 / 16
    return newImg

# Description: Convert input image with 256 levels to 8 levels image and print both images, than save the converted
# image as newColor.png.
def main(argv):
    img = cv2.imread(argv[1])
    img = cv2.resize(img, (220, 250))
    print('Processing...')
    newImg = colorErrorDiffusion(img)
    print("done. New Image called newColor.png located at the code folder")
    cv2.imshow('orig', img)
    cv2.imshow('newImg', newImg)
    cv2.imwrite('newColor.png', newImg)
    cv2.waitKey(0)

if __name__ == '__main__':
    main(sys.argv)
