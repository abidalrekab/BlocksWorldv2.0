import random
from random import seed
from GenerateCombination import GenerateCombination
from GeneratePoints import GeneratePoints
from CentersCalculations import CentersCalculations
from CenterCheck import CenterCheck
from AngleBtw2Points import AngleBtw2Points
from AdjacencyCheck import AdjacencyCheck
from itertools import combinations
from RotateApoint import RotateApoint

def Rectangle(center, length, width, orientation):
    point1 = RotateApoint(center, [center[0] + length / 2, center[1] + width / 2], orientation)
    point2 = RotateApoint(center, [center[0] - length / 2, center[1] + width / 2], orientation)
    point3 = RotateApoint(center, [center[0] - length / 2, center[1] - width / 2], orientation)
    point4 = RotateApoint(center, [center[0] + length / 2, center[1] - width / 2], orientation)
    return [point1, point2, point3, point4]

def Square():
    pass
def Sedean(gap = 'False'):
    seed(0)
    ##### these Object A parameters #######
    OriAngle = random.randint(0, 90)
    center = [random.randint(300, 340), random.randint(220, 260)]
    size = random.randint(50, 100)  # Now setting how many vertices in every object ( we have only three for now )
    NrVertices = 4  # number of vertices for the first object.
    points0 = GeneratePoints(center, size, NrVertices, OriAngle)
    points1 = GeneratePoints(center, size, NrVertices, OriAngle)
    points2 = GeneratePoints(center, size, NrVertices, OriAngle)
    points3 = GeneratePoints(center, size, NrVertices, OriAngle)
    points4 = GeneratePoints(center, size, NrVertices, OriAngle)
    points5 = GeneratePoints(center, size, NrVertices, OriAngle)



    pass


def Turck(center, OriAngle, gap = 'False'):
    pass

def Wagen(center, OriAngle, gap = 'False'):
    pass

def train(center, OriAngle, gap = 'False'):
    pass

def Motorocyle(center, OriAngle, gap = 'False'):
    pass
