import json
GraphTemp = {    0: [(1, 1)],    1: [(0, 1), (2, 2), (3, 3)],    2: [(1, 2), (3, 1), (4, 5)],    3: [(1, 3), (2, 1), (4, 1)],    4: [(2, 5), (3, 1)]}
json.dump(GraphTemp, open("Coords.txt",'w'))

