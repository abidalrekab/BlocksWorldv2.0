from random import *
from BuildDataSet import *
from math import *
from random import randint
from PathsModule import AggregateOutputPath

def Distance(p1, p2):
    return sqrt(pow((p1[0]-p2[0]),2)+pow((p1[1]-p2[1]),2))
def rot(P,Rotpoint, theta1):
    xhat1 = (P[0] - Rotpoint[0]) * cos(theta1) - (P[1] - Rotpoint[1]) * sin(theta1) + Rotpoint[0]
    yhat1 = (P[0] - Rotpoint[0]) * sin(theta1) + (P[1] - Rotpoint[1]) * cos(theta1) + Rotpoint[1]
    return [xhat1,yhat1]
def AngleBtw2Points(pointA, pointB):
  changeInX = pointB[0] - pointA[0]
  changeInY = pointB[1] - pointA[1]
  return round(degrees(atan2(changeInY,changeInX)))
def CenterCheck(center1,center2, MainCenter,point0,point1,point2,point3):
    if Distance(center1, MainCenter) >= Distance(center2, MainCenter):
        center = center1
        px1hat = point0
        px2hat = point2
    else:
        center = center2
        px1hat = point1
        px2hat = point3
    return center, px1hat,px2hat
def GenerateCombination(N, ObjectNumber):
    # initiate the object B and C positions
    # Get all permutations of length 2
    combinlist = []
    for i in range(N):
        if i < N-1:
            j = i + 1
        else:
            j = 0
        combin = [ObjectNumber, i, j]
        combinlist.append(combin)
    return combinlist
def GeneratePoints(center,size, nrVertices,OriAngle):
    points = []
    x = center[0]
    y = center[1]
    #print("x {}, y {}".format(x,y))
    radius = int(size / 2.0)

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
    return output
def CentersCalculations(p1,p2,NrVertices, offset = 0):
    '''
    :param p1: the coordinate of the first point
    :param p2: the coordinate of the second point
    :param PreCenter: the center of an object that this new object is adjecent to.
    :return:
    :param [c1,c2] the center of the next object
    :param Radius of the object
    :param Rotation Angle.
    '''
    # Frist calculate the middle point to rotate point around it.
    #p1 = [160,350]
    #p2 = [120,350]
    #PreCenter = [0,0]
    #NrVertices = 5
    Rotpoint = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
    #print(Distance(p1,p2))
    #---------------------------------------------------------------------------------------------#
    # assign p1 to the most left point and p2 to the most right
    if p1[0] < p2[0]:
        Px0 = p1
        Px1 = p2
    elif p1[0] > p2[0]:
        Px0 = p2
        Px1 = p1
    elif p1[0] == p2[0]:
        if p1[1] < p2[1]:
            Px0 = p1
            Px1 = p2
        else:
            Px0 = p2
            Px1 = p1
    elif p1[1] == p2[1]:
        if p1[0] < p2[0]:
            Px0 = p1
            Px1 = p1

        else:
            Px0 = p2
            Px1 = p1
    #print("After px0 {}, px1 {}".format(Px0, Px1))
    #---------------------------------------------------------------------------------------------#
    # now calculate the rotate angle and rotate the two vertices to have the same y-coordinate
    # so that the calculation of the center will be easier.

    if Px0[1] > Px1[1] and Px0[0] != Px1[0]:
        mode = 1
        theta = atan(abs(Px0[1] - Px1[1]) / abs(Px0[0] - Px1[0]))
        #print("theta", theta * (180 / pi))
        # now calculate the new coordinate of the two vertices p1 and p2 and call them [xhat1,yhat1], and [xhat2,yhat2]
        xhat1, yhat1 = rot(Px0, Rotpoint, theta)
        xhat2, yhat2 = rot(Px1, Rotpoint, theta)
    elif Px1[1] > Px0[1] and Px0[0] != Px1[0]:
        mode = 2
        theta = - atan(abs(Px0[1] - Px1[1]) / abs(Px0[0] - Px1[0]))
        #print("theta", theta * (180 / pi))
        # now calculate the new coordinate of the two vertices p1 and p2 and call them [xhat1,yhat1], and [xhat2,yhat2]
        xhat1, yhat1 = rot(Px0, Rotpoint, theta)
        xhat2, yhat2 = rot(Px1, Rotpoint, theta)
    elif Px0[1] == Px1[1]:
        # in this case the two vertices y-coordinates are equal so no need to rotate them.
        mode = 0
        xhat1 = Px0[0]
        yhat1 = Px0[1]
        xhat2 = Px1[0]
        yhat2 = Px1[1]
        theta = 0
    elif Px0[0] == Px1[0]:
        # in this case the two vertices x-coordinates are equal so we need to rotate them by pi/2 counterclockwise.
        mode = 3
        theta = pi / 2
        #print("theta", theta * (180 / pi))
        xhat1, yhat1 = rot(Px0, Rotpoint, theta)
        xhat2, yhat2 = rot(Px1, Rotpoint, theta)

    #---------------------------------------------------------------------------------------------#

    px1 = [xhat1,yhat1]
    px2 = [xhat2,yhat2]
    px1m = [xhat1, yhat1 - offset]
    px1p = [xhat1, yhat1 + offset]
    px2m = [xhat2, yhat2 - offset]
    px2p = [xhat2, yhat2 + offset]
    #____________________#
    alpha = 2* pi/ NrVertices
    a = Distance(px1, px2)
    R = 0.5 * a / sin(alpha / 2)
    deltay = 0.5 * sqrt(4 * R ** 2 - a ** 2) + offset
    cx  = Rotpoint[0]
    cy1 = Rotpoint[1] - deltay
    cy2 = Rotpoint[1] + deltay
    centerx = [[cx, cy1], [cx, cy2]]
    #--------------------><-----------------><-------------------><------------------------><-----#
    c1 = centerx[0]
    c2 = centerx[1]
    if mode == 0:
        cx1 = c1[0]
        cy1 = c1[1]
        cx2 = c2[0]
        cy2 = c2[1]
        point0 = px1m
        point1 = px1p
        point2 = px2m
        point3 = px2p
    elif mode == 1:
        alpha = - theta
        cx1, cy1 = rot(c1, Rotpoint, alpha)
        cx2, cy2 = rot(c2, Rotpoint, alpha)
        #-----------------#
        point0 = rot(px1m, Rotpoint, alpha)
        point1 = rot(px1p, Rotpoint, alpha)
        point2 = rot(px2m, Rotpoint, alpha)
        point3 = rot(px2p, Rotpoint, alpha)
    elif mode == 2:
        alpha = - theta
        cx1, cy1 = rot(c1, Rotpoint, alpha)
        cx2, cy2 = rot(c2, Rotpoint, alpha)
        # -----------------#
        point0 = rot(px1m, Rotpoint, alpha)
        point1 = rot(px1p, Rotpoint, alpha)
        point2 = rot(px2m, Rotpoint, alpha)
        point3 = rot(px2p, Rotpoint, alpha)

    elif mode == 3:
        alpha = - theta
        cx1, cy1 = rot(c1, Rotpoint, alpha)
        cx2, cy2 = rot(c2, Rotpoint, alpha)
        # -----------------#
        point0 = rot(px1m, Rotpoint, alpha)
        point1 = rot(px1p, Rotpoint, alpha)
        point2 = rot(px2m, Rotpoint, alpha)
        point3 = rot(px2p, Rotpoint, alpha)

    center1 = [cx1, cy1]
    center2 = [cx2, cy2]
    #R = Distance(p1,center1)
    # print("center 1",center1)
    # print("center 2", center2)
    # print("distance between p1 {} ,p2 {} and center 1".format(Distance(p1,center1),Distance(p2,center1)))
    # print("distance between p1 {} ,p2 {} and center 2".format(Distance(p1,center2),Distance(p2,center2)))
    # print("Angle center 1 and p2",AngleBtw2Points(center1,p2))
    # print("Angle center 2 and p2", AngleBtw2Points(center2,p2))
    # print("Diameter R center 1", Distance(center1, p2))
    # print("Diameter R center 2", Distance(center2, p2))

    return center1,center2, R, point0,point1,point2,point3
def GenerateAdjecentShapesPoints(NrObjects = 4, var = 'True'):
    Aggrpoints = []
    centers = []
    ShapeNrVertices = []
    Raduis = []
    orientations = []
    ##### these Object A parameters #######
    OriAngle   = randint(0,90)
    center     = [randint(300, 340), randint(220, 260)]
    size       = randint(50,100) # Now setting how many vertices in every object ( we have only three for now )
    NrVertices = randint(3, 10)    # number of vertices for the first object.
    ShapeNrVertices.append(NrVertices)
    Raduis.append(size)
    orientations.append(OriAngle)
    # NOw i need to generate a combination of all possible positions of the next objects
    combinations = GenerateCombination(NrVertices, 0)
    # Generate vertices as points [[vertex 1], [vertex 2], [vertex 3],...]
    points = GeneratePoints(center, size, NrVertices, OriAngle)
    centers.append(center)
    Aggrpoints.append(points)
    for i in range(1, NrObjects + 1):
        verGroup = random.choice(combinations)
        #print(verGroup)
        combinations.remove(verGroup)                  # to get rid of chosen item so we don't take next time
        points = Aggrpoints[verGroup[0]]
        Px0 = points[verGroup[1]]
        Px1 = points[verGroup[2]]
        #print("Before Px0 {} , Px1 {} , center {}".format(Px0, Px1, centers[verGroup[0]]))
        NrVertices = randint(3,8)  # shape 2 vertices
        ShapeNrVertices.append(NrVertices)
        if var == 'True':
            offset = random.randint(1,10)
            print('offset', offset)
        else:
            offset = 0

        center1, center2, R, point0, point1, point2, point3 = CentersCalculations(Px0,Px1, NrVertices, offset)
        MainCenter = centers[verGroup[0]]
        #print("R", R)
        center, px1hat, px2hat = CenterCheck(center1,center2,MainCenter,point0,point1,point2,point3)
        #print("px2hat",px2hat)
        if offset != 0:
            OriAngle = AngleBtw2Points(center, px2hat)
        else:
            OriAngle = AngleBtw2Points(center,Px1)
        #print(" obect {}, NrVertices {}".format(i, NrVertices))
        #print("This is the Center ---- > x {}, y {}".format(center[0], center[1]))
        size = 2 * R
        Raduis.append(size)
        orientations.append(OriAngle)
        points = GeneratePoints(center,size, NrVertices, OriAngle)
        combination = GenerateCombination(NrVertices, i)
        #print(combination)
        combination.remove(combination[0])
        combination.remove(combination[0])
        combination.remove(combination[-1])
        combinations.extend(combination)
        centers.append(center)
        Aggrpoints.append(points)
        #print(Aggrpoints)
        #print("centers", centers)
    return Aggrpoints, centers, Raduis, orientations, ShapeNrVertices
def CreateNewObject(data, name, center,vertex, radii, nrVertices, rotation):
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
    return data['layer0'][0]["AggrObjects"].append(
        {'GUID': name, 'center': center, "Vertices": vertex, 'radii': radii, 'nrVertices': nrVertices, 'orientation': rotation})
def SaveData(FileName):
    '''
        This function saves all data into a Json file to be used later to generate an exact replica to data set.
    :return:
        Nothing
    '''

    JsonFileName1 = FileName  # modified data file name.
    JsonFilepath1 = os.path.join(AggregateOutputPath, JsonFileName1)

    try:
        with open(JsonFilepath1, 'w') as f:
            json.dump(data, f, indent=1, sort_keys=True)
    except FileNotFoundError:
        print("couldn't save the file")
    return 'done!'


if __name__ == "__main__":
    # The main program parameters
    NumberOfImages = 1                              # the number of images you want [0-100000]
    NrObjects = randint(3,7)                        # the number of objects in each image [1-10]
    var = 'True'                                    # is there gap between objects or not.
    colors = ['red', 'blue', 'black', 'yellow']     # choose a set of colors that gonna be used
    # create output directory
    if not os.path.exists(AggregateOutputPath):
        os.makedirs(AggregateOutputPath)
    # Generate N images and save their information into json file that has the same name as image file
    for idx in range(NumberOfImages):
        tag = 'TestImage' + str(uuid.uuid4())
        imageName = tag + '.png'
        jsonfile = tag
        data = {'layer0':[{"AggregateObjectName":tag, "AggCenter" : [], "AggrObjects":[],
          "orientation": 0}]}
        resultFile = os.path.join(AggregateOutputPath, imageName)
        image, canvas = getImage('RGB', (640, 480), 'white')
        AggpointsShape, centersShape, RadiusShape,rotationShape, NrVerticesShape  = GenerateAdjecentShapesPoints(NrObjects, var)
        for idx, points in enumerate(AggpointsShape):
            color = random.choice(colors)
            drawSolid(canvas, points, color)
            ObjectName = 'object_' + str(idx)
            CreateNewObject(data, ObjectName, centersShape[idx], points, RadiusShape[idx], NrVerticesShape[idx], rotationShape[idx])
            # for i in range(len(points) - 1):
            #     draw(canvas, (points[i + 0], points[i + 1]), str(i))
            # for i in range(len(c) - 1):
            #     draw(canvas, (c[i + 0], c[i + 1]), str(i))
        image.save(resultFile)
        SaveData(jsonfile)



