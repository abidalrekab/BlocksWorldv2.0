import json
import uuid
from numpy import *
from blocksWorld import *
from PathsModule import JsonInputPath
from PathsModule import AggregateOutputPath
from PathsModule import getImage
import os


class CreateDataSet():
    def __init__(self):
        self.AggregateOutputPath = AggregateOutputPath
        self.path = JsonInputPath
        self.data = self.LoadDefaultData()
        self.UpdateNames()
        self.NrOfShapesAggr, self.NrOfLayers, self.AggregateShapeNames = self.AggregateObjectParameters()
        self.Vertices = self.CalculateVertices()
        self.Aggrcenters, self.Aggrradii, self.AggrnrVertices,self.Aggrorientation, self.AggrNames, self.AggrVertices  = self.GetBasicObjectInfo()
        self.centroid = self.AggregateCentroide()

    def LoadDefaultData(self):

        ''''
        This function is to load json file into a python variable.
        inputs : path to the Json file. 
        :return: python data variable.
        '''''
        # specify the data file name.
        JsonFileName = 'data.json'

        # state the path to the data file.
        JsonFilepath = os.path.join(self.path, JsonFileName)

        try:
            with open(JsonFilepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print('Check the file path')

    def SaveData(self, FileName):
        '''
            This function saves all data into a Json file to be used later to generate an exact replica to data set.
        :return:
            Nothing
        '''

        JsonFileName1 = FileName  # modified data file name.
        JsonFilepath1 = os.path.join(JsonInputPath, JsonFileName1)

        try:
            with open(JsonFilepath1, 'w') as f:
                json.dump(self.data, f, indent=2, sort_keys=True)
        except FileNotFoundError:
            print("couldn't save the file")
        return 'done!'

    def LoadExistingData(self, FileName):
        # specify the data file name.
        JsonFileName = FileName

        # state the path to the data file.
        JsonFilepath = os.path.join(self.path, JsonFileName)

        try:
            with open(JsonFilepath, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print('Check the file path')

    def AggregateObjectParameters(self):
        '''
        This function to return basic information about the aggregate object.
        :return
        This function is to obtain:
            -   Number of objects within the aggregate object
            -   Number of layers in the data set.
        '''

        # get the number of layers
        NrOfLayers = len(self.data.keys())

        # initialize the number of shapes in an aggregate object to an empty list
        NrOfShapesAggr = []
        AggregateShapeNames = []
        for key, values in self.data.items():
            NrOfShapesAggr.append(len(values[0]["AggrObjects"]))
            AggregateShapeNames.append(values[0]["AggregateObjectName"])
        return NrOfShapesAggr, NrOfLayers, AggregateShapeNames


    def GetBasicObjectInfo(self):
        '''
        :input
            data
        :return:
            for each an Aggregate object it returns centers, Radii, number of vertices, and orientation
            for all basic shapes that consist of. for example:
            [[[20,10],[20,40]],[[20,10],[30,10]]] this means that we have two aggregate objects each has two basic shapes.

        '''

        Aggrcenters = []                    # a list of centers for all shapes in all aggregate objects.
        Aggrradii = []                      # a list of radii for all shapes in all aggregate objects.
        AggrnrVertices = []                 # a list of vertices for all shapes in all aggregate objects.
        Aggrorientation = []                # a list of orientation for all shapes in all aggregate objects.
        AggrNames = []                      # a list of names for all shapes in every aggregsate objects.
        AggrVertices = []                   # a list of vertices ....
        for key, values in self.data.items():
            centers = []
            radii = []
            nrNodes = []
            orientation = []
            Names = []
            vertex = []
            # using get method to get key's values to avoid throwing errors.
            for index, object in enumerate(values[0].get("AggrObjects")):
                centers.append(object.get("center"))
                radii.append(object.get("radii"))
                nrNodes.append(object.get("nrVertices"))
                orientation.append(object.get("orientation"))
                Names.append(object.get("GUID"))
                vertex.append(object.get("Vertices"))
            Aggrcenters.append(centers)
            Aggrradii.append(radii)
            AggrnrVertices.append(nrNodes)
            Aggrorientation.append(orientation)
            AggrNames.append(Names)
            AggrVertices.append(vertex)
        return array(Aggrcenters), array(Aggrradii), array(AggrnrVertices), array(
            Aggrorientation), AggrNames, AggrVertices

    def createNewObject(self, name, layer, center, radii=10, nrVertices=4, rotation=45):
        return self.data[layer][0]["AggrObjects"].append(
            {'GUID': name, 'center': center, 'radii': radii, 'nrVertices': nrVertices, 'orientation': rotation})

    def DelObject(self, name):
        for key, values in self.data.items():
            listOfitems = values[0]['AggrObjects']
            for i in range(len(listOfitems)):
                print(i)
                if listOfitems[i]['GUID'] == name:
                    print(listOfitems[i])
                    del listOfitems[i]
                    break

    def CalculateVertices(self):
        Vertices = []                               # the location of all vertices for all aggregate objects
        for key, values in self.data.items():

            Aggrpoints = []                         # the number of vertices for a single aggregate object.

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
                object['Vertices'] = output
            Vertices.append(Aggrpoints)
        return list(Vertices)

    def Updatecenters(self):
        for key, value in self.data.items():
            for element in value[0]['AggrObjects']:
                xlist = [Center[0] for Center in element['Vertices']]
                ylist = [Center[1] for Center in element['Vertices']]
                nr = len(xlist)
                x = sum(xlist) / nr
                y = sum(ylist) / nr
                element['center'] = [x, y]



    def UpdateVertices(self):

        Vertices = self.NewVertices                            # the location of all vertices for all aggregate objects
        indicator = self.AggrnrVertices
        temp = []
        for idx, (key, values) in enumerate(self.data.items()):
            start = 0
            temp.append([])
            for idy, object in enumerate(values[0]["AggrObjects"]):
                offset = indicator[idx][idy]
                end = start + offset
                object['Vertices'] = Vertices[idx][start:end]
                print(Vertices[idx][start:end])
                temp[idx].append(Vertices[idx][start:end])
                start = end
        self.AggrVertices = temp
        self.Vertices = Vertices


    def AggregateCentroide(self):
        '''
        This function is to calculate centroid of an Aggregate object based on how many basic shapes there are.
        input:
            A list of vertices of each aggregate object in the form of :
                [[ all vertices of first Aggregate obj], [...second], [Third..]]
            if we assume that we have more than one layer because each layer has only one aggregate object.
        :return:
            a list of centers coordinates in form of :
            [[Cx1,Cy1],[Cx2,Cy2],[Cx3,Cy3],....]
        Note: These centers are used to perform all actions on the aggregate object: rotation, scaling, and translation
        '''
        centroid = []
        # here we calculate the center by averaging x-coordinates, and y-coordinates
        for element in self.Vertices:
            _x_list = [vertex[0] for vertex in element]
            _y_list = [vertex[1] for vertex in element]
            _len = len(_x_list)
            _x = sum(_x_list) / _len
            _y = sum(_y_list) / _len
            centroid.append(array([_x, _y]).round())

        # This part is to store centers into its prospective aggregate objects.
        for idx in range(len(self.Vertices)):
            layerName = 'layer' + str(idx)
            self.data[layerName][0]["AggCenter"] = list(centroid[idx])
        return centroid


    def UpdateNames(self):
        for key, values in self.data.items():
            # using get method to get key's values to aviod throwing errors.
            for index, object in enumerate(values[0].get("AggrObjects")):
                object["GUID"] = 'object-' + str(uuid.uuid4())


    def AggregateRotation(self, angle):
        # assuming that we have only two layers
        # translate the points to the origin
        self.NewVertices = []
        for index, centr in enumerate(self.centroid):
            tx = centr[0]
            ty = centr[1]
            #print("{},{}".format(tx, ty))
            OriAngle = angle[index]
            radAngle = (OriAngle / 360.0) * 2.0 * math.pi
            rotationMatrix = array(
                [[math.cos(radAngle), - math.sin(radAngle), 0], [math.sin(radAngle), math.cos(radAngle), 0], [0, 0, 1]])
            translationMatrix1 = array([[1, 0, -tx], [0, 1, -ty], [0, 0, 1]])
            translationMatrix2 = array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
            NewAggrVertices = []
            for vert in self.Vertices[index]:
                #print("the point before rotation", hstack((vert, 1)))
                w_translation = dot(translationMatrix1, hstack((vert, 1)))
                w_rotation = dot(rotationMatrix, w_translation)
                w_final = dot(translationMatrix2, w_rotation).round()
                #print("the point after rotation", w_final)
                NewAggrVertices.append(list(w_final[0:2]))
            self.NewVertices.append(NewAggrVertices)

    def AggregateScaling(self, scale=array([1, 1])):
        # assuming that we have only two layers
        # translate the points to the origin
        self.NewVertices = []
        for index, centroid in enumerate(self.centroid):
            tx = centroid[0]
            ty = centroid[1]
            print("{},{}".format(tx, ty))
            Sx = scale[0]
            Sy = scale[1]
            ScaleMatrix = array([[Sx, 0, 0], [0, Sy, 0], [0, 0, 1]])
            translationMatrix1 = array([[1, 0, -tx], [0, 1, -ty], [0, 0, 1]])
            translationMatrix2 = array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
            NewAggrVertices = []

            for vert in self.Vertices[index]:
                print("the point before scaling", hstack((vert, 1)))
                w_translation = dot(translationMatrix1, hstack((vert, 1)))
                w_scale = dot(ScaleMatrix, w_translation)
                w_final = dot(translationMatrix2, w_scale).round()
                print("the point after scaling", w_final)
                NewAggrVertices.append(list(w_final[0:2]))
            self.NewVertices.append(NewAggrVertices)


    def AggregateTranslate(self, distance=[1, 1]):
        # assuming that we have only two layers
        # translate the points to the origin
        self.NewVertices = []

        for index, centroid in enumerate(self.centroid):
            tx = centroid[0]
            ty = centroid[1]
            print("{},{}".format(tx, ty))
            Tx = distance[0]
            Ty = distance[1]
            TranslationMatrix = array([[1, 0, Tx], [0, 1, Ty], [0, 0, 1]])
            translationMatrix1 = array([[1, 0, -tx], [0, 1, -ty], [0, 0, 1]])
            translationMatrix2 = array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
            NewAggrVertices = []

            for vert in self.Vertices[index]:

                #print("the point before Translation", hstack((vert, 1)))
                w_translation = dot(translationMatrix1, hstack((vert, 1)))
                w_transl = dot(TranslationMatrix, w_translation)
                w_final = dot(translationMatrix2, w_transl).round()
                #print("the point after Translation", w_final)
                NewAggrVertices.append(list(w_final[0:2]))
            self.NewVertices.append(NewAggrVertices)


    @property
    def DisplayInformation(self):
        for i in range(self.NrOfLayers):
            print(
                "-----------------------------------------------------------------------{}--------------------------------------------------".format(
                    self.AggregateShapeNames[i]))
            print(
                '------ shape Name ------------------------------ Nr vertices ------ Radii ---- Center ---- orientation ----- vertices -------------------')
            for j in range(self.NrOfShapesAggr[i]):
                print('----- {} ----- {} ----------- {} ----- {} ----- {} ----- {} -----'.format(self.AggrNames[i][j],
                                                                                                 self.AggrnrVertices[i][j],
                                                                                                 self.Aggrradii[i][j],
                                                                                                 self.Aggrcenters[i][j],
                                                                                                 self.Aggrorientation[i][j],
                                                                                                 self.AggrVertices[i][j]))
            print("____ Centroid ________ = {}".format(self.centroid[i]))
            print("____ rotation ________ = {}".format(0))
            print("____ Translation _____ = {}".format(0))
            print("____ Scaling _________ = {}".format(1))
        return 0

    def DisplayImage(self, saveImage = 'False', showImage = 'False'):
        if not os.path.exists(self.AggregateOutputPath):
            os.makedirs(self.AggregateOutputPath)
        imageName = 'Aggregate-'+ str(uuid.uuid4()) + '.png'
        resultFile = os.path.join(self.AggregateOutputPath, imageName)
        image, canvas = getImage('L', (640, 480), 'white')
        for i in range(self.NrOfShapesAggr[0]):
            points = self.AggrVertices[0][i]
            drawWire(canvas, points)
        if saveImage == 'True':
            image.save(resultFile)
            print("Image has been saved to directory /test/Aggregate ")
        else:
            print("Image hasn't been saved")

        if showImage == 'True':
            image.show()
        else:
            print("Image won't be shown")