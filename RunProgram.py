from ShortestCalculator import shortestPath
from FindLength import Length
from FindCenterpoint import Center
import igraph as ig
import re

#calculate shortest path
ISPoints = [(0,1), (0,2), (1,3), (2,3), (2,4), (3,5), (4,5)]
PointNumbers = re.findall('[0-9]+', str(ISPoints))
PointOne = str(PointNumbers[0])
PointTwo = str(PointNumbers[1])
f = open('out\CoordsGreenDots.txt')
Length(InputOne,InputTwo)
Weight = [2, 1, 5, 4, 7, 3, 2]
shortestPath(ig.Graph(6,ISPoints),Weight,4)

#visualise
#Center('OnlyGreenPoints.png')


