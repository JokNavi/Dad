# Python3 code to demonstrate
# convert dictionary string to dictionary
# using json.loads()
import json
from ast import literal_eval

SendToFile = {"1" : ["John"], "2":[36]}
f = 3
x = 1
FXold = [[int(f),int(x)]]
f = 9
x = 8
FX = FXold +  [[int(f),int(x)]]
FXold = [[int(f),int(x)]]
#guests = ['1', tuple(FX)]
f = 50
x = 96
FX = FXold + [[int(f),int(x)]]
FXold = int(f),int(x)
#guests = ['1', tuple(FX)]
SendToFile.update({'1':tuple(FX)})
print(SendToFile)
json.dump(SendToFile, open("out/CoordsTest.json",'w'))

# using json.loads()
# convert dictionary string to dictionary
with open('out/CoordsTest.json') as f:
    data = f.read()
    data = json.loads(data)
# print result
print(data)

