#FUNCTIONS
import sys
import cv2
import math
import json
import imutils
import colorsys
import networkx as nx
class Colours():

    def HexToRgb(self,HEX):
        LineColourHex = HEX.lstrip('#')
        Output = list(tuple(int(LineColourHex[i:i+2], 16) for i in (0, 2, 4)))
        print('RGB: ', Output)
        return Output

    def RgbToHsv(self,RGB):
        (r, g, b) = (RGB[0], RGB[1], RGB[2])
        #normalize
        (r, g, b) = (r / 255, g / 255, b / 255)
        #convert to hsv
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
        #expand HSV range
        (h, s, v) = (int(h * 179), int(s * 255), int(v * 255))
        Output = h,s,v
        print('HSV: ', Output)
        return Output

class ImageManipulation():

    def Center(self, Input):
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
        return SendToFile

    def Mask(self, Input, Colour):
        img = cv2.imread(Input)
        ## mask of red color
        C = Colours()
        Colour = C.HexToRgb(Colour)
        Colour = C.RgbToHsv(Colour)
        mask = cv2.inRange(img, (0,0,200),(Colour))
        ## mask of blue color
        res = cv2.bitwise_and(img,img,mask= mask)
        ## final mask
        cv2.imwrite(Colour, res)

class Paths():

    def Length(self,InputOne,InputTwo):
        #0,1 | x1, y1
        #1,0 | x2, y2
        #dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        Dist = math.sqrt((int(InputTwo[0]) - int(InputOne[0]))**2 + (int(InputTwo[1]) - int(InputOne[1]))**2) 
        return Dist 

    def ShortestPath(self,Nodes,Start,End):
        G = nx.Graph(Nodes)
        G.add_edge("0", "1", weight=4)
        G.add_edge("1", "3", weight=2)
        G.add_edge("0", "2", weight=3)
        G.add_edge("2", "3", weight=4)
        return nx.shortest_path(G, str(Start), str(End), weight="weight")

class CheckPaths():
    def __init__(self,Im):
        self.Im = Im
    def FindColour(self, X, Y):
            pix = self.Im.load()
            print("Image size: ",self.Im.size)  # Get the width and hight of the image for iterating over # Get the RGBA Value of the a pixel of an image
            return pix[X,Y]

    def ReplaceColour(self,X,Y):
            pix = self.Im.load()
            pix[X,Y] = 255,255,255
            self.Im.save('MainProject\Out\Modified.png')

if (__name__ == '__main__'):
    sys.exit()