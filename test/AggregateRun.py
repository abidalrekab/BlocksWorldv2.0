from BuildDataSet import *
#
# load the data set
Set1 = CreateDataSet()
imageList = []
# show the aggregate object before applying any actions
Set1.DisplayImage(saveImage='True',showImage='True')

# apply rotation by -30 degree ( minus means clockwise direction) for first aggregate object and 10 for the second
# in case there were more than one aggregate object.
Set1.AggregateRotation([-30,10])
# Update the aggregate object parameters
Set1.UpdateVertices()
Set1.UpdateCenters()
# apply translation
Set1.AggregateTranslate([50,10])
# Update the aggregate object parameters
Set1.UpdateVertices()
Set1.UpdateCenters()
# apply scaling by factor 2.
Set1.AggregateScaling([0.5,1])
# Update the aggregate object parameters
Set1.UpdateVertices()
Set1.UpdateCenters()
# finally choose to save to a image, show or both for data set.
Set1.DisplayImage(saveImage='True',showImage='True')
# At the end save the whole data set into a json file so we can replicate the exact data set once again.
Set1.SaveData('Set1.json')