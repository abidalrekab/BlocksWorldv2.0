import random
from math import *
from RotateApoint import RotateApoint
from blocksWorld import regularPolygon, rotate
from Distance import Distance


def RotationSet(points, Anchor, angle):
    ''''
    rotating a set of points at once
    points are the vertices of the object
    Anchor is the reference point about which points are rotated
    angle is angle of rotation in rads
    '''
    New_points = []
    for idx, items in enumerate(points):
        out = []
        for  idy, point in enumerate(items):
            out.append(RotateApoint(point, Anchor, radians(angle)))
        New_points.append(out)
    return New_points
def Rectangle(center, L, W, orientation):
    d = sqrt(L**2 + W**2)
    alpha = - asin(W/d)
    point1 = [round(num1) for num1 in RotateApoint([center[0] + L / 2, center[1] + W / 2], center, alpha + orientation)]
    point2 = [round(num2) for num2 in RotateApoint([center[0] - L / 2, center[1] + W / 2], center, alpha + orientation)]
    point3 = [round(num3) for num3 in RotateApoint([center[0] - L/2 , center[1] - W / 2], center, alpha + orientation)]
    point4 = [round(num4) for num4 in RotateApoint([center[0] + L / 2, center[1] - W / 2], center, alpha + orientation)]
    return [point1, point2, point3, point4]

def Rectangle1(center, L, W, theta1, theta2, orientation):

    d = sqrt(L**2 + W**2)
    alpha = - asin(W/d)
    L1 = sqrt((W/sin(theta1))**2 - W**2)
    L2 = sqrt((W/sin(theta2))**2 - W**2)
    point1 = [round(num1) for num1 in RotateApoint([center[0] + L / 2, center[1] + W / 2], center, alpha + orientation)]
    point2 = [round(num2) for num2 in RotateApoint([center[0] - L / 2, center[1] + W / 2], center, alpha + orientation)]
    point3 = [round(num3) for num3 in RotateApoint([center[0] - L / 2 + L2 if theta2 < radians(90) else center[0] - L / 2 - L2, center[1] - W / 2], center, alpha + orientation)]
    point4 = [round(num4) for num4 in RotateApoint([center[0] + L / 2 + L1 if theta1 < radians(90) else center[0] + L / 2 - L1, center[1] - W / 2], center, alpha + orientation)]
    return [point1, point2, point3, point4]
def Square(center, length, orientation):
    alpha = - asin(1/sqrt(2))
    point1 = [round(num1) for num1 in RotateApoint( [center[0] + length / 2, center[1] + length / 2], center, alpha + orientation)]
    point2 = [round(num2) for num2 in RotateApoint( [center[0] - length / 2, center[1] + length / 2], center, alpha + orientation)]
    point3 = [round(num3) for num3 in RotateApoint( [center[0] - length / 2, center[1] - length / 2], center, alpha + orientation)]
    point4 = [round(num4) for num4 in RotateApoint( [center[0] + length / 2, center[1] - length / 2], center, alpha + orientation)]
    return [point1, point2, point3, point4]

def Circle(center, Redius):
    return regularPolygon(250,center, Redius)


def Triangle(center, Redius, orientation):
    Points0 = regularPolygon(3,center, Redius)
    Points = rotate(Points0, center, orientation)
    return Points


def Triangle90(center, Redius, angle):
    Points0 = regularPolygon(3,center, Redius)
    Points = rotate(Points0,center, angle)
    del Points[0]
    Points.append(center)
    return Points

def Sedean( Distortion, missing, scale = 2, rotation = 0 ):
    #seed(0)
    if Distortion == 'True':
        VarLocaion = random.choices(range(-40,20,5), k = 2)
        VarSize = random.choices(range(0,20,5), k = 2)
    else:
        VarSize = [0,0]
        VarLocaion = [0,0]

    Wheelsize = random.randint(35,55) * scale

    c0 = [random.randint(300, 340), random.randint(220, 260)]
    BodyL, BodyW = [random.randint(150, 200) * scale, random.randint(50, 76) * scale]
    CabenL = random.randint(30,60) * scale
    alpha1 = asin(BodyW / sqrt(BodyL ** 2 + BodyW ** 2))
    alpha2 = asin(1/ sqrt(2))
    obj1 = Rectangle(c0, BodyL, BodyW, alpha1)
    p1 = obj1[0]
    p2 = obj1[1]
    p3 = obj1[2]
    p4 = obj1[3]
    x = range(p2[0],p1[0])
    y1 = [[num + VarLocaion[0], round(((num - p1[0])* ((p2[1]-p1[1])/(p2[0] - p1[0]))) + p1[1] + 2 * VarLocaion[0])] for num in x]
    y2 = [[num + VarLocaion[1] , round(((num - p4[0])* ((p3[1]-p4[1])/(p3[0] - p4[0]))) + p4[1] + 2 * VarLocaion[1] - CabenL/2)] for num in x]
    c1 = y1[round(0.2 * len(y1))]
    c2 = y1[round(0.8 * len(y1))]
    c3 = y2[round(0.5 * len(y2))]
    obj2 = Circle(c1, Wheelsize + VarSize[0])
    obj3 = Circle(c2, Wheelsize + VarSize[1])
    obj4 = Square(c3, CabenL, alpha2)
    vertices = [obj1,obj2, obj3, obj4]
    cenroid = [round((c0[0] + c1[0] + c2[0] + c3[0])/4), round((c0[1] + c1[1] + c2[1] + c3[1])/4)]
    vertices = RotationSet(vertices, cenroid, rotation )
    if missing == 'True':
        r = random.choice(range(len(vertices)+1))
        del vertices[r]
    else:
        r = 0
    return vertices

def SUV1(Distortion, missing, scale = 1, rotation = 0):
    #seed(0)
    if Distortion == 'True':
        VarLocaion = random.choices(range(-40,20,5), k = 2)
        VarSize = random.choices(range(0,20,5), k = 2)
    else:
        VarSize = [0,0]
        VarLocaion = [0,0]

    Wheelsize = random.randint(25, 45) * scale
    c0 = [random.randint(300, 340), random.randint(220, 260)]
    BodyL, BodyW = [random.randint(150, 200)* scale, random.randint(30, 55)* scale]
    CabL, CabW   = [random.randint(80, 120)* scale, random.randint(30, 35)* scale]
    d1 = sqrt(BodyL ** 2 + BodyW ** 2)
    d2 = sqrt(CabL ** 2 + CabW ** 2)
    alpha1 = asin(BodyW / d1)
    alpha2 = asin(CabW / d2)
    obj1 = Rectangle(c0, BodyL , BodyW,  alpha1)
    p1 = obj1[0]
    p2 = obj1[1]
    p3 = obj1[2]
    p4 = obj1[3]
    x = range(p2[0], p1[0])
    y1 = [[num, round(((num - p1[0]) * ((p2[1] - p1[1]) / (p2[0] - p1[0]))) + p1[1] + 2 * VarLocaion[0])] for num in x]
    y2 = [[num, round(((num - p4[0]) * ((p3[1] - p4[1]) / (p3[0] - p4[0]))) + p4[1] + 2 * VarLocaion[1] - CabW/2 )] for num in x]
    c1 = y1[round(0.2 * len(y1))]
    c2 = y1[round(0.8 * len(y1))]
    c3 = y2[round(0.5 * len(y2))]
    obj2 = Circle(c1, Wheelsize + VarSize[0])
    obj3 = Circle(c2, Wheelsize + VarSize[1])
    obj4 = Rectangle(c3, CabL, CabW, alpha2)
    #obj5 = Rectangle1([200,100], 100, 50, radians(110), radians(80), asin(50/ sqrt(100 ** 2 + 50 ** 2)))
    vertices = [obj1, obj2, obj3, obj4]
    cenroid = [round((c0[0] + c1[0] + c2[0] + c3[0]) / 4), round((c0[1] + c1[1] + c2[1] + c3[1]) / 4)]
    vertices = RotationSet(vertices, cenroid, rotation)
    if missing == 'True':
        r = random.choice(range(len(vertices)+1))
        del vertices[r]
    else:
        r = 0
    return vertices

def SUV2(Distortion, missing, scale = 1, rotation = 0):
    #seed(0)
    if Distortion == 'True':
        VarLocaion = random.choices(range(-40,20,5), k = 2)
        VarSize = random.choices(range(0,20,5), k = 2)
    else:
        VarSize = [0,0]
        VarLocaion = [0,0]

    Wheelsize = random.randint(45, 55) * scale
    c0 = [random.randint(300, 340), random.randint(220, 260)]
    BodyL, BodyW = [random.randint(150, 200) * scale, random.randint(50, 76) * scale]
    CabL, CabW   = [random.randint(80, 120), random.randint(40, 55)]
    d1 = sqrt(BodyL ** 2 + BodyW ** 2)
    d2 = sqrt(CabL ** 2 + CabW ** 2)
    alpha1 = asin(BodyW / d1)
    alpha2 = asin(CabW / d2)
    obj1 = Rectangle(c0, BodyL, BodyW,  alpha1)
    p1 = obj1[0]
    p2 = obj1[1]
    p3 = obj1[2]
    p4 = obj1[3]
    x = range(p2[0], p1[0])
    y1 = [[num + VarLocaion[0], round(((num - p1[0])* ((p2[1]-p1[1])/(p2[0] - p1[0]))) + p1[1] + 2 * VarLocaion[0])] for num in x]
    y2 = [[num + VarLocaion[1] , round(((num - p4[0])* ((p3[1]-p4[1])/(p3[0] - p4[0]))) + p4[1] + 2 * VarLocaion[1] - CabW/2)] for num in x]
    c1 = y1[round(0.2 * len(y1))]
    c2 = y1[round(0.8 * len(y1))]
    c3 = y2[round(0.4 * len(y2))]
    obj2 = Circle(c1, Wheelsize)
    obj3 = Circle(c2, Wheelsize)
    obj4 = Rectangle(c3, CabL, CabW, alpha2)
    obj5 = Rectangle1(c3, CabL, CabW, radians(110), radians(70), asin(CabW/ sqrt(CabW ** 2 + CabL ** 2)))
    vertices = [obj1, obj2, obj3, obj5]
    cenroid = [round((c0[0] + c1[0] + c2[0] + c3[0]) / 4), round((c0[1] + c1[1] + c2[1] + c3[1]) / 4)]
    vertices = RotationSet(vertices, cenroid, rotation)
    if missing == 'True':
        r = random.choice(range(len(vertices)+1))
        del vertices[r]
    else:
        r = 0
    return vertices

def Wagen( Distortion, missing, scale = 1, rotation = 0):
    #seed(0)
    if Distortion == 'True':
        VarLocaion = random.choices(range(-40, 20, 5), k=2)
        VarSize = random.choices(range(0, 20, 5), k=2)
    else:
        VarSize = [0, 0]
        VarLocaion = [0, 0]

    Wheelsize = random.randint(65, 85) * scale
    c0 = [random.randint(300, 340), random.randint(220, 260)]
    BodyL, BodyW = [random.randint(150, 200) * scale, random.randint(50, 76) * scale]
    d1 = sqrt(BodyL ** 2 + BodyW ** 2)
    alpha1 = asin(BodyW / d1)
    obj1 = Rectangle1(c0, BodyL, BodyW, radians(70), radians(110), asin(BodyW/ sqrt(BodyW ** 2 + BodyL ** 2)))
    p1 = obj1[0]
    p2 = obj1[1]
    p3 = obj1[2]
    p4 = obj1[3]
    x = range(p2[0], p1[0])
    y1 = [[num + VarLocaion[0], round(((num - p1[0]) * ((p2[1] - p1[1]) / (p2[0] - p1[0]))) + p1[1] + 2 * VarLocaion[0])] for num in x]
    y2 = [[num + VarLocaion[1], round(((num - p4[0]) * ((p3[1] - p4[1]) / (p3[0] - p4[0]))) + p4[1] + 2 * VarLocaion[1])] for num in x]
    c1 = y1[-1]
    c2m = y2[0]
    lo2, wo2 = 60 * scale, 20 * scale
    c2 = [c2m[0]- 0.75 * lo2, c2m[1] + wo2/2]
    c3 = y1[round(0.2 * len(y1))]
    obj2 = Rectangle1(c2, lo2, wo2, radians(110), radians(90), asin(wo2 / sqrt(lo2 ** 2 + wo2 ** 2)) )
    obj3 = Circle(c1, Wheelsize + VarSize[0])
    obj4 = Triangle(c3, random.randint(60,80) * scale, 90 )
    vertices = [obj1, obj2, obj3, obj4]
    cenroid = [round((c0[0] + c1[0] + c2[0] + c3[0]) / len(vertices)), round((c0[1] + c1[1] + c2[1] + c3[1]) / len(vertices))]
    vertices = RotationSet(vertices, cenroid, rotation)
    if missing == 'True':
        r = random.choice(range(len(vertices)+1))
        del vertices[r]
    else:
        r = 0
    return vertices

def train( Distortion, missing, scale = 2, rotation = 0):
    #seed(0)
    if Distortion == 'True':
        VarLocaion = random.choices(range(-40, 20, 5), k=2)
        VarSize = random.choices(range(0, 20, 5), k=2)
    else:
        VarSize = [0, 0]
        VarLocaion = [0, 0]

    Wheelsize1 = random.randint(65, 75) * scale            # for big wheel
    Wheelsize2 = random.randint(45, 55) * scale            # for small wheel
    c0 = [random.randint(300, 340), random.randint(220, 260)]
    BodyL, BodyW = [random.randint(150, 180) * scale, random.randint(50, 76) * scale]
    CabL, CabW = [ random.randint(60, 75) * scale, random.randint(100, 140)* scale]
    alpha1 = asin(BodyW / sqrt(BodyL ** 2 + BodyW ** 2))
    alpha2 = asin(CabW / sqrt(CabL ** 2 + CabW ** 2))
    obj1 = Rectangle(c0, BodyL, BodyW, alpha1)
    p1 = obj1[0]
    p2 = obj1[1]
    p3 = obj1[2]
    p4 = obj1[3]
    x = range(p2[0], p1[0])
    y1 = [
        [num + VarLocaion[0], round(((num - p1[0]) * ((p2[1] - p1[1]) / (p2[0] - p1[0]))) + p1[1] + 2 * VarLocaion[0])]
        for num in x]
    y2 = [[num + VarLocaion[1],
           round(((num - p4[0]) * ((p3[1] - p4[1]) / (p3[0] - p4[0]))) + p4[1] + 2 * VarLocaion[1] - CabW / 2)] for num
          in x]
    c1 = y1[round(0.2 * len(y1))]
    c2 = y1[round(0.5 * len(y1))]
    c3m = y1[-1]
    c3 = [c3m[0] + CabL/2, c3m[1] - CabW/2]
    obj2 = Circle([sum(x) for x in zip(c1, VarLocaion)], Wheelsize2 + VarSize[0])
    obj3 = Circle([sum(x) for x in zip(c2, VarLocaion)], Wheelsize2 + VarSize[1])
    obj4 = Rectangle(c3, CabL, CabW, alpha2)
    p41 = obj4[0]
    p42 = obj4[1]
    p43 = obj4[2]
    p44 = obj4[3]
    x1 = range(p42[0], p41[0])
    y3 = [
        [num + VarLocaion[0], round(((num - p41[0]) * ((p42[1] - p41[1]) / (p42[0] - p41[0]))) + p41[1] + 2 * VarLocaion[0])]
        for num in x1]
    y4 = [[num + VarLocaion[1],
           round(((num - p4[0]) * ((p3[1] - p4[1]) / (p3[0] - p4[0]))) + p4[1] + 2 * VarLocaion[1])] for num
          in x]
    c4 = y3[round(0.5 * len(y3))]
    obj5 = Circle(c4, Wheelsize1)
    c5m = y4[round(0.2 * len(y4))]
    Obj6R = random.randint(40, 75) * scale
    Obj7R = random.randint(60, 85) * scale
    c5 = [c5m[0], c5m[1] - Obj6R/2]
    obj6 = Triangle([sum(x) for x in zip(c5, VarLocaion)], Obj6R + VarSize[0], 90)
    c6 = y1[0]
    obj7 = Triangle90([sum(x) for x in zip(c6, VarLocaion)], Obj7R + VarSize[1], 0 )
    vertices = [obj1, obj2, obj3, obj4, obj5, obj6, obj7]
    cenroid = [round((c0[0] + c1[0] + c2[0] + c3[0] + c4[0] + c5[0] + c6[0]) / len(vertices)), round((c0[1] + c1[1] + c2[1] + c3[1]+ c4[0] + c5[0] + c6[1]) / len(vertices))]
    vertices = RotationSet(vertices, cenroid, rotation)
    if missing == 'True':
        r = random.choice(range(len(vertices)+1))
        del vertices[r]
    else:
        r = 0
    return vertices

def Bicycle( Distortion, missing, scale = 1, rotation = 0):
    #seed(0)
    if Distortion == 'True':
        VarLocaion = random.choices(range(-20, 20, 5), k=2)
        VarSize = random.choices(range(-20, 20, 5), k=2)
        VarAngle = random.choices(range(-10, 10, 5), k=2)
    else:
        VarSize = [0, 0]
        VarLocaion = [0, 0]
        VarAngle = [0,0]

    Wheelsize = random.randint(70, 95) * scale
    c0 = [random.randint(300, 340), random.randint(220, 260)]
    Obj1R = random.randint(80, 100) * scale
    obj1 = Triangle(c0, Obj1R, 90 + VarAngle[0])
    L = Distance(obj1[0],obj1[1])
    l = sqrt(3/4) * L
    c1 = [c0[0] - 0.5 * L, c0[1] + l/3]
    obj2 = Triangle([sum(x) for x in zip(c1, VarLocaion)], Obj1R, -90 + VarAngle[1])
    p1 = obj2[0]
    p2 = obj2[1]
    p3 = obj2[2]
    c2 = p3
    c3 = [p2[0] + L, p2[1]]
    obj3 = Circle([sum(x) for x in zip(c2, VarLocaion)], Wheelsize + VarSize[0])
    obj4 = Circle([sum(x) for x in zip(c3, VarLocaion)], Wheelsize + VarSize[1])
    O5L, O5w = 20, 10
    c4 = [p1[0], p1[1] - O5w/2]

    p11 = [p1[0] + L , p1[1]]
    p22 = [p2[0] + L , p2[1]]
    x1 = range(int(p11[0]), int(p22[0]))
    y1 = [
        [num + VarLocaion[0], round(((num - p11[0]) * ((p22[1] - p11[1]) / (p22[0] - p11[0]))) + p11[1] + 2 * VarLocaion[0])] for num in x1]
    c5 = y1[round(0.4 * len(y1))]
    O6L, O6w = 120, 10
    obj5 = Rectangle(c4,O5L, O5w, asin(O5w / sqrt(O5L ** 2 + O5w ** 2)))
    obj6 = Rectangle(c5,O6L, O6w, asin(O6w / sqrt(O6L ** 2 + O6w ** 2)) + 45)
    vertices = [obj1, obj2, obj3, obj4, obj5, obj6]
    cenroid = [round((c0[0] + c1[0] + c2[0] + c3[0]) / len(vertices)), round((c0[1] + c1[1] + c2[1] + c3[1] ) / len(vertices))]
    vertices = RotationSet(vertices, cenroid, rotation)
    if missing == 'True':
        r = random.choice(range(len(vertices)+1))
        del vertices[r]
    else:
        r = 0
    return vertices

def Monocycle( Distortion, missing, scale = 1, rotation = 0):
    #seed(0)
    if Distortion == 'True':
        VarLocaion = random.choices(range(-20, 20, 5), k=2)
        VarSize = random.choices(range(-20, 20, 5), k=2)
        VarAngle = random.choices(range(-10, 10, 5), k=2)
    else:
        VarSize = [0, 0]
        VarLocaion = [0, 0]
        VarAngle = [0,0]

    Wheelsize = random.randint(70, 95) * scale
    c0 = [random.randint(300, 340), random.randint(220, 260)]
    Obj1R = random.randint(80, 100) * scale
    obj1 = Triangle(c0, Obj1R, 90 + VarAngle[0])
    L = Distance(obj1[0],obj1[1])
    l = sqrt(3/4) * L
    c1 = [c0[0] - 0.5 * L, c0[1] + l/3]
    obj2 = Triangle([sum(x) for x in zip(c1, VarLocaion)], Obj1R, -90 + VarAngle[1])
    p1 = obj2[0]
    p2 = obj2[1]
    p3 = obj2[2]
    c2 = p3
    c3 = [p2[0] + L, p2[1]]
    obj3 = Circle([sum(x) for x in zip(c2, VarLocaion)], Wheelsize + VarSize[0])
    obj4 = Circle([sum(x) for x in zip(c3, VarLocaion)], Wheelsize + VarSize[1])
    O5L, O5w = 20, 10
    c4 = [p1[0], p1[1] - O5w/2]

    p11 = [p1[0] + L , p1[1]]
    p22 = [p2[0] + L , p2[1]]
    x1 = range(int(p11[0]), int(p22[0]))
    y1 = [
        [num + VarLocaion[0], round(((num - p11[0]) * ((p22[1] - p11[1]) / (p22[0] - p11[0]))) + p11[1] + 2 * VarLocaion[0])] for num in x1]
    c5 = y1[round(0.4 * len(y1))]
    O6L, O6w = 120, 10
    obj5 = Rectangle(c4,O5L, O5w, asin(O5w / sqrt(O5L ** 2 + O5w ** 2)))
    obj6 = Rectangle(c5,O6L, O6w, asin(O6w / sqrt(O6L ** 2 + O6w ** 2)) + 45)
    vertices = [obj1, obj2, obj3, obj4, obj5, obj6]
    cenroid = [round((c0[0] + c1[0] + c2[0] + c3[0]) / len(vertices)), round((c0[1] + c1[1] + c2[1] + c3[1] ) / len(vertices))]
    vertices = RotationSet(vertices, cenroid, rotation)
    if missing == 'True':
        r = random.choice(range(len(vertices)+1))
        del vertices[r]
    else:
        r = 0
    return vertices