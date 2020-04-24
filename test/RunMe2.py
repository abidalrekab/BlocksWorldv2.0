import random
from PathsModule import AggregateOutputPath
import os
import uuid
from getImage import getImage
from GenerateAdjecentShapesPoints import GenerateAdjecentShapesPoints
from blocksWorld import drawSolid
from CreateNewObject import CreateNewObject
from SaveData import Save
from VehicleProfile import Rectangle
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
        AggpointsShape = Rectangle(center, 50, 20, OriAngle)
        for idy, points in enumerate(AggpointsShape):
            color = random.choice(colors)
            drawSolid(canvas, points, color)
            ObjectName = 'object_' + str(idy)
            # for i in range(len(points) - 1):
            #     draw(canvas, (points[i + 0], points[i + 1]), str(i))
            # for i in range(len(c) - 1):
            #     draw(canvas, (c[i + 0], c[i + 1]), str(i))
        image.save(resultFile)
        Save(data, jsonfile)



