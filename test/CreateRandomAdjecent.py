from BuildDataSet import *
from random import seed
from math import *
from random import randint
from PathsModule import AggregateOutputPath
from itertools import combinations

def GenerateCombination(N):
    # initiate the object B and C positions
    # Get all permutations of length 2
    combinlist = []
    for i in range(N):
        if i < N-1:
            j = i + 1
        else:
            j = 0
        combin = [i, j]
        combinlist.append(combin)
    return combinlist

def GenerateAdjecentShapesPoints(NrObjects = 3, var = 'False'):
    Aggrpoints = []
    centers = []
    ##### these Object A parameters #######
    OriAngle   = randint(0,90)
    center     = [randint(200, 340), randint(100, 280)]
    size       = randint(50,150) # Now setting how many vertices in every object ( we have only three for now )
    NrVertices = randint(3, 7)    # number of vertices for the first object.
    # NOw i need to generate a combination of all possible positions of the next objects
    combinations = GenerateCombination(NrVertices)
    print(combinations)
    # Generate vertices as points [[vertex 1], [vertex 2], [vertex 3],...]
    pointsA = GeneratePoints(center, size, NrVertices, OriAngle)
    centers.append(center)
    if var == 'True':
        '''
        here we will find the new center of an object after considering a small offset 
        away from the central object.
        '''
        dis = randint(2,30)      # this is the distance that new center will be moved inward in direction
        # of outside of baisc object.
        size = size + dis
    pointsB = GeneratePoints(center, size, NrVertices, OriAngle)
    Aggrpoints.append(pointsA)
    for i in range(NrObjects):
        print(len(combinations))
        verGroup = random.choice(combinations)
        print(verGroup)
        combinations.remove(verGroup)                  # to get rid of chosen item so we don't take next time
        Px0 = pointsB[verGroup[0]]
        Px1 = pointsB[verGroup[1]]
        print("Px0 {} , Px1 {} ".format(Px0, Px1))
        NrVertices = randint(3,7)  # shape 2 vertices
        print(NrVertices)
        alpha = 2 * pi / NrVertices
        rd = round(0.5 * distance(Px1, Px0) / sin(alpha / 2))
        size = 2 * rd
        if (Px0[0] == Px1[0]):
            a = 1
            b = - 2*Px0[0]
            c = Px0[0]**2 + ((Px1[1]-Px0[1])/2) ** 2 - rd ** 2
            cx1 = round((- b + sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            cx2 = round((- b - sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            cy1 = round((Px0[1]+Px1[1])/2)
            cy2 = round((Px0[1]+Px1[1])/2)
        elif (Px0[1] == Px1[1]):
            a = 1
            b = - 2 * Px0[1]
            c = Px0[1] ** 2 + ((Px1[0] - Px0[0]) / 2) ** 2 - rd ** 2
            cy1 = round((- b + sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            cy2 = round((- b - sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            cx1 = round((Px0[0] + Px1[0]) / 2)
            cx2 = round((Px0[0] + Px1[0]) / 2)
        else:
            c1 = Px0[0] ** 2 + Px0[1] ** 2 - rd ** 2
            c2 = Px1[0] ** 2 + Px1[1] ** 2 - rd ** 2
            k1 = (Px1[0] - Px0[0]) / (Px1[1] - Px0[1])
            k2 = (c1 - c2) / (Px0[1] - Px1[1])
            a = 1 + k1 ** 2
            b = - k1 * k2 + 2 * Px0[1] * k1 - 2 * Px0[0]
            c = 0.25 * k2 ** 2 - Px0[1] * k2 + c1

            cx1 = round((- b + sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            cx2 = round((- b - sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            cy1 = round(- cx1 * k1 + 0.5 * k2)
            cy2 = round(- cx2 * k1 + 0.5 * k2)
        #print("(cx1 , cy1) ( {} , {}) and (cx2 , cy2) ( {} , {})".format(cx1, cy1, cx2, cy2))
        if distance([cx1, cy1], centers[0]) >= distance([cx2, cy2], centers[0]):
            center = [cx1, cy1]
        else:
            center = [cx2, cy2]
        print("the Distance between Center1, and [{},{}] {}".format(cx1,cy1, distance([cx1, cy1], centers[0])))
        print("the Distance between Center1, and [{},{}] {}".format(cx2,cy2, distance([cx2, cy2], centers[0])))
        print("This is the Center ---- > x {}, y {}".format(center[0], center[1]))
        OriAngle = AngleBtw2Points(center, Px0)
        points = GeneratePoints(center,size,NrVertices, OriAngle)
        centers.append(center)
        Aggrpoints.append(points)
    return centers, Aggrpoints
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
        output.append(np.array([xr, yr]))
    return output

def distance(P1,P2):
    dis = sqrt((P1[0]-P2[0])**2 + (P1[1]-P2[1])**2)
    return dis
def AngleBtw2Points(pointA, pointB):
  changeInX = pointB[0] - pointA[0]
  changeInY = pointB[1] - pointA[1]
  return round(degrees(atan2(changeInY,changeInX)))
if __name__ == "__main__":
    if not os.path.exists(AggregateOutputPath):
        os.makedirs(AggregateOutputPath)
    NumberOfImages = 1
    color = 'blue'
    for idx in range(NumberOfImages):
        imageName = 'TestImage' + str(uuid.uuid4()) + '.png'
        resultFile = os.path.join(AggregateOutputPath, imageName)
        image, canvas = getImage('RGB', (640, 480), 'white')
        c, Aggpoints = GenerateAdjecentShapesPoints()
        for points in Aggpoints:
            print(points)
            drawSolid(canvas, points, color)
            #drawWire(canvas, points)
        image.save(resultFile)


