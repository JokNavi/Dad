import sys
from PIL import Image
from MyFunctions import CheckPaths, Paths
from ImageStuff import Tracking, ImageManipulation, Intersects

#TESTING
Im = Image.open('MainProject\Out\Lines.tif')
IM = ImageManipulation(Im)
#I.TrackCorners('MainProject\Out\Lines.jpg')
#I.Center('MainProject\Out\Intersects.jpg')

C = Tracking(Im)
Directions = ['-X','+X','-Y','+Y']
Dot = 1
#C.FindEdges(Dot,Directions,Coords)

Im = Image.open('MainProject\Out\Lines.tif')
#CH = CheckPaths(Im)
#print(CH.Size())
#print(CH.FindColour(0,0))
#print(CH.ReplaceColour(0,0))

P = Paths()
##P.ShortestPath(0,3,))

#CP = CheckPaths(Im)
Directions = ['-X','+X','-Y','+Y']
Dot = 0
#CP.Size()
#print(CP.FindColour(877,782))
#Facing =  CP.FindEdges(Dot,Directions)
#Axis = CP.ClosestDot(1,Facing)
#print(CP.FindClosest(Facing,Axis))

I = Intersects('MainProject\Out\Lines.tif')
'''Coords = IM.TrackCorners('MainProject\Out\Lines.tif')
Dot = 0
while Dot < 64:
    CoordSpecific = Coords[Dot]
    CoordSpecific = re.findall('[0-9]+', str(CoordSpecific))
    IM.ReplaceColour(CoordSpecific[0], CoordSpecific[1], (255,255,255), 'MainProject\Out\Corners.tif')
    Dot = Dot + 1'''

class MainProgram():
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
        Im.save('MainProject\Out\Intersects.tif')

    #PROGRAM
    def Start():
        Im = Image.open('MainProject\Out\Lines.tif')
        I = Intersects('MainProject\Out\Lines.tif')
        M = MainProgram()
        IM = ImageManipulation(Im)
        Coords = IM.TrackCorners('MainProject\Out\Lines.tif')
        M.ShowIntersects(Coords)
        CP = CheckPaths('MainProject\Out\Lines.tif', Coords)
        CP.FindClosest(Axis,SpecialCoord)
        #CP.FindClosest()

        
#RUN [(90, 726), (80, 736)
print(MainProgram.Start())


if (__name__ == '__main__'):
    sys.exit()