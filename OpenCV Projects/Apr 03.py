import cv2
import numpy as np


blurRadius = 5
elephantImg = cv2.imread('elephant.jpg', 0)
noise = np.zeros(elephantImg.shape, np.uint8)
cv2.randu(noise, 0, 255)
elephantImgWithNoise = elephantImg + np.array(0.2*noise, dtype=np.uint8)
blur_kernel = np.array([[0.0625, 0.125, 0.0625],
                        [0.125, 0.25, 0.125],
                        [0.0625, 0.125, 0.0625]])

newImg = np.zeros([elephantImg.shape[0]+2*blurRadius, elephantImg.shape[1]+2*blurRadius], np.uint8)
newImg[blurRadius:blurRadius + elephantImg.shape[0], blurRadius:blurRadius+elephantImg.shape[1]] = elephantImgWithNoise

print(elephantImg.shape)

elephantBlur = np.zeros(newImg.shape, np.uint8)

for rowN in range(blurRadius, newImg.shape[0]-blurRadius):
    for colN in range(blurRadius, newImg.shape[1]-blurRadius):
        #get current pixel
        pixel = newImg[rowN, colN]
        #get neighbours

        neighbours = newImg[rowN -blurRadius: rowN+blurRadius+1, colN-blurRadius: colN+blurRadius+1]
        #apply blur by * kernel
        #print(f"row: {rowN}, column: {colN}")
        #add values
        #replace the pixel value
        newImg[rowN, colN] = int(np.mean(neighbours))

cv2.imshow('window', elephantImg)
cv2.imshow('window2', elephantImgWithNoise)
cv2.imshow('blurred image', newImg)
cv2.waitKey(0)
