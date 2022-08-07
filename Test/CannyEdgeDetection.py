import json
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('OnlyLines.png',0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image')
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image')
plt.show()
with open(r'Edges.txt', 'w') as fp:
    for item in edges:
        # write each item on a new line
        fp.write(item)
    print('Done')