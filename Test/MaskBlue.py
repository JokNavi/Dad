import cv2
import numpy as np
 

 

Image = cv2.imread('Everything.jpg')
# It converts the BGR color space of image to HSV color space
hsvImage = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
# Threshold of blue in HSV space
lower_blue = np.array([110, 245, 250])
upper_blue = np.array([120, 255, 254])
 
# preparing the mask to overlay
mask = cv2.inRange(hsvImage, lower_blue, upper_blue)
     
# The black region in the mask has the value of 0,
# so when multiplied with original image removes all non-blue regions
result = cv2.bitwise_and(Image, Image, mask = mask)
 
cv2.imshow('Image', Image)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
     
cv2.waitKey(0)
 
cv2.destroyAllWindows()
