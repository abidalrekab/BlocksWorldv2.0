import random
from PathsModule import AggregateOutputPath
import os
import uuid
from getImage import getImage
from GenerateAdjecentShapesPoints import GenerateAdjecentShapesPoints
from blocksWorld import drawSolid, drawWire, draw
from CreateNewObject import CreateNewObject
from SaveData import Save
from VehicleProfile import Rectangle, Circle, Square, Triangle, Sedean, SUV1, SUV2, Wagen, train, Bicycle

# Function to convert number into string
# Switcher is dictionary data type here
def Choose_from_Profile(argument, Parameters):
    Distortion = Parameters[0]
    missing = Parameters[1]
    scale = Parameters[2]/10
    rotation = Parameters[3]
    switcherFunctions = {
        0: Sedean( Distortion, missing, scale, rotation),
        1: SUV1(   Distortion, missing, scale, rotation),
        2: SUV2(   Distortion, missing, scale, rotation),
        3: Wagen(  Distortion, missing, scale, rotation),
        4: train(  Distortion, missing, scale, rotation),
        5: Bicycle(Distortion, missing, scale, rotation)
    }
    switcherName = {
        0: 'Sedean',
        1: 'SUV1',
        2: 'SUV2',
        3: 'Wagen',
        4: 'train',
        5: 'Bicycle'
    }
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcherFunctions.get(argument, "nothing"), switcherName.get(argument, "nothing")

if __name__ == "__main__":
    # The main program parameters
    NumberOfImages = 100                              # the number of images you want [0-100000]
    colors = ['red', 'blue', 'black', 'yellow', 'green', 'red', 'blue', 'black', 'yellow', 'green']     # choose a set of colors that gonna be used
    # create output directory
    if not os.path.exists(AggregateOutputPath):
        os.makedirs(AggregateOutputPath)
    # Generate N images and save their information into json file that has the same name as image file

    for idx in range(NumberOfImages + 1):
        tag = 'Image(' + str(idx) + ')'+ str(uuid.uuid4())
        imageName = tag + '.png'
        jsonfile = tag + '.txt'
        print("Creating Image Number {} of {}".format(idx,NumberOfImages))
        resultFile = os.path.join(AggregateOutputPath, imageName)
        image, canvas = getImage('RGB', (640, 480), 'white')
        #Parameters = [random.choice(['True', 'False']),random.choice(['True', 'False']), random.choice(range(5, 20)), random.choice(range(0,90,5) )]
        Parameters = ['True', 'False',random.choice(range(5, 20)), random.choice(range(0,90,5) )]
        #Choice = random.choice(range(0,6))
        Choice = 5
        Ver, FunName = Choose_from_Profile(Choice, Parameters)
        print(FunName)
        data = {'ImageTag':[{"File Name": FunName, "AggCenter": [], "Gap": Parameters[0], "Missing" : Parameters[1], "Scale": Parameters[2]/10, "orientation": Parameters[3], "Vertices": Ver}]}
        for idx, points in enumerate(Ver):
            drawSolid(canvas, points, colors[idx])
        ObjectName = 'object_' + str(00)
        image.save(resultFile)
        Save(data, jsonfile)



