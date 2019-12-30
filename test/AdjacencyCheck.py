

def test(p1,p2, p):
    ''''
    line equation is w1 * x1 + w2 * x2 + b = 0
    '''
    # compute slope
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    # compute w1
    w2 = 1/(m*p1[0]-p1[1])
    # compute w2
    w1 = - m/(m*p1[0]-p1[1])
    # compute b
    b = 1
    if w2 * p[1] + w1 * p[0] + b >= 0:
        return 1
    elif w2 * p[1] + w1 * p[0] + b < 0:
        return -1

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
    Group1 = GenerateEdges(points[0])
    print(Group1)
    Group2 = GenerateEdges(points[1])
    print(Group2)
    c2 = centerx[1]
    c1 = centerx[0]
    print(centerx)
    points[0].append(centerx[0])
    points[1].append(centerx[1])
    print("point0", points[0])
    print("points1", points[1])
    flag = 0
    for x in points[0]:
        print(x)
        total = 0
        for y in Group2:
            print(y)
            c2_sign = test(y[0], y[1], c2)
            x_sign  = test(y[0], y[1], x )
            total += (x_sign * c2_sign)
        if total == len(Group2):
            flag += 1
        else:
            flag += 0
    for x in points[1]:
        total = 0
        for y in Group1:
            c1_sign = test(y[0], y[1], c1)
            x_sign  = test(y[0],y[1],x)
            total += (x_sign * c1_sign)
        if total == len(Group1):
            flag += 1
        else:
            flag += 0
    return flag


if __name__ == "__main__":
    points = [[[100,100],[200,300],[300,100]],[[450,450],[300,400],[400,200]]]
    #points = [[[120, 70], [180, 120], [90, 130]], [[80, 90], [170, 80], [90, 130]]]
    obj1 = points[0]
    obj2 = points[1]
    cx1 = sum([obj1[i][0] for i in range(len(obj1))]) / len(obj1)
    cy1 = sum([obj1[i][1] for i in range(len(obj1))]) / len(obj1)
    cx2 = sum([obj2[i][0] for i in range(len(obj2))]) / len(obj2)
    cy2 = sum([obj2[i][1] for i in range(len(obj2))]) / len(obj2)
    centerx = [[cx1,cy1],[cx2,cy2]]
    print(centerx)
    flags = AdjacencyCheck(points,centerx)
    print(flags)