import cv2
import numpy as np
import sys
def Red():
    Image = cv2.imread('OnlyLines.png')
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    threshold_level = 100
    coords = np.column_stack(np.where(gray < threshold_level))
    mask = gray < threshold_level
    Image[mask] = (	0, 0, 255)
    Image.save("MainProject\Out\Red.jpg") 
    cv2.imshow('Red', Image)
    cv2.waitKey()
    return coords
def Green():
    Image = cv2.imread('OnlyGreenPointsWhite.png')
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    threshold_level = 200
    coords = np.column_stack(np.where(gray < threshold_level))
    mask = gray < threshold_level
    Image[mask] = (0, 255, 0)
    Image.save("MainProject\Out\Green.jpg") 
    cv2.imshow('Green', Image)
    cv2.waitKey()
    return coords
def Blue():
    Image = cv2.imread('OnlyBlueDots.png')
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    threshold_level = 100
    coords = np.column_stack(np.where(gray < threshold_level))
    mask = gray < threshold_level
    Image[mask] = (255, 0, 0)
    Image.save("MainProject\Out\Blue.jpg") 
    cv2.imshow('Blue', Image)
    cv2.waitKey()
    return coords
if (__name__ == '__main__'):
    sys.exit()
