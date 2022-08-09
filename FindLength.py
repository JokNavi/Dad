import math
def Length(InputOne,InputTwo):
    #0,1 | x1, y1
    #1,0 | x2, y2
    dist = math.sqrt((int(InputTwo[2]) - int(InputOne[2]))**2 + (int(InputTwo[7]) - int(InputOne[7]))**2)
    #dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(dist)