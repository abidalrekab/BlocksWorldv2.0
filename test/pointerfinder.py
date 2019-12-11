from math import *
from random import *
import numpy as np
from BuildDataSet import *
from math import *
from random import randint
from PathsModule import AggregateOutputPath

def length(p1,p2):
    return sqrt(pow((p1[0]-p2[0]),2)+pow((p1[1]-p2[1]),2))

def pointstransformation(Px1,Px2,NrVertices):
    midpoint = [(Px1[0]+Px2[0])/2,(Px1[1]+Px2[1])/2 ]
    alpha = 360 / NrVertices
    print(alpha)
    a = length(Px1, Px2)
    R = a / sin(alpha / 2)
    deltay = 0.5 * sqrt(4 * R ** 2 - a ** 2)
    cx = midpoint[0]
    cy1 = midpoint[1] - deltay
    cy2 = midpoint[1] + deltay
    center = [[cx,cy1],[cx,cy2]]
    print(center)
    return center

def RotateAndTraslate(p1,p2):
    Rotpoint = [(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
    print(Rotpoint)
    if p1[0] < p2[0]:
        px0 = p1
        px1 = p2
    elif p2[0] > p1[0]:
        px0 = p2
        px1 = p1
    elif p1[0] == p2[0]:
        if p1[1] < p2[1]:
            px0 = p1
            px1 = p2
        else:
            px0 = p2
            px1 = p1
    elif p1[1] == p2[1]:
        if p1[0] < p2[0]:
            px0 = p1
            px1 = p2
        else:
            px0 = p2
            px1 = p1

    if px0[1] > px1[1] and px0[0] != px1[0]:
        mode = 1
        theta1 = atan(abs(px0[1]-px1[1])/abs(px0[0]-px1[0]))
        print("theta", theta1 * (180/pi))
        xhat1, yhat1 = rot(px0,Rotpoint,theta1)
        xhat2, yhat2 = rot(px1,Rotpoint,theta1)
    elif px1[1] > px0[1] and px0[0] != px1[0]:
        mode = 2
        theta1 = - atan(abs(px0[1] - px1[1]) / abs(px0[0] - px1[0]))
        print("theta", theta1 * (180/pi))
        xhat1, yhat1 = rot(px0, Rotpoint, theta1)
        xhat2, yhat2 = rot(px1, Rotpoint, theta1)
    elif px0[1] == px1[1] :
        mode = 0
        xhat1 = px0[0]
        yhat1 = px0[1]
        xhat2 = px1[0]
        yhat2 = px1[1]
        theta1 = 0
    elif px0[0] == px1[0]:
        mode = 4
        theta1 = pi/2
        print("theta", theta1 * (180 / pi))
        xhat1, yhat1 = rot(px0, Rotpoint, theta1)
        xhat2, yhat2 = rot(px1, Rotpoint, theta1)

    return [xhat1,yhat1],[xhat2,yhat2], theta1, Rotpoint, mode

def RotateAndTranslateCenter(center, theta, Rotpoint, mode):
    c1 = center[0]
    c2 = center[1]
    if mode == 0:
        return [c1,c2]
    elif mode == 1:
        alpha = -theta
        cx1, cy1 = rot(c1, Rotpoint, alpha)
        cx2, cy2 = rot(c2, Rotpoint, alpha)
        return [[cx1, cy1], [cx2, cy2]]

    elif mode == 2:
        alpha = - theta
        cx1, cy1 = rot(c1, Rotpoint, alpha)
        cx2, cy2 = rot(c2, Rotpoint, alpha)
        return [[round(cx1), round(cy1)], [round(cx2), round(cy2)]]
    elif mode == 4:
        alpha = - theta
        cx1, cy1 = rot(c1, Rotpoint, alpha)
        cx2, cy2 = rot(c2, Rotpoint, alpha)
        return [[round(cx1), round(cy1)], [round(cx2), round(cy2)]]

def rot(px0,Rotpoint, theta1):
    xhat1 = (px0[0] - Rotpoint[0]) * cos(theta1) - (px0[1] - Rotpoint[1]) * sin(theta1) + Rotpoint[0]
    yhat1 = (px0[0] - Rotpoint[0]) * sin(theta1) + (px0[1] - Rotpoint[1]) * cos(theta1) + Rotpoint[1]
    return [xhat1,yhat1]
if __name__ == '__main__':
    NrVertices  = randint(3,6)
    p1 = [100,230]
    p2 = [120,230]
    p1hat, p2hat , theta, Rotpoint, mode = RotateAndTraslate(p1,p2)
    print("xhat1 {} yhat1 {}, xhat2 {} yhat2 {}".format(p1hat[0],p1hat[1],p2hat[0],p2hat[1]))
    center = pointstransformation(p1hat, p2hat,NrVertices)
    print("Before rotation and translation", center)
    print(length(center[0], p1hat))
    print(length(center[0], p2hat))
    print(length(center[1], p1hat))
    print(length(center[1], p2hat))
    center = RotateAndTranslateCenter(center,theta, Rotpoint, mode)
    print("After rotation and translation", center)
    print(length(center[0],p1))
    print(length(center[0], p2))
    print(length(center[1], p1))
    print(length(center[1], p2))
    if not os.path.exists(AggregateOutputPath):
        os.makedirs(AggregateOutputPath)
    NumberOfImages = 1
    color = 'blue'
    imageName = 'TestImage' + str(uuid.uuid4()) + '.png'
    resultFile = os.path.join(AggregateOutputPath, imageName)
    image, canvas = getImage('L', (640, 480), 'white')
    drawPoints = [p1,p2,center[0],center[1]]
    print(drawPoints)
    for i in range(len(drawPoints) - 1):
        draw(canvas, (drawPoints[i + 0], drawPoints[i + 1]), 'c')
    image.save(resultFile)
    image.close()