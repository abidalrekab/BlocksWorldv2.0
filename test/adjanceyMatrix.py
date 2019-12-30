from itertools import combinations
from Distance import Distance
def adjanceyMatrix(centersShape,RadiusShape, NrObjects):
    matrix = []
    l = list(range(NrObjects + 1))
    comb = combinations(l, 2)
    for item in comb:
        object = list(item)
        d = Distance(centersShape[object[0]],centersShape[object[1]])
        if d < (RadiusShape[object[0]] + RadiusShape[object[1]]):
            bit = 1
        else:
            bit = 0
        object.append(bit)
        matrix.append(object)
    flag = 0
    for element in matrix:
        flag = flag + element[2]
    return flag