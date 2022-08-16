import re
import sys
from PIL import Image
import networkx as nx
from MyFunctions import CheckPaths, Paths
from ImageStuff import Tracking, ImageManipulation, Intersects

#TESTING
Im = Image.open('MainProject\Out\Lines.tif')
I = Intersects('MainProject\Out\Lines.tif')
'''Coords = IM.TrackCorners('MainProject\Out\Lines.tif')
Dot = 0
while Dot < 64:
    CoordSpecific = Coords[Dot]
    CoordSpecific = re.findall('[0-9]+', str(CoordSpecific))
    IM.ReplaceColour(CoordSpecific[0], CoordSpecific[1], (255,255,255), 'MainProject\Out\Corners.tif')
    Dot = Dot + 1'''

class MainProgram():
    def __init__(self, ImagePath):
        self.ImagePath = ImagePath
        Coords = []
        with open('MainProject/Out/Coords.txt', 'r') as f:
            for line in f:
                RemoveLB = line[:-1]
                Coords.append(RemoveLB)
        self.Coords = Coords

    #FUNCTIONS
    def ShowIntersects(self, Coords):
        ImagePath = self.ImagePath
        Dot = 0
        print(len(Coords))
        Points = []
        pix = Im.load()
        while Dot < len(Coords):
            Points.append(I.FindIntersect(Dot))
            Coord = Points[Dot]
            pix[int(Coord[0]),int(Coord[1])] = (255,255,255)
            Dot = Dot + 1
        Im.save(ImagePath)
        return Points

    def NewImage(self):
        CP = CheckPaths(self.ImagePath)
        LinkedCoords = CP.FindClosest()
        with open(r'MainProject\Out\LinkedCoords.txt', 'w') as f:
            for LinkedCoord in LinkedCoords:
                f.write(f'{LinkedCoord}\n')

    #PROGRAM
    def Start(self, NewImage):
        ImagePath = self.ImagePath
        Im = Image.open(ImagePath)
        M = MainProgram(ImagePath)
        IM = ImageManipulation(ImagePath)
        if NewImage == 'True':
            CoordsCorners = IM.TrackCorners(ImagePath)
            Coords = M.ShowIntersects(CoordsCorners)
            Coords = re.findall('[[0-9]+, [0-9]+]', str(Coords))
            Coords = [*set(Coords)]
            with open('MainProject/Out/Coords.txt', 'w') as f:
                for Coord in Coords:
                    f.write(f'{Coord}\n')
            CP = CheckPaths(ImagePath)
            M.NewImage()
            Distances = CP.FindDistance()
            Path =CP.AddToGraph(Distances)
            print(Path)
        else:
            CP = CheckPaths(ImagePath)
            Distances =  CP.FindDistance()
            G = CP.AddToGraph(Distances)
            nx.shortest_path(G, str(0), str(3), weight="weight")
            print(Path)           

        print('Done')
        #CP.AddToGraph(LinkedCoords)

        
#RUN [(90, 726), (80, 736)
M = MainProgram('MainProject\Out\Lines.tif')
print(M.Start('True'))


if (__name__ == '__main__'):
    sys.exit()