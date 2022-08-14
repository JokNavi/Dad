#FUNCTIONS
import sys
import cv2
import math
import json
import numpy as np
import networkx as nx 

class Colours:

    def HexToRgb(self,HEX):
        LineColourHex = HEX.lstrip('#')
        Output = list(tuple(int(LineColourHex[i:i+2], 16) for i in (0, 2, 4)))
        print('RGB: ', Output)
        return Output

    def RgbToHsv(self,RGB):
        BGR = np.uint8([[RGB]])
        Output = cv2.cvtColor(BGR,cv2.COLOR_BGR2HSV)
        print (Output)
        return Output

class Paths():  
    def Length(self,InputOne,InputTwo):
        #0,1 | x1, y1
        #1,0 | x2, y2
        #dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        Dist = math.sqrt((int(InputTwo[0]) - int(InputOne[0]))**2 + (int(InputTwo[1]) - int(InputOne[1]))**2) 
        return Dist 
        
    def ShortestPath(self,Start,End,Nodes):
        G = nx.Graph()
        G.add_edge("0", "1", weight=4)
        G.add_edge("1", "3", weight=2)
        G.add_edge("0", "2", weight=3)
        G.add_edge("2", "3", weight=4)
        return nx.shortest_path(G, str(Start), str(End), weight="weight")

class CheckPaths:
    def __init__(self, ImagePath, Coords):
        self.PhotoPath = ImagePath
        self.Coords = Coords

    def Size(self):
        return self.Im.size

    def FindColour(self, X, Y):
            pix = self.Im.load()
            return pix[X,Y]

    def ReplaceColour(self,X,Y):
            pix = self.Im.load()
            pix[X,Y] = 255,255,255
            self.Im.save('MainProject\Out\Modified.png')

    def FindEdges(self, Coord, Direction):
        Minus = lambda a : int(a) - 15
        Plus = lambda a : int(a) + 15
        if '-X' in Direction and CheckPaths.FindColour(self,Minus(Coord[0]),Coord[1])>(20,20,20):
            return '-X'
        if '+X' in Direction and CheckPaths.FindColour(self,Plus(Coord[0]),Coord[1])>(20,20,20):
                return '+X'
        if '-Y' in Direction and CheckPaths.FindColour(self,Coord[0],Minus(Coord[1]))>(20,20,20):
                return '-Y'
        if '+Y' in Direction and CheckPaths.FindColour(self,Coord[0],Plus(Coord[1]))>(20,20,20):
                return '+Y'
        else: return None
            
    def ClosestDot(self, Coord):
        CP = CheckPaths('MainProject\Out\Lines.tif', self.Coords)
        Directions = ['-X','+X','-Y','+Y']
        FoundWhite = False
        for Direction in Directions:
            if CP.FindEdges(self, Coord, Direction) != None:
                pass #then go untill you hit an intersect
            
            
    def FindClosest(self):
        CP = CheckPaths('MainProject\Out\Lines.tif', self.Coords)
        for Coord in self.Coords:
            CP.ClosestDot(self, Coord)
        
        #myArr[myArr < myNumber].max()
 
if(__name__ == '__main__'):
    sys.exit()