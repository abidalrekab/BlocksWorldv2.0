import json
import os
import uuid
from PathsModule import JsonInputPath
import math
from numpy import *


def LoadData():

    ''''
    This function is to load json file into a python variable.
    inputs : path to the Json file. 
    :return: python data variable.
    '''''
    # specify the data file name.
    JsonFileName = 'data.json'

    # state the path to the data file.
    JsonFilepath = os.path.join(JsonInputPath, JsonFileName)

    try:
        with open(JsonFilepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Check the file path')


def SaveData(data):
    JsonFileName1 = 'data1.json'  # modified data file name.
    JsonFilepath1 = os.path.join(JsonInputPath, JsonFileName1)

    try:
        with open(JsonFilepath1, 'w') as f:
            json.dump(data, f, indent=2, sort_keys=True)
    except FileNotFoundError:
        print("couldn't save the file")


def GetNrShapesInAggr(data):
    ''''
    This function is to obtain:
        -   Number of objects within the aggregate object
        -   Number of layers in the data set.
    '''''

    # get the number of layers
    NrOfLayers = len(data.keys())

    # initialize the number of shapes in an aggregate object to an empty list
    NrOfShapesAggr = []
    for key, values in data.items():
        NrOfShapesAggr.append(len(values[0]["Aggobjects"]))
    return NrOfShapesAggr, NrOfLayers


def GetBasicObjectInfo(data):
    '''

    :param data:
    :return: for each an Aggregate object it returns centers, Radii, number of vertices, and orientation
    for all basic shapes that consist of. for example:
    [[[20,10],[20,40]],[[20,10],[30,10]]] this means that we have two aggregate objects each has two basic shapes.
    
    '''''

    Aggrcenters = []                            # a list of centers for all shapes in all aggregate objects.
    Aggrradii = []                              # a list of radii for all shapes in all aggregate objects.
    AggrnrVertices = []                         # a list of vertices for all shapes in all aggregate objects.
    Aggrorientation = []                        # a list of orientation for all shapes in all aggregate objects.
    for key, values in data.items():
        centers = []
        radii = []
        nrNodes = []
        orientation = []
        # using get method to get key's values to avoid throwing errors.
        for index, object in enumerate(values[0].get("AggrObjects")):
            centers.append(object.get("center"))
            radii.append(object.get("radii"))
            nrNodes.append(object.get("nrVertices"))
            orientation.append(object.get("orientation"))
        Aggrcenters.append(centers)
        Aggrradii.append(radii)
        AggrnrVertices.append(nrNodes)
        Aggrorientation.append(orientation)
    return array(Aggrcenters), array(Aggrradii), array(AggrnrVertices), array(Aggrorientation)


def createNewObject(name, layer, center, radii = 10, nrVertices = 4, rotation = 45):
    return data[layer][0]["AggrObjects"].append({ 'GUID': name, 'center': center, 'radii': radii, 'nrVertices':nrVertices, 'orientation': rotation})


def DelObject(name):
    for key, values in data.items():
        listOfitems = values[0]['AggrObjects']
        for i in range(len(listOfitems)):
            print(i)
            if listOfitems[i]['GUID'] == name:
                print(listOfitems[i])
                del listOfitems[i]
                break


def Object2points(data):
    Vertices = []            # the location of all vertices for all aggregate objects
    for key, values in data.items():

        Aggrpoints = []      # the number of vertices for a single aggregate object.

        for object in values[0]["AggrObjects"]:
            center = object["center"]
            size = object["radii"]
            nrVertices = object["nrVertices"]
            OriAngle = object["orientation"]
            points = []
            x = center[0]
            y = center[1]

            radius = size / 2.0

            x0 = round(x + radius)
            y0 = y
            points.append([x0, y0])

            segment = 2 * math.pi / nrVertices

            # (xi - x)^2 + (yi - y)^2 = radius^2
            for i in range(nrVertices - 1):
                angle = (i + 1) * segment

                xi = round(radius * math.cos(angle) + x)
                yi = round(radius * math.sin(angle) + y)
                points.append([xi, yi])
            # print(points)

            output = []
            radAngle = (OriAngle / 360.0) * 2.0 * math.pi
            c = math.cos(radAngle)
            s = math.sin(radAngle)
            #
            for point in points:
                x = point[0] - center[0]
                y = point[1] - center[1]
                xr = round(x * c - y * s + center[0])
                yr = round(x * s + y * c + center[1])
                output.append([xr, yr])
                # print(output)
                Aggrpoints.append([xr, yr])
            object['points'] = output
        Vertices.append(Aggrpoints)

    return asarray(Vertices)


def AggregateCentroide(vertexes):
    centroid = []
    for object in vertexes:
        _x_list = [vertex[0] for vertex in vertexes]
        _y_list = [vertex[1] for vertex in vertexes]
        _len = len(vertexes)
        _x = sum(_x_list) / _len
        _y = sum(_y_list) / _len
        centroid.append(array([_x, _y]).round())
    return centroid


def UpdateNames(data):
    for key, values in data.items():
        # using get method to get key's values to aviod throwing errors.
        for index, object in enumerate(values[0].get("AggrObjects")):
            object["GUID"] = 'object-' + str(uuid.uuid4())


def AggregateRotation(points, centroids, angle):
    # assuming that we have only two layers
    # translate the points to the origin
    for index, centroid in enumerate(centroids):
        tx = centroid[0]
        ty = centroid[1]
        print("{},{}".format(tx,ty))
        OriAngle = angle[index]
        radAngle = (OriAngle / 360.0) * 2.0 * math.pi

        rotationMatrix = array([[math.cos(radAngle), - math.sin(radAngle), 0], [math.sin(radAngle), math.cos(radAngle), 0], [0, 0, 1]])
        translationMatrix1 = array([[1, 0, -tx], [0, 1, -ty], [0, 0, 1]])
        translationMatrix2 = array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
        for vert in points[index]:
            print("the point before rotation", hstack((vert, 1)))
            w_translation = dot(translationMatrix1, hstack((vert, 1)))
            w_rotation = dot(rotationMatrix,w_translation)
            w_final = dot(translationMatrix2 , w_rotation).round()
            print("the point after rotation", w_final)

def AggregateScaling(points, centroids, scale = array([1,1])):
    # assuming that we have only two layers
    # translate the points to the origin
    for index, centroid in enumerate(centroids):
        tx = centroid[0]
        ty = centroid[1]
        print("{},{}".format(tx, ty))
        Sx = scale[0]
        Sy = scale[1]
        ScaleMatrix = array([[Sx,0,0],[0,Sy,0],[0,0,1]])
        translationMatrix1 = array([[1, 0, -tx], [0, 1, -ty], [0, 0, 1]])
        translationMatrix2 = array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])

        for vert in points[index]:
            print("the point before scaling", hstack((vert, 1)))
            w_translation = dot(translationMatrix1, hstack((vert, 1)))
            w_scale = dot(ScaleMatrix, w_translation)
            w_final = dot(translationMatrix2, w_scale).round()
            print("the point after scaling", w_final)


def AggregateTranslate(points, centroids, distance = array([1,1])):
    # assuming that we have only two layers
    # translate the points to the origin
    for index, centroid in enumerate(centroids):
        tx = centroid[0]
        ty = centroid[1]
        print("{},{}".format(tx, ty))
        Tx = distance[0]
        Ty = distance[1]
        TranslationMatrix = array([[1, 0, Tx], [0, 1, Ty], [0, 0, 1]])
        translationMatrix1 = array([[1, 0, -tx], [0, 1, -ty], [0, 0, 1]])
        translationMatrix2 = array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
        for vert in points[index]:
            print("the point before Translation", hstack((vert, 1)))
            w_translation = dot(translationMatrix1, hstack((vert, 1)))
            w_transl = dot(TranslationMatrix, w_translation)
            w_final = round(dot(translationMatrix2, w_transl))
            print("the point after Translation", w_final)

