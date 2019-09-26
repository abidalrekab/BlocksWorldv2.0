import json
import uuid
from numpy import *
from blocksWorld import *
from PathsModule import JsonInputPath
from PathsModule import AggregateOutputPath
from PathsModule import getImage
import os


class CreateDataSet():
    '''
    THis class contents many functions to help with creating a data set.
        - to initialize the class and set the aggregate object parameters such as : path, load the data, obtaning
            critical information that is important to calculate vertices and centroids.
        - every time the user apply a transformation ( rotation, scaling, or translation ) needs to update vertices and
            centers of each basic shape within that aggregate object.
    '''
    def __init__(self):
        # obtain the path to where you can save the aggregate object image
        self.AggregateOutputPath = AggregateOutputPath
        # get the path of json file that stores the basic objects
        self.path = JsonInputPath
        # load the json file into a variable called data
        self.data = self.LoadDefaultData()
        # generate unique names for all basic shapes using GUID function
        self.UpdateNames()
        # get number of shapes for every aggregate object, number of layers, and their names
        self.NrOfShapesAggr, self.NrOfLayers, self.AggregateShapeNames = self.AggregateObjectParameters()
        # calculate the vertices from given info. [number of vertices, center, radii]---> vertices [[vertex 1][vertex 2]...[vertex n]]
        self.Vertices = self.CalculateVertices()
        # store the vital aggregate object parameters into class param.
        self.Aggrcenters, self.Aggrradii, self.AggrnrVertices,self.Aggrorientation, self.AggrNames, self.AggrVertices  = self.GetBasicObjectInfo()
        # now, obtain the centroid for each aggregate object.[in case we have more than one]
        self.centroid = self.AggregateCentroide()

    def UpdateNames(self):
        '''
        This function is used to generate a unique names for basic shapes.
        :return:
        basic shape names in form of 'object-XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
        '''
        for key, values in self.data.items():
            # using get method to get key's values to aviod throwing errors.
            for index, object in enumerate(values[0].get("AggrObjects")):
                object["GUID"] = 'object-' + str(uuid.uuid4())

    def LoadDefaultData(self):

        '''
        This function is to load json file into a python variable.
        inputs : path to the Json file. 
        :return: python data variable.
        '''
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
        '''
        This function is used to load an existing data to generate the same images.
        :return:
        '''
        # specify the data file name
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

    def CreateNewObject(self, name, layer, center, radii=10, nrVertices=4, rotation=45):
        '''
        This function under construction
        :param name:
        :param layer:
        :param center:
        :param radii:
        :param nrVertices:
        :param rotation:
        :return:
        '''

        return self.data[layer][0]["AggrObjects"].append(
            {'GUID': name, 'center': center, 'radii': radii, 'nrVertices': nrVertices, 'orientation': rotation})

    def DelObject(self, name):
        '''
        This function is under construction
        :param name:
        :return:
        '''
        for key, values in self.data.items():
            listOfitems = values[0]['AggrObjects']
            for i in range(len(listOfitems)):
                print(i)
                if listOfitems[i]['GUID'] == name:
                    print(listOfitems[i])
                    del listOfitems[i]
                    break

    def CalculateVertices(self):
        '''
        This function basically calculate the vertices of a shape given its center, radii, orientation, and number of vertices
        :return:
        a set of n vertices for each shape within the aggregate object in a format [[vertix 0][vertix 1][vertix 2]...[vertix n]]
        '''
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

    def UpdateCenters(self):
        '''
        This function is to compute the new centers of each shape after every a transformation happen.
        :return:
            [x, y] center.
        '''
        for key, value in self.data.items():
            for element in value[0]['AggrObjects']:
                xlist = [Center[0] for Center in element['Vertices']]
                ylist = [Center[1] for Center in element['Vertices']]
                nr = len(xlist)
                x = sum(xlist) / nr
                y = sum(ylist) / nr
                element['center'] = [x, y]

    def UpdateVertices(self):
        '''
        This function copy the New vertices [after performing a transformation] into a data.AggrVertices
        this is done because the way vertices are displayed and used to obtain other calculation is different.
        :return:
        The same format of vertices that are stored into data.
        '''
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

    def AggregateRotation(self, angle):
        '''
        This function is to apply a rotation about centroid by a specific angle
        :param angle:
        :return:
        all vertices after rotation is applied.
        '''
        # assuming that we have only two layers
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
        '''
        By default this function is applying scaling by 1 in both directions x, and y about the centroid
        :param scale:
        :return:
        all vertices after scaling is applied.

        '''
        # assuming that we have only two layers
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

    def AggregateTranslate(self, distance=array([1, 1])):
        '''
        This function is perform a translation to a specific reference point "centroid"
        :param distance [distance x, distance y]:
        :return:
        all vertices after translation is applied.
        '''
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
        '''
        This function is desgined to display all information about an agregate objects, and layers.
        :return:
        all info.
        '''
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
        '''
        This function is to do two tasks:
            - save a  resultant image into a file
            - display it to the user without saving it.
        :param saveImage:
        :param showImage:
        :return:
        '''
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