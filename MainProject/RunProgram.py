import igraph as ig
import re
import json
from MyFunctions import ShortestPath, Length, Center

#CALCULATE SHORTEST PATH
ISPoints = [(0,1), (0,2), (1,3), (2,3), (2,4), (3,5), (4,5)]
PointNumbers = re.findall('[0-9]+', str(ISPoints))
PointOne = str(PointNumbers[0])
PointTwo = str(PointNumbers[1])
with open("MainProject\Out\CoordsGreenDots.txt", 'r', encoding='utf-8') as File:
    Coords = json.load(File)
CoordNumbers = re.findall('[0-9]+', str(Coords))
Length(Coords[0],Coords[0])
Weight = [2, 1, 5, 4, 7, 3, 2]
#ShortestPath(ig.Graph(6,ISPoints),Weight,4)

#VISUALISE
#Center('MainProject\Out\OnlyGreenPoints.png')

