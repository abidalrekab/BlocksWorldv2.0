from CreateDataSet import *
import numpy as np
from PathsModule import JsonInputPath

#
# # load the data
# data = LoadData()
#
# # first update names with a unique GUID's
# UpdateNames(data)
#
# # obtain the parameters values to be used later to modify or create new images
# NrOfObjAggr, NrOfLayers, AggregateShapeNames = GetNrShapesInAggr(data)
# pointee = Object2points(data)
# Aggrcenters, Aggrradis, AggrnrNodes, Aggrorientation, AggrNames, Vertices = GetBasicObjectInfo(data)
# centroid = AggregateCentroide(Aggrcenters)
#
#
#
#
#
# # print out the number of Aggregate object and how many basic objects they have
# #AggregateRotation(pointee,centroid,[30,20])
# # in a case when the user wants to create and add a new object, a layer and the object name should be specified.
# #createNewObject('object_04','layer0', [45,46], 15, 7, 80 )
# # the user can del a basic object from an Aggregate object.
# #delObject(name = 'object_01')
# for iter in range(100):
#     pass
# SaveData(data)
Set1 = CreateDataSet()
Set1.DisplayImage(saveImage='False',showImage='True')
Set1.AggregateRotation([-30,10])
Set1.AggregateTranslate([50,10])
Set1.Updatecenters()
Set1.UpdateVertices()
Set1.DisplayImage(saveImage='False',showImage='True')