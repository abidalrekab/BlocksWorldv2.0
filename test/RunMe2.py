import random
from PathsModule import AggregateOutputPath
import os
import uuid
from getImage import getImage
from GenerateAdjecentShapesPoints import GenerateAdjecentShapesPoints
from blocksWorld import drawSolid, drawWire, draw
from CreateNewObject import CreateNewObject
from SaveData import Save
from VehicleProfile import Rectangle, Circle, Square, Triangle, Sedean, SUV
if __name__ == "__main__":
    # The main program parameters
    NumberOfImages = 1                              # the number of images you want [0-100000]
    colors = ['red', 'blue', 'black', 'yellow']     # choose a set of colors that gonna be used
    # create output directory
    if not os.path.exists(AggregateOutputPath):
        os.makedirs(AggregateOutputPath)
    # Generate N images and save their information into json file that has the same name as image file
    OriAngle = random.randint(0, 90)
    center = [random.randint(300, 340), random.randint(220, 260)]
    for idx in range(NumberOfImages):
        tag = 'Image(' + str(idx) + ')'+ str(uuid.uuid4())
        imageName = tag + '.png'
        jsonfile = tag
        print("Creating Image Number {} of {}".format(idx,NumberOfImages))
        data = {'layer0':[{"AggregateObjectName":tag, "AggCenter" : [], "AggrObjects":[],
          "orientation": 0}]}
        resultFile = os.path.join(AggregateOutputPath, imageName)
        image, canvas = getImage('RGB', (640, 480), 'white')
        Ver = Sedean(gap='True',missing='False', scale= 1, rotation= 45)
        #Ver = SUV(gap='False',missing='False', scale= 1, rotation= 0)
        #points = Rectangle([120,100], 150, 120, 0)
        #points = Circle([120,100], 50)
        #print(points)
        #drawWire(canvas, points)
        for points in Ver:
            i = random.randint(0,3)
            drawSolid(canvas, points, colors[i])
        ObjectName = 'object_' + str(00)
        image.save(resultFile)
        Save(data, jsonfile)



