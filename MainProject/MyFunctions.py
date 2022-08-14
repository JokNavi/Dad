#FUNCTIONS
import sys
import cv2
import math
import json
import numpy as np
import networkx as nx 

class Colours():

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

class CheckPaths():
    def __init__(self, ImagePath, Coords):
        self.PhotoPath = ImagePath
        self.Coords = Coords

    def __init__(self,Im):
        self.Im = Im

    def Size(self):
        return self.Im.size

    def FindColour(self, X, Y):
            pix = self.Im.load()
            return pix[X,Y]

    def ReplaceColour(self,X,Y):
            pix = self.Im.load()
            pix[X,Y] = 255,255,255
            self.Im.save('MainProject\Out\Modified.png')

    def FindEdges(self, Coord, DirectionsL):
        Minus = lambda a : int(a) - 15
        Plus = lambda a : int(a) + 15
        if '-X' in DirectionsL and CheckPaths.FindColour(self,Minus(Coord[0]),Coord[1])>(20,20,20):
            return '-X'
        if '+X' in DirectionsL and CheckPaths.FindColour(self,Plus(Coord[0]),Coord[1])>(20,20,20):
                return '+X'
        if '-Y' in DirectionsL and CheckPaths.FindColour(self,Coord[0],Minus(Coord[1]))>(20,20,20):
                return '-Y'
        if '+Y' in DirectionsL and CheckPaths.FindColour(self,Coord[0],Plus(Coord[1]))>(20,20,20):
                return '+Y'
        else: return None
            
    def ClosestDot(self, Dot, Facing):
        with open('MainProject\Out\CoordsGreenDots.json') as File:
            Coords = json.load(File)
        File.close()
        Coord = Coords[f'{Dot}']
        #print(Coord)
        FoundGreen = False

        if Facing == '-X':
            Coord[0] = Coord[0] -8
            while FoundGreen == False:
                if  Coord[0] < 0: break
                Coord[0] = Coord[0] -10
                Colour = CheckPaths.FindColour(self,Coord[0],Coord[1])
                if((Colour[1] >240)):
                    FoundGreen = True
                #print(str(Coord[0]))
                CheckPaths.ReplaceColour(self,Coord[0],Coord[1])
                return Coord[0]

        elif Facing == '+X':
            Coord[0] = Coord[0] +8
            while FoundGreen == False:
                if  Coord[0] < 0: break
                Coord[0] = Coord[0] +10
                Colour = CheckPaths.FindColour(self,Coord[0],Coord[1])
                if((Colour[1] >240)):
                    FoundGreen = True
                #print(str(Coord[0]))
                CheckPaths.ReplaceColour(self,Coord[0],Coord[1])
                return Coord[0]

        elif Facing == '-Y':
            Coord[1] = Coord[1] -8
            while FoundGreen == False:
                if  Coord[1] < 0: break
                Coord[1] = Coord[1] -10
                Colour = CheckPaths.FindColour(self,Coord[0],Coord[1])
                if((Colour[1] >240)):
                    FoundGreen = True
                #print(str(Coord[1]))
                CheckPaths.ReplaceColour(self,Coord[0],Coord[1])
                return Coord[1]

        elif Facing == '+Y':
            Coord[1] = Coord[1] +8
            while FoundGreen == False:
                if  Coord[1] < 0: break
                Coord[1] = Coord[1] +10
                Colour = CheckPaths.FindColour(self,Coord[0],Coord[1])
                if((Colour[1] >240)):
                    FoundGreen = True
                #print(str(Coord[1]))
                CheckPaths.ReplaceColour(self,Coord[0],Coord[1])
                return Coord[1]

    def FindClosest(self,Axis,SpecialCoord):
        pass
        
        #myArr[myArr < myNumber].max()
 
if(__name__ == '__main__'):
    sys.exit()