import random
from random import seed
from GenerateCombination import GenerateCombination
from GeneratePoints import GeneratePoints
from CentersCalculations import CentersCalculations
from CenterCheck import CenterCheck
from AngleBtw2Points import AngleBtw2Points
from AdjacencyCheck import AdjacencyCheck
from itertools import combinations


def removeDuplicates(x):

    '''
    This function is to remove duplicate elements in a list.
    :param x:
    :return: the same list with non-duplicate elements
    '''
    return list(dict.fromkeys(x))


def DeleteByIndices(lst, indices):

    indices_as_set = set(indices)
    return [ lst[i] for i in range(len(lst)) if i not in indices_as_set ]

def GenerateAdjecentShapesPoints(NrObjects = 10, var = 'False', OverlapRemove = 'False'):

    seed(0)
    Aggrpoints = []
    centers = []
    ShapeNrVertices = []
    Raduis = []
    orientations = []
    ##### these Object A parameters #######
    OriAngle   = random.randint(0,90)
    center     = [random.randint(300, 340), random.randint(220, 260)]
    size       = random.randint(50,100) # Now setting how many vertices in every object ( we have only three for now )
    NrVertices = random.randint(3, 10)    # number of vertices for the first object.
    ShapeNrVertices.append(NrVertices)
    Raduis.append(size)
    orientations.append(OriAngle)
    # NOw i need to generate a combination of all possible positions of the next objects
    combs = GenerateCombination(NrVertices, 0)
    # Generate vertices as points [[vertex 1], [vertex 2], [vertex 3],...]
    points = GeneratePoints(center, size, NrVertices, OriAngle)
    centers.append(center)
    Aggrpoints.append(points)
    #print(combs)
    for i in range(1, NrObjects + 1):
        verGroup = random.choice(combs)
        #print(verGroup)
        combs.remove(verGroup)                  # to get rid of chosen item so we don't take next time
        points = Aggrpoints[verGroup[0]]
        Px0 = points[verGroup[1]]
        Px1 = points[verGroup[2]]
        #print("Before Px0 {} , Px1 {} , center {}".format(Px0, Px1, centers[verGroup[0]]))
        NrVertices = random.randint(3,8)  # shape 2 vertices
        ShapeNrVertices.append(NrVertices)
        if var == 'True':
            offset = random.randint(1,10)
            #print('offset', offset)
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
        if NrVertices >= 4:
            combination.remove(combination[0])
            combination.remove(combination[-1])

        combs.extend(combination)
        centers.append(center)
        Aggrpoints.append(points)
        #print(Aggrpoints)
        #print("centers", centers)

    #__________________________________________________________________________________________________________________#
    #  ____________________________     In this section overlapped object can be removed if enabled   _________________#
    #print("Aggrpoints", Aggrpoints)
    if OverlapRemove == 'True':
        m = [x for x in range(NrObjects)]
        comb = list(combinations(m, 2))
        results = [list(element) for element in comb]
        #print(results)
        removelist = []
        print(" We gonna compare {} combination to find overlapped object".format(len(results)))
        for num, ele in enumerate(results):
            print(ele)
            print("{} from {}".format(num+1, len(results)))
            print("{}-{}%".format('-' * num, round((num+1)/len(results) * 100,2)) )
            G1 = Aggrpoints[ele[0]]
            G2 = Aggrpoints[ele[1]]
            centerx = [centers[ele[0]],centers[ele[1]]]
            #print(centerx)
            flag0, flag1, flag2 = AdjacencyCheck([G1,G2], centerx)
            if flag1 >= 1:
                removelist.append(ele[1])
                #print("the list", removelist)

        removelist = removeDuplicates(removelist)
        print("the list", removelist)
        Aggrpoints = DeleteByIndices(Aggrpoints, removelist)
        centers = DeleteByIndices(centers, removelist)
        Raduis = DeleteByIndices(Raduis, removelist)
        orientations = DeleteByIndices(orientations, removelist)
        ShapeNrVertices = DeleteByIndices(ShapeNrVertices, removelist)


    return Aggrpoints, centers, Raduis, orientations, ShapeNrVertices
