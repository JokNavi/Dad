import sys
import json
from PIL import Image
from MyFunctions import ImageManipulation, Colours, CheckPaths, Paths

#CALCULATE SHORTEST PATH
with open("MainProject\Out\CoordsGreenDots.txt", 'r', encoding='utf-8') as File:
    Coords = json.load(File)

I = ImageManipulation()
#I.Mask('MainProject\Out\GreenAndRed.png','ff0000')
#I.Center('MainProject\Out\OnlyGreenPoints.png')

C = Colours()
#C.RgbToHsv([255,0,0])
#C.HexToRgb('#ff0000')

Im = Image.open('MainProject\Out\LinesOnlyBlack.png')
CH = CheckPaths(Im)
CH.ReplaceColour(0,0)
CH.FindColour(0,0)

if (__name__ == '__main__'):
    sys.exit()