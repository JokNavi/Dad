#FUNCTIONS
from configparser import LegacyInterpolation
import math
import re
import sys
import cv2
import numpy as np
import pandas as pd
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
    def Length(self,CoordsOne,CoordsTwo):
        InputOne = re.sub("\'","", str(CoordsOne))
        InputOne = InputOne.split(', ')
        InputTwo = re.sub("\'","", str(CoordsTwo))
        InputTwo = InputTwo.split(', ')
        Length =  (int(InputOne[0]) - int(InputTwo[0]))*-1, (int(InputOne[1]) - int(InputTwo[1]))*-1
        return Length
        
   
       
        

class CheckPaths:
    def __init__(self, ImagePath, Coords):
        self.ImagePath = ImagePath
        self.Coords = Coords

    def Size(self):
        return self.Im.size

    def FindColour(self, X, Y):
            Im = Image.open(self.ImagePath)
            Im = Im.convert("RGB")
            return Im.getpixel((int(X),int(Y)))

    def ReplaceColour(self,X,Y):
            Im = Image.open(self.ImagePath)
            Im.putpixel((int(X),int(Y)),(255, 255, 255))
            Im.save('MainProject\Out\Modified.tif')

    def FindEdges(self, Coord, Direction, Value):
        Coord = re.sub("\'","", str(Coord))
        Coord = re.sub("\"","", str(Coord))
        Minus = lambda a : int(a) - Value
        Plus = lambda a : int(a) + Value
        if '-X' in Direction and CheckPaths.FindColour(self, Minus(int(Coord[0])),int(Coord[1]))>(30,30,30):
            return '-X'
        if '+X' in Direction and CheckPaths.FindColour(self, Plus(int(Coord[0])),int(Coord[1]))>(30,30,30):
                return '+X'
        if '-Y' in Direction and CheckPaths.FindColour(self, int(Coord[0]),Minus(int(Coord[1])))>(30,30,30):
                return '-Y'
        if '+Y' in Direction and CheckPaths.FindColour(self, int(Coord[0]),Plus(int(Coord[1])))>(30,30,30):
                return '+Y'
        else: return None
            
    def ClosestDot(self, CoordSpecific):
        CP = CheckPaths('MainProject\Out\Intersects.tif', self.Coords)
        Directions = ['-X','+X','-Y','+Y']
        Im = Image.open('MainProject\Out\Intersects.tif')
        CoordSpecific = list(CoordSpecific)
        LinkedCoord = []
        for Direction in Directions:
            Looking = CP.FindEdges(CoordSpecific, Direction, 16)
            Coord = CoordSpecific
            if Looking != None:
                print(Looking)
                Minus = lambda a : int(a) - 1
                Plus = lambda a : int(a) + 1
                while True or abs(int(Coord[0])) >= 1000 or abs(int(Coord[1])) >= 1000:
                    pix = Im.load()
                    pix[int(Coord[0]),int(Coord[1])] = 255,255,255
                    if '-X' in Direction: Coord = [Minus(Coord[0]),int(Coord[1])]
                    if '+X' in Direction: Coord = [Plus(Coord[0]),int(Coord[1])]
                    if '-Y' in Direction: Coord = [int(Coord[0]),Minus(Coord[1])]
                    if '+Y' in Direction: Coord = [int(Coord[0]), Plus(Coord[1])]
                    MoveOne = CP.FindColour(int(Coord[0]), int(Coord[1]))
                    Im.save('MainProject\Out\Modified.tif')
                    if abs(int(Coord[0])) >= 1500 or abs(int(Coord[1])) >= 1500: return 'Took too long'
                    if MoveOne >= (255, 20, 20): 
                        LinkedCoord.append(Coord)
                        break
        return LinkedCoord

    def FindClosest(self):
        CP = CheckPaths('MainProject\Out\Intersects.tif', self.Coords)
        LinkedCoord = []
        for Coord in self.Coords:
            print(Coord)
            Coord = re.findall('[0-9]+', str(Coord))
            LinkedCoord.append([Coord, CP.ClosestDot(Coord)])
            print('\n')
        return LinkedCoord

    def FindDistance(self):
        P = Paths()
        CP = CheckPaths('MainProject\Out\Intersects.tif', self.Coords)
        Directions = ['-X','+X','-Y','+Y']
        LinkedCoords = []
        Distances = []
        with open(r'MainProject\Out\LinkedCoords.txt', 'r') as f:
            for line in f:
                RemoveLB = line[:-1]
                LinkedCoords.append(RemoveLB)
        
        for LineTwo in LinkedCoords:
            MainCoords = re.sub("\'","", str(LineTwo))
            MainCoords = re.sub("\"","", str(MainCoords))
            MainCoords = re.findall(r"\'*[0-9]+\'*, \'*[0-9]+\'*", str(LineTwo))
            print(MainCoords)
            for Direction in Directions:
                Looking = CP.FindEdges(MainCoords[0], Direction, 16)
                if Looking != None: break
            Counter = 1
            Lengths = []
            while Counter <= len(MainCoords)-1:
                Length = P.Length(MainCoords[0],MainCoords[Counter])
                print(Length)
                Lengths.append(Length)
                Counter = Counter + 1
            Distances.append(Lengths)
            print('\n')
        return Distances

    def AddToGraph(self, Distances, Coords):
        LinkedCoords = []
        Distances = Distances[0]
        with open(r'MainProject\Out\LinkedCoords.txt', 'r') as f:
            for line in f:
                RemoveLB = line[:-1]
                LinkedCoords.append(RemoveLB)
        G = nx.Graph()
        Counter = 0
        for Line in LinkedCoords:
            Distances = re.findall(r"[0-9]+", str(Distances))
            QuantityZeros = re.findall(r"0", str(Distances))
            for QuantityZeros
            LineCoords = list(re.findall(r"[0-9]+, [0-9]+", str(Line)))
            if isinstance(len(Line)/2, float) == True:
                while Counter <= int(len(Distances)/2)+1:
                    IndexOne = Coords.index(f'[{LineCoords[Counter]}]')
                    IndexTwo = Coords.index(f'[{LineCoords[Counter+1]}]')
                    G.add_edge(str(IndexOne), str(IndexTwo), weight= int(Distances[Counter]))
                    Counter = Counter + 1
                    print('added')
            else:
                while Counter <= len(Line)/2:
                    IndexOne = Coords.index(LineCoords[Counter])
                    IndexTwo = Coords.index(LineCoords[Counter+1])
                    G.add_edge(str(IndexOne), str(IndexTwo), weight=int(Distances[Counter]))
                    Counter = Counter + 1
                    print('added')
        return nx.shortest_path(G, str(0), str(3), weight="weight")
 
if(__name__ == '__main__'):
    sys.exit()