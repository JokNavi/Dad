import cv2
def Colour(Input):
    image = cv2.imread(Input)
    for y in range(0, 100, 10):
        for x in range(0, 100, 10):
            color = image[x, y]
    print(color)
