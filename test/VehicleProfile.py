import random
from random import seed
from math import *
from GeneratePoints import GeneratePoints
from RotateApoint import RotateApoint
from blocksWorld import regularPolygon

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
def ScaleSet(points, dx, dy):
    pass
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
    return GeneratePoints(center, Redius, 3, orientation)

def Triangle90(center, Redius, orientation):
    Points = regularPolygon(3,center, Redius)
    del Points[0]
    Points.append(center)
    return Points

def Sedean( gap, missing, scale = 2, rotation = 0 ):
    if gap == 'True':
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
        r = random.choice(range(0,3))
        del vertices[r]
    else:
        r = 0
    return vertices

def SUV(gap, missing, scale = 1, rotation = 0):
    seed(0)
    if gap == 'True':
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
        r = random.choice(range(0,3))
        del vertices[r]
    else:
        r = 0
    return vertices

def Wagen( gap, missing, scale = 1, rotation = 0):
    seed(0)
    if gap == 'True':
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
    obj3 = Circle(c1, Wheelsize)
    obj4 = Triangle(c3, 60 * scale, 90 )
    vertices = [obj1, obj2, obj3, obj4]
    cenroid = [round((c0[0] + c1[0] + c2[0] + c3[0]) / len(vertices)), round((c0[1] + c1[1] + c2[1] + c3[1]) / len(vertices))]
    vertices = RotationSet(vertices, cenroid, rotation)
    if missing == 'True':
        r = random.choice(range(0, 3))
        del vertices[r]
    else:
        r = 0
    return vertices

def train( gap, missing, scale = 2, rotation = 0):
    pass

def Motorocyle( gap, missing, scale = 2, rotation = 0):
    pass
