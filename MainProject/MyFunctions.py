#FUNCTIONS
import re
import sys
import cv2
import math
import numpy as np
import networkx as nx
from PIL import Image

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
        self.ImagePath = ImagePath
        self.Coords = Coords

    def Size(self):
        return self.Im.size

    def FindColour(self, X, Y):
            Im = Image.open('MainProject\Out\Lines.tif')
            pix = Im.load()
            return pix[int(X),int(Y)]

    def ReplaceColour(self,X,Y):
            Im = Image.open('MainProject\Out\Lines.tif')
            pix = Im.load()
            pix[int(X),int(Y)] = 255,255,255
            Im.save('MainProject\Out\Modified.tif')

    def FindEdges(self, Coord, Direction, Value):
        Minus = lambda a : int(a) - Value
        Plus = lambda a : int(a) + Value
        if '-X' in Direction and CheckPaths.FindColour(self, Minus(Coord[0]),int(Coord[1]))>(30,30,30):
            return '-X'
        if '+X' in Direction and CheckPaths.FindColour(self, Plus(Coord[0]),int(Coord[1]))>(30,30,30):
                return '+X'
        if '-Y' in Direction and CheckPaths.FindColour(self, int(Coord[0]),Minus(Coord[1]))>(30,30,30):
                return '-Y'
        if '+Y' in Direction and CheckPaths.FindColour(self, int(Coord[0]),Plus(Coord[1]))>(30,30,30):
                return '+Y'
        else: return None
            
    def ClosestDot(self, Coord):
        CP = CheckPaths('MainProject\Out\Intersects.tif', self.Coords)
        Directions = ['-X','+X','-Y','+Y']
        Im = Image.open('MainProject\Out\Intersects.tif')
        Coord = list(Coord)
        for Direction in Directions:
            Looking = CP.FindEdges(Coord, Direction, 16)
            if Looking != None:
                print(Looking)
                Minus = lambda a : int(a) - 1
                Plus = lambda a : int(a) + 1
                MoveOne = CP.FindColour(Coord[0], Coord[1])
                while MoveOne <= (250,250,250) or abs(int(Coord[0])) >= 1000 or abs(int(Coord[1])) >= 1000:
                    pix = Im.load()
                    pix[int(Coord[0]),int(Coord[1])] = 255,255,255
                    if '-X' in Direction: Coord = [Minus(Coord[0]),int(Coord[1])]
                    if '+X' in Direction: Coord = [Plus(Coord[0]),int(Coord[1])]
                    if '-Y' in Direction: Coord = [int(Coord[0]),Minus(Coord[1])]
                    if '+Y' in Direction: Coord = [int(Coord[0]), Plus(Coord[1])]
                    MoveOne = CP.FindColour(int(Coord[0]), int(Coord[1]))
                Im.save('MainProject\Out\Modified.jpg')
                return Coord

                
            
    def FindClosest(self):
        CP = CheckPaths('MainProject\Out\Intersects.tif', self.Coords)
        for Coord in self.Coords:
            Coord = re.findall('[0-9]+', str(Coord))
            PointTwo = CP.ClosestDot(Coord)
        
        #myArr[myArr < myNumber].max()
 
if(__name__ == '__main__'):
    sys.exit()