#FUNCTIONS

import re
import cv2
import json
import imutils
import numpy as np
from PIL import Image



class ImageManipulation():
    def __init__(self,Im):
        self.Im = Im

    def TrackCorners(self,input): 
        img = cv2.imread(input)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        Corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
        Corners = np.int0(Corners)
        '''for corner in Corners:
            x,y = corner.ravel()
            cv2.rectangle(img,(x-5,y+5),(x+5,y-5),255,-1)
        #cv2.imshow('Corner',img)   
        #cv2.waitKey(0)
        cv2.imwrite('MainProject\Out\IntersectsAndLines.jpg',img)'''
        return Corners

    def Size(self,Im):
        return Im.size

    def FindColour(self,X, Y):
        pix = self.Im.load()
        return pix[int(X),int(Y)]


    def ReplaceColour(self,X,Y):
        pix = self.Im.load()
        pix[int(X),int(Y)] = 255,255,255
        self.Im.save('MainProject\Out\Modified.jpg')

    def PlaceIntersect(self, Coord, Facing):
        Minus = lambda a : int(a) - 5
        Plus = lambda a : int(a) + 5
        if Facing == '-X': return [Minus(Coord[0]), Coord[1]]
        if Facing == '+X': return [Plus(Coord[0]), Coord[1]]
        if Facing == '-Y': return [Coord[0], Minus(Coord[1])]
        if Facing == '+Y': return [Coord[0], Plus(Coord[1])]
        

class Tracking():
    def FindEdges(self,Img, DirectionsL, Coord):
        
        Im = Image.open(Img)
        I = ImageManipulation(Im)
        Minus = lambda a : int(a) - 2
        Plus = lambda a : int(a) + 2
        I.ReplaceColour(Coord[0],Coord[1])
        if '-X' in DirectionsL and I.FindColour(Minus(Coord[0]), Coord[1])>(20,20,20):
            return '-X'

        if '+X' in DirectionsL and I.FindColour(Plus(Coord[0]), Coord[1])>(20,20,20):
                return '+X'

        if '-Y' in DirectionsL and I.FindColour(Coord[0], Minus(Coord[1]))>(20,20,20):
                return '-Y'

        if '+Y' in DirectionsL and I.FindColour(Coord[0], Plus(Coord[1]))>(20,20,20):
                return '+Y'
        else: return 'N'

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
        cv2.imshow('image',image)
        cv2.waitKey(0)
        with open('MainProject\Out\CoordsGreenDots.json', 'w') as File:
            File.write(json.dumps(SendToFile))
            File.close()
            return SendToFile
   
class Intersects():
    def __init__(self,ImagePath):
        self.Photo = ImagePath

    def FindLines(self, Img, Coord):
        Facing = []
        Directions = ['-X','+X','-Y','+Y']
        for x in  range(4):
            FacingRightNow = (C.FindEdges(Img,Directions,Coord))
            if FacingRightNow in Directions:
                Directions.remove(FacingRightNow)
                #ModifiedCoord.append(I.PlaceIntersect(Coord, Facing))
            Facing.append(FacingRightNow)
        return Facing
       
    def PlusCoord(self, Coord):
        Plus = lambda a : int(a) + 2
        Coord[0], Coord[1] = Plus(Coord[0]) , Plus(Coord[1])
        Coord = [Coord[0], Coord[1]]
        return Coord

    def MinusCoord(self, Coord):
        Minus = lambda a : int(a) - 2
        Coord[0], Coord[1] = Minus(Coord[0]), Minus(Coord[1])
        Coord = [Coord[0], Coord[1]]
        return Coord

    def RemoveNone(self, Facing):
        Facing = list(filter(('N').__ne__, Facing))
        return Facing


    def FindIntersect(self):
        ImagePath = Image.open(self.Photo)
        I = ImageManipulation(ImagePath)
        M = Intersects()
        Coords = I.TrackCorners(self.Photo)
        Dot = 1
        Coord = Coords[Dot]
         #Coord = [(90, 726), (80, 736)]
        Coord = re.findall('[0-9]+', str(Coord))
        Facing = M.FindLines(self.Photo, Coord)
        Facing = M.RemoveNone(Facing)

        if len(Facing) == 3: return 'Error 3 Sides match. Wierd coord location.'
        if len(Facing) >= 4:
            print('\n')  
            Coord = M.PlusCoord(Coord)
            Facing = M.FindLines(self.Photo, Coord)
            Facing = M.RemoveNone(Facing)
            Coord =  M.MinusCoord(Coord)
        if len(Facing) >= 4:
            print('\n')  
            Coord = M.MinusCoord(Coord)
            Facing = M.FindLines(self.Photo, Coord)
            Facing = M.RemoveNone(Facing)
            Coord = M.PlusCoord(Coord)
        if len(Facing) == 3: return 'Error 4 Sides match. Wierd coord location.'
        print(Facing)
        print(Coord)

        Counter = 0
        while Counter < len(Facing):
            Coord = I.PlaceIntersect(Coord, Facing[Counter])
            Counter = Counter + 1
        print(Coord)
        I.ReplaceColour(Coord[0],Coord[1])
        return Coord