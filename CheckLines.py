import cv2 as cv
import numpy as np
import math

src_img = cv.imread('OnlyLines.png')
cv.imshow('Original Image',src_img)

dst_img = cv.Canny(src_img, 50, 100, None, 3)

linesP = cv.HoughLinesP(dst_img, 1, np.pi / 180, 50, None, 50, 10)

for i in range(0, len(linesP)):
            lin = linesP[i][0]
            cv.line(src_img, (lin[0], lin[1]), (lin[2], lin[3]), (0,0,1), 3, cv.LINE_AA)

cv.imshow("Image with lines", src_img)
cv.waitKey(0)