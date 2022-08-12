#FUNCTIONS
import sys
import cv2
import math
import json
import imutils
import numpy as np
import networkx as nx
import rhinoscriptsyntax as rs
import matplotlib.pyplot as plt
from PIL import Image  
from skimage.morphology import skeletonize

class Colours():

    def HexToRgb(self,HEX):
        LineColourHex = HEX.lstrip('#')
        Output = list(tuple(int(LineColourHex[i:i+2], 16) for i in (0, 2, 4)))
        print('RGB: ', Output)
        return Output

    def RgbToHsv(self,RGB):
        BGR = np.uint8([[RGB]])
        Output = cv2.cvtColor(BGR,cv2.COLOR_BGR2HSV)
        print (Output)
        return Output

class ImageManipulation():

    def MakeIntersect(self):
        def Binary():
            #Make image binary
            img=cv2.imread('MainProject\Out\Lines.jpg') 
            ImGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
            thresh = 5
            im_bw = cv2.threshold(ImGray, thresh, 255, cv2.THRESH_BINARY)[1]
            ImBinary = np.array(im_bw, dtype=bool)
            return ImBinary

        def Skeletonise(ImBinary):
            # Invert the horse image
            image = ImBinary
            # perform skeletonization
            skeleton = skeletonize(image)
            # display results
            fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
                                    sharex=True, sharey=True)
            ax = axes.ravel()
            ax[0].imshow(image, cmap=plt.cm.gray)
            ax[0].axis('off')
            ax[0].set_title('original', fontsize=20)
            ax[1].imshow(skeleton, cmap=plt.cm.gray)
            ax[1].axis('off')
            ax[1].set_title('skeleton', fontsize=20)
            fig.tight_layout()
            plt.show()
            return skeleton
            
        def HitOrMiss(Skeleton):
            '''input_image = np.array((
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 255, 255, 255, 0, 0, 0, 255],
    [0, 255, 255, 255, 0, 0, 0, 0],
    [0, 255, 255, 255, 0, 255, 0, 0],
    [0, 0, 255, 0, 0, 0, 0, 0],
    [0, 0, 255, 0, 0, 255, 255, 0],
    [0,255, 0, 255, 0, 0, 255, 0],
    [0, 255, 255, 255, 0, 0, 0, 0]), dtype="uint8")'''
            
            Skeleton.astype(int)*255 
            input_image = np.array((Skeleton), dtype="uint8")
            kernel = np.array((
                    [0, 0, 0,],
                    [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0],
                    [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0],), dtype="int")
            output_image = cv2.morphologyEx(input_image, cv2.MORPH_HITMISS, kernel)
            rate = 50
            kernel = (kernel + 1) * 127
            kernel = np.uint8(kernel)
            kernel = cv2.resize(kernel, None, fx = rate, fy = rate, interpolation = cv2.INTER_NEAREST)
            cv2.imshow("kernel", kernel)
            cv2.moveWindow("kernel", 0, 0)
            input_image = cv2.resize(input_image, None, fx = rate, fy = rate, interpolation = cv2.INTER_NEAREST)
            cv2.imshow("Original", input_image)
            cv2.moveWindow("Original", 0, 200)
            output_image = cv2.resize(output_image, None , fx = rate, fy = rate, interpolation = cv2.INTER_NEAREST)
            cv2.imshow("Hit or Miss", output_image)
            cv2.moveWindow("Hit or Miss", 500, 200)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        def GoodTrack(): 
            img = cv2.imread('MainProject\Out\Lines.jpg')
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            corners = cv2.goodFeaturesToTrack(gray,90,0.01,10)
            corners = np.int0(corners)
            for i in corners:
                x,y = i.ravel()
                cv2.circle(img,(x,y),3,255,-1)
            plt.imshow(img),plt.show()
        
        #ImBinary = Binary()
        #Skeleton = Skeletonise(ImBinary)
        #HitOrMiss(Skeleton)
        #GoodTrack()
        def RhinoSol():
            obj = rs.GetObject("Select a line")
            if rs.IsLine(obj):
                print("The object is a line.")
            else:
                print ("The object is not a line.")
        RhinoSol()

    def Center(self, Input):
        # load the image, convert it to grayscale, blur it slightly,
        # and threshold it
        image = cv2.imread(Input)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
        # find contours in the thresholded image
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        # loop over the contours
        SendToFile = {}
        Counter = 0
        n = 2
        for c in cnts:
        # compute the center of the contour
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # draw the contour and center of the shape on the image
            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(image, str(Counter), (cX - 20, cY - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            #SendToFile[Counter]= [[int(cX),int(cY)]]
            SendToFile[Counter]= (int(cX),int(cY))
            Counter = Counter+1
            print(Counter)
        cv2.imshow('image',image)
        cv2.waitKey(0)
        with open('MainProject\Out\CoordsGreenDots.json', 'w') as File:
            File.write(json.dumps(SendToFile))
            File.close()
            return SendToFile
class Paths():  
    def Length(self,InputOne,InputTwo):
        #0,1 | x1, y1
        #1,0 | x2, y2
        #dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        Dist = math.sqrt((int(InputTwo[0]) - int(InputOne[0]))**2 + (int(InputTwo[1]) - int(InputOne[1]))**2) 
        return Dist 
    def ShortestPath(self,Start,End,Nodes):
        G = nx.Graph()
        G.add_edge("0", "1", weight=4)
        G.add_edge("1", "3", weight=2)
        G.add_edge("0", "2", weight=3)
        G.add_edge("2", "3", weight=4)
        return nx.shortest_path(G, str(Start), str(End), weight="weight")

class CheckPaths():
    def __init__(self,Im):
        self.Im = Im

    def Size(self):
        return self.Im.size

    def FindColour(self, X, Y):
            pix = self.Im.load()
            return pix[X,Y]

    def ReplaceColour(self,X,Y):
            pix = self.Im.load()
            pix[X,Y] = 255,255,255
            self.Im.save('MainProject\Out\Modified.png')
    def FindEdges(self, Dot, Check):
        with open('MainProject\Out\CoordsGreenDots.json') as File:
            Coords = json.load(File)
        File.close()
        Coord = Coords[f'{Dot}']
        Minus = lambda a : int(a) - 15
        Plus = lambda a : int(a) + 15
        #Output = (0,0,0)
        if '-X' in Check and CheckPaths.FindColour(self,Minus(Coord[0]),Coord[1])>(20,20,20):
            return '-X'

        if '+X' in Check and CheckPaths.FindColour(self,Plus(Coord[0]),Coord[1])>(20,20,20):
                return '+X'

        if '-Y' in Check and CheckPaths.FindColour(self,Coord[0],Minus(Coord[1]))>(20,20,20):
                return '-Y'

        if '+Y' in Check and CheckPaths.FindColour(self,Coord[0],Plus(Coord[1]))>(20,20,20):
                return '+Y'

        else: return 'None'
            
    def ClosestDot(self, Dot, Facing):
        with open('MainProject\Out\CoordsGreenDots.json') as File:
            Coords = json.load(File)
        File.close()
        Coord = Coords[f'{Dot}']
        #print(Coord)
        FoundGreen = False

        if Facing == '-X':
            Coord[0] = Coord[0] -8
            while FoundGreen == False:
                if  Coord[0] < 0: break
                Coord[0] = Coord[0] -10
                Colour = CheckPaths.FindColour(self,Coord[0],Coord[1])
                if((Colour[1] >240)):
                    FoundGreen = True
                #print(str(Coord[0]))
                CheckPaths.ReplaceColour(self,Coord[0],Coord[1])
                return Coord[0]

        elif Facing == '+X':
            Coord[0] = Coord[0] +8
            while FoundGreen == False:
                if  Coord[0] < 0: break
                Coord[0] = Coord[0] +10
                Colour = CheckPaths.FindColour(self,Coord[0],Coord[1])
                if((Colour[1] >240)):
                    FoundGreen = True
                #print(str(Coord[0]))
                CheckPaths.ReplaceColour(self,Coord[0],Coord[1])
                return Coord[0]

        elif Facing == '-Y':
            Coord[1] = Coord[1] -8
            while FoundGreen == False:
                if  Coord[1] < 0: break
                Coord[1] = Coord[1] -10
                Colour = CheckPaths.FindColour(self,Coord[0],Coord[1])
                if((Colour[1] >240)):
                    FoundGreen = True
                #print(str(Coord[1]))
                CheckPaths.ReplaceColour(self,Coord[0],Coord[1])
                return Coord[1]

        elif Facing == '+Y':
            Coord[1] = Coord[1] +8
            while FoundGreen == False:
                if  Coord[1] < 0: break
                Coord[1] = Coord[1] +10
                Colour = CheckPaths.FindColour(self,Coord[0],Coord[1])
                if((Colour[1] >240)):
                    FoundGreen = True
                #print(str(Coord[1]))
                CheckPaths.ReplaceColour(self,Coord[0],Coord[1])
                return Coord[1]

    def FindClosest(self,Axis,SpecialCoord):
        with open('MainProject\Out\CoordsGreenDots.json') as File:
            Coords = json.load(File)
        
        
        #myArr[myArr < myNumber].max()

 
if(__name__ == '__main__'):
    sys.exit()