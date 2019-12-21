from random import randint, random
from GenerateCombination import GenerateCombination
from GeneratePoints import GeneratePoints
from CentersCalculations import CentersCalculations
from CenterCheck import CenterCheck
from AngleBtw2Points import AngleBtw2Points

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
