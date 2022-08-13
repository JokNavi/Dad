import re
import sys
from PIL import Image
from MyFunctions import CheckPaths, Paths
from ImageStuff import Tracking, ImageManipulation, Intersects

#TESTING
Im = Image.open('MainProject\Out\Lines.jpg')
I = ImageManipulation(Im)
#I.TrackCorners('MainProject\Out\Lines.jpg')
#I.Center('MainProject\Out\Intersects.jpg')

C = Tracking()
Directions = ['-X','+X','-Y','+Y']
Dot = 0
#C.FindEdges(Dot,Directions,Coords)

Im = Image.open('MainProject\Out\Lines.jpg')
CH = CheckPaths(Im)
#print(CH.Size())
#print(CH.FindColour(0,0))
#print(CH.ReplaceColour(0,0))

P = Paths()
##P.ShortestPath(0,3,)

CP = CheckPaths(Im)
Directions = ['-X','+X','-Y','+Y']
Dot = 1
#CP.Size()
#print(CP.FindColour(877,782))
#Facing =  CP.FindEdges(Dot,Directions)
#Axis = CP.ClosestDot(1,Facing)
#print(CP.FindClosest(Facing,Axis))


class MainProgram():
    #PROGRAM
    def Start():
        M = MainProgram()
        I = Intersects()
        
        Img = 'MainProject\Out\Lines.jpg'
        Coords = I.TrackCorners(Img)
        Imag = Image.open('MainProject\Out\Lines.jpg')
        Intersects.append(I.FindIntersect(Imag))

#RUN [(90, 726), (80, 736)]
print(MainProgram.Start())

if (__name__ == '__main__'):
    sys.exit()