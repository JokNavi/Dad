import re
import sys
from typing_extensions import Self
from PIL import Image
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

    #FUNCTIONS
    def ShowIntersects(self, Coords):
        Dot = 0
        print(len(Coords))
        Points = []
        pix = Im.load()
        while Dot < len(Coords):
            Points.append(I.FindIntersect(Dot))
            Coord = Points[Dot]
            pix[int(Coord[0]),int(Coord[1])] = (255,255,255)
            Dot = Dot + 1
        Im.save(self.ImagePath)
        return Points

    def NewImage(self, Coords):
        CP = CheckPaths(self.ImagePath, Coords)
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
        CoordsCorners = IM.TrackCorners(ImagePath)
        Coords = M.ShowIntersects(CoordsCorners)
        CP = CheckPaths(ImagePath, Coords)
        Coords = re.findall('[[0-9]+, [0-9]+]', str(Coords))
        Coords = [*set(Coords)]
        if NewImage == True:
            M.NewImage(ImagePath , Coords)
            Distances = CP.FindDistance()
            Path =CP.AddToGraph(Distances, Coords)
            print(Path)
        else: 
           Distances =  CP.FindDistance()
           Path = CP.AddToGraph(Distances, Coords)
           print(Path)           

        print('Done')
        #CP.AddToGraph(LinkedCoords)

        
#RUN [(90, 726), (80, 736)
M = MainProgram('MainProject\Out\Lines.tif')
print(M.Start(False))


if (__name__ == '__main__'):
    sys.exit()