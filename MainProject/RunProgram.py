import igraph as ig
import re
import json
from MyFunctions import ShortestPath, Length, Center

#CALCULATE SHORTEST PATH
ISPoints = [(0,1), (0,2), (1,3), (2,3), (2,4), (3,5), (4,5)]
PointNumbers = re.findall('[0-9]+', str(ISPoints))
PointOne = int(PointNumbers[0])
PointTwo = int(PointNumbers[1])
with open("MainProject\Out\CoordsGreenDots.txt", 'r', encoding='utf-8') as File:
    Coords = json.load(File)
Weights = []
for Point in ISPoints:
    Weights.append(Length(Coords[str(PointOne)],Coords[str(PointTwo)]))
    print(Weights)
#Weight = [2, 1, 5, 4, 7, 3, 2]
ShortestPath(ig.Graph(6,ISPoints),Weights,5)

#VISUALISE
#Center('MainProject\Out\OnlyGreenPoints.png')

