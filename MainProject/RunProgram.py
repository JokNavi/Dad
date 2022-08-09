import igraph as ig
import re
import json
import networkx as nx
from MyFunctions import ShortestPath, Length, Center
import matplotlib.pyplot as plt
#CALCULATE SHORTEST PATH
Goal = 4
AmountOfVert = 4
with open("MainProject\Out\CoordsGreenDots.txt", 'r', encoding='utf-8') as File:
    Coords = json.load(File)
Steps = []
Graph = 'G'
Start = "0"
End = "3"
Steps.append(ShortestPath(Graph, Start, End))
print(Steps)

#plt.show()

#VISUALISE
#Center('MainProject\Out\OnlyGreenPoints.png')