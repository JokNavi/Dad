#FUNCTIONS
import math
import imutils
import cv2
import json

def Length(InputOne,InputTwo):
    #0,1 | x1, y1
    #1,0 | x2, y2
    dist = math.sqrt((int(InputTwo[0]) - int(InputOne[0]))**2 + (int(InputTwo[1]) - int(InputOne[1]))**2)
    #dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(dist) 

def ShortestPath(Input, Weight, Goal):
    g = Input
    #6,        [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)]
    # Find the shortest path on a weighted graph
    g.es["weight"] = Weight
    # g.get_shortest_paths() returns a list of edge ID paths
    results = g.get_shortest_paths(0,to=Goal,weights=g.es["weight"],output="epath",)
    print(results) 

def Center(Input):
    # load the image, convert it to grayscale, blur it slightly,
    # and threshold it
    image = cv2.imread(Input)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    # find contours in the thresholded image
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # loop over the contours
    SendToFile = {}
    Counter = 0
    n = 2
    for c in cnts:
    # compute the center of the contour
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # draw the contour and center of the shape on the image
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(image, str(Counter), (cX - 20, cY - 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        #SendToFile[Counter]= [[int(cX),int(cY)]]
        SendToFile[Counter]= (int(cX),int(cY))
        Counter = Counter+1
        print(Counter)
    with open('MainProject\Out\CoordsGreenDots.txt', 'w') as file:
        file.write(json.dumps(SendToFile))
    cv2.imshow('image',image)
    cv2.waitKey(0)
    return SendToFile
#Center("out\OnlyGreenPoints.png")