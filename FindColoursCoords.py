import cv2
import numpy as np
import sys
def Red():
    image = cv2.imread('OnlyLines.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Set threshold level
    threshold_level = 100

    # Find coordinates of all pixels below threshold
    coords = np.column_stack(np.where(gray < threshold_level))

    #print(coords)

    # Create mask of all pixels lower than threshold level
    mask = gray < threshold_level

    # Color the pixels in the mask
    image[mask] = (	0, 0, 255)
    cv2.imshow('Red', image)
    cv2.waitKey()
    return coords
def Green():
    image = cv2.imread('OnlyGreenPointsWhite.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Set threshold level
    threshold_level = 200

    # Find coordinates of all pixels below threshold
    coords = np.column_stack(np.where(gray < threshold_level))

    #print(coords)

    # Create mask of all pixels lower than threshold level
    mask = gray < threshold_level

    # Color the pixels in the mask
    image[mask] = (0, 255, 0)

    cv2.imshow('Green', image)
    cv2.waitKey()
    return coords
def Blue():
    image = cv2.imread('OnlyBlueDots.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Set threshold level
    threshold_level = 100

    # Find coordinates of all pixels below threshold
    coords = np.column_stack(np.where(gray < threshold_level))

    #print(coords)

    # Create mask of all pixels lower than threshold level
    mask = gray < threshold_level

    # Color the pixels in the mask
    image[mask] = (255, 0, 0)
    cv2.imshow('Blue', image)
    cv2.waitKey()
    return coords
if (__name__ == '__main__'):
    sys.exit()
