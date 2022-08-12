import sys
import json
from PIL import Image
from MyFunctions import ImageManipulation, Colours, CheckPaths, Paths

#TESTING
I = ImageManipulation()
#I.Center('MainProject\Out\Intersects.jpg')
I.MakeIntersect()

C = Colours()
#C.RgbToHsv([250,0,4])
#C.HexToRgb('#0000ff')

Im = Image.open('MainProject\Out\IntersectAndLines.jpg')
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

#PROGRAM
'''Dot = 1
Counter = 0
Directions = ['-X','+X','-Y','+Y']
while Counter < 4:
    Facing =  CP.FindEdges(Dot,Directions)
    print(f'Facing: {Facing}')
    if Facing in Directions:
        print(f'Closest Dot: {CP.ClosestDot(Dot,Facing)}')
        Directions.remove(Facing)
    Counter = Counter + 1'''

if (__name__ == '__main__'):
    sys.exit()