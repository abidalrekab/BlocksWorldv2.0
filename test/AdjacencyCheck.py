import Distance
def test(p1 ,p2, p):

    if p1[0] == p2[0] and p1[1] != p2[1]:
        '''
        conducting testing 
        '''
        if p[0] == p1[0] :
            print("----------------")
            vy = sorted([p1[1], p2[1]])
            r2 = range(vy[0] - 1, vy[1] + 1)
            if (p[1] in r2):
                print("1---> 0 ")
                return 0
            else:
                print("1---> 2 ")
                return 2
        elif p[0] > p1[0]:
            return 1
        else:
            return -1
    elif p1[1] == p2[1] and p1[0] != p2[0]:
        '''
                conducting testing 
        '''
        if p[1] == p1[1]:
            print("----------------")
            vx = sorted([p1[0], p2[0]])
            r1 = range(vx[0] - 1, vx[1] + 1)
            if (p[0] in r1):
                print("2 ---> 0 ")
                return 0
            else:
                print("2 ---> 2 ")
                return 2
        elif p[1] > p1[1]:
            return 1
        else:
            return -1
    else:
        ''''
        line equation is w1 * x1 + w2 * x2 + b = 0
        '''
        # compute slope
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        # compute w1
        w2 = 1
        # compute w2
        w1 = - m
        # compute b
        b = -(p1[1] - m * p1[0])
        if w2 * p[1] + w1 * p[0] + b > 0.000000000000001:
            return 1
        elif w2 * p[1] + w1 * p[0] + b < -0.000000000000001:
            return -1
        elif (w2 * p[1] + w1 * p[0] + b) > -0.000000000000001 and (w2 * p[1] + w1 * p[0] + b) < 0.000000000000001:
            print("----------------")
        vx = sorted([p1[0], p2[0]])
        vy = sorted([p1[1], p2[1]])
        r1 = range(vx[0] - 1, vx[1] + 1)
        r2 = range(vy[0] - 1, vy[1] + 1)
        if (p[0] in r1) and (p[1] in r2):
            print("3 ---> 0 ")
            return 0
        else:
            print("3 ---> 2 ")
            return 2


def GenerateEdges(vertex):
    ''''
    generate a list of all edges of an object in a form [point1, point2]
    '''
    combinlist = []
    N = len(vertex)
    for i in range(N):
        if i < N - 1:
            j = i + 1
        else:
            j = 0
        combin = [vertex[i], vertex[j]]
        combinlist.append(combin)
    return combinlist


def AdjacencyCheck(points, centerx):
    print(points)
    # create a group of edges for object one!
    Group1 = GenerateEdges(points[0])
    print(Group1)
    # create a group of edges for object two!
    Group2 = GenerateEdges(points[1])
    print(Group2)
    c2 = centerx[1]
    c1 = centerx[0]
    print(centerx)
    # append the center of each object to the list of vertices.

    '''
    I have done that because i want to check centers of each objects in case when two objects completely overlapped.
    
    '''
    points[0].append(centerx[0])
    points[1].append(centerx[1])

    print("points0", points[0])
    print("points1", points[1])
    # initialize the flags to zero

    flag0 = 0   # flag0 is for indicate whether the two objects are touching
    flag1 = 0   # flag1 is for indicating whether the two objects are overlapping
                # it also shows how many vertices are overlapped
    flag2 = 0   # flag2 is to indicate whether the two objects are adjacent

    # These matrices help me to store and indicate which point is bounded or touching the line.

    Matrix1 = [[0 for x in range(len(Group2))] for x in range(len(points[0]))]
    Matrix2 = [[0 for x in range(len(Group1))] for x in range(len(points[1]))]

    for idx, x in enumerate(points[0]):
        print(x)
        total = 0
        for idy, y in enumerate(Group2):
            print(y)
            c2_sign = test(y[0], y[1], c2)
            x_sign = test(y[0], y[1], x)
            total += (x_sign * c2_sign)
            if x_sign == 0:
                Matrix1[idx][idy] = 1
        if total == len(Group2):
            flag1 += 1
        else:
            flag1 += 0
    for idx, x in enumerate(points[1]):
        total = 0
        print(x)
        for idy, y in enumerate(Group1):
            print(y)
            c1_sign = test(y[0], y[1], c1)
            x_sign = test(y[0], y[1], x)
            total += (x_sign * c1_sign)
            if x_sign == 0:
                Matrix2[idx][idy] = 1

        if total == len(Group1):
            flag1 += 1
        else:
            flag1 += 0

    print(Matrix1)
    print(Matrix2)
    idex1 = [sum(Matrix1[i]) for i in range(len(Matrix1))]
    idex2 = [sum(Matrix2[i]) for i in range(len(Matrix2))]
    # Index of Non-Zero elements in Python list
    # using list comprehension + enumerate()
    res1 = [idx for idx, val in enumerate(idex1) if val != 0]
    res2 = [idx for idx, val in enumerate(idex2) if val != 0]


    if len(res1) == 1 and len(res2) == 1:
        flag0 = 1
        print('touching at the same vertex {}, and {}'.format(points[0][res1[0]],points[1][res2[0]]))

    elif len(res1) == 1 or len(res2) == 1:
        flag0 = -1
        if len(res1) == 1:
            e1 = Matrix1[res1[0]]
            id1 = e1.index(max(e1))
            print('touching at one vertex and an Edge {}'.format(Group2[id1], points[0][res1[0]]))
        else:
            e1 = Matrix2[res2[0]]
            id1 = e1.index(max(e1))

            print('touching at one vertex and an Edge {}'.format(Group1[id1]), points[1][res2[0]])

    elif len(res1) == 2 and len(res2) == 2:
        flag2 = 1
        print('Adjacent at an Edge with two vertices {}, and {}'.format(points[0][res1[0]],points[0][res1[1]]))

    if flag1 == 1:
        print("overlapped with a vertex or more!!")

    return flag0, flag1, flag2


if __name__ == "__main__":
    points1 = [[[100,100],[200,300],[300,100]],[[450,450],[300,400],[400,200]]]
    #d = Distance(c1, c2)
    points2 = [[[80,90], [170, 80], [90, 130]], [[70,130], [90,130], [110, 180], [70, 180]]]
    # a triangle and sequare adjacent
    points3 = [[[140,40],[180,100],[100,100]],[[100,100],[180,100],[180,160],[100,180]]]
    # two triangles overlapped
    points4 = [[[200,60],[280,30],[250,100]],[[240,60],[310,50],[290,110]]]
    # pentagon and rectangle overlapped
    points5 = [[[110,180],[180,220],[150,290],[100,290],[70,250]],[[150,180],[230,180],[230,260],[150,260]]]
    # two object touching in a vertex and an edge
    points = [[[40,10],[40,70],[10,40]],[[70,10],[70,70],[40,40]]]
    obj1 = points[0]
    obj2 = points[1]
    cx1 = sum([obj1[i][0] for i in range(len(obj1))]) / len(obj1)
    cy1 = sum([obj1[i][1] for i in range(len(obj1))]) / len(obj1)
    cx2 = sum([obj2[i][0] for i in range(len(obj2))]) / len(obj2)
    cy2 = sum([obj2[i][1] for i in range(len(obj2))]) / len(obj2)
    centerx = [[cx1, cy1], [cx2, cy2]]
    print(centerx)
    flag0, flag1, flag2 = AdjacencyCheck(points, centerx)
    print(flag0)
    print(flag1)
    print(flag2)

