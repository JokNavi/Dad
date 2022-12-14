#FUNCTIONS
import re
import cv2
import json
import imutils
import numpy as np
from PIL import Image

class Intersects():
    def __init__(self,ImagePath):
        self.PhotoPath = ImagePath
        

    def FindLines(self, Coord):
        C = Tracking(self.PhotoPath)
        Facing = []
        Directions = ['-X','+X','-Y','+Y']
        for x in  range(4):
            FacingRightNow = (C.FindEdges(Directions,Coord))
            if FacingRightNow in Directions:
                Directions.remove(FacingRightNow)
            Facing.append(FacingRightNow)
        return Facing
       
    def ChangeCoord(self, Coord, Facing, Amount):
        Minus = lambda a : int(a) - Amount
        Plus = lambda a : int(a) + Amount
        if Facing == 'LeftTop': return [Minus(Coord[0]), Plus(Coord[1])]
        if Facing == 'RightTop': return [Plus(Coord[0]), Plus(Coord[1])]
        if Facing == 'LeftBottom': return [Minus(Coord[0]), Minus(Coord[1])]
        if Facing == 'RightBottom': return [Plus(Coord[0]), Minus(Coord[1])]
        return Coord

    def RemoveNone(self, Facing):
        Facing = list(filter(('N').__ne__, Facing))
        return Facing

    def FindIntersect(self, Dot):
        Im = Image.open(self.PhotoPath)
        IM = ImageManipulation(Im)
        M = Intersects(Im)
        Directions = ['LeftTop','RightTop','LeftBottom','RightBottom']
        Coords = IM.TrackCorners(self.PhotoPath)
        CoordSpecific = Coords[Dot]
        #Coord = [(90, 726), (80, 736)]
        CoordSpecific = re.findall('[0-9]+', str(CoordSpecific))
        Facing = M.FindLines(CoordSpecific)
        Facing = M.RemoveNone(Facing)
        CoordEdit = CoordSpecific
        print(CoordSpecific)
        HadToModify = False

        for Direction in Directions:
            CoordEdit = M.ChangeCoord(CoordSpecific, Direction, 1)
            FacingTemp = M.FindLines(CoordEdit)
            FacingTemp = M.RemoveNone(FacingTemp)
            if len(FacingTemp) == 1: HadToModify = True

        if HadToModify == True: 
            CoordSpecific = IM.EditCoord(CoordSpecific, Facing[0],15)
            CoordSpecific = IM.EditCoord(CoordSpecific, Facing[1],15)
        else: 
            CoordSpecific = IM.EditCoord(CoordSpecific, Facing[0],16)
            CoordSpecific = IM.EditCoord(CoordSpecific, Facing[1],16)
        print(CoordSpecific)
        #IM.ReplaceColour(CoordSpecific[0],CoordSpecific[1], (255,255,255), 'MainProject\Out\Modified.tif')
        print('\n')
        print(Facing)
        return CoordSpecific  

class ImageManipulation(Intersects):
    def __init__(self, ImagePath):
        super().__init__(ImagePath)
    
    def TrackCorners(self, InputString):
        Img = cv2.imread(InputString)
        gray = cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        Corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
        Corners = np.int0(Corners)
        return Corners

    def Size(self):
        return self.PhotoPath.size

    def FindColour(self,X, Y):
        pix = self.PhotoPath.load()
        return pix[int(X),int(Y)]

    def ReplaceColour(self,X,Y, Colour, Save):
        pix = self.PhotoPath.load()
        pix[int(X),int(Y)] = Colour
        self.PhotoPath.save(Save)

    def EditCoord(self, Coord, Facing, Amount):
        Minus = lambda a : int(a) - Amount
        Plus = lambda a : int(a) + Amount
        if Facing == '-X': return [Minus(Coord[0]), Coord[1]]
        if Facing == '+X': return [Plus(Coord[0]), Coord[1]]
        if Facing == '-Y': return [Coord[0], Minus(Coord[1])]
        if Facing == '+Y': return [Coord[0], Plus(Coord[1])]

class Tracking(Intersects):
    def __init__(self, ImagePath):
        super().__init__(ImagePath)

    def FindEdges(self, DirectionsL, Coord):
        I = ImageManipulation(self.PhotoPath)
        Minus = lambda a : int(a) - 1
        Plus = lambda a : int(a) + 1
        if '-X' in DirectionsL and I.FindColour(Minus(Coord[0]), Coord[1])>(20,20,20):
            return '-X'

        if '+X' in DirectionsL and I.FindColour(Plus(Coord[0]), Coord[1])>(20,20,20):
                return '+X'

        if '-Y' in DirectionsL and I.FindColour(Coord[0], Minus(Coord[1]))>(20,20,20):
                return '-Y'

        if '+Y' in DirectionsL and I.FindColour(Coord[0], Plus(Coord[1]))>(20,20,20):
                return '+Y'
        else: return 'N'
class Visualisation():
    def ShowDots():
        pass
