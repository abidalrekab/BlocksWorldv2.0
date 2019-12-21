from math import pi, cos, sin

def GeneratePoints(center,size, nrVertices,OriAngle):
    points = []
    x = center[0]
    y = center[1]
    #print("x {}, y {}".format(x,y))
    radius = int(size / 2.0)

    x0 = round(x + radius)
    y0 = y
    points.append([x0, y0])

    segment = 2 * pi / nrVertices

    # (xi - x)^2 + (yi - y)^2 = radius^2
    for i in range(nrVertices - 1):
        angle = (i + 1) * segment

        xi = round(radius * cos(angle) + x)
        yi = round(radius * sin(angle) + y)
        points.append([xi, yi])
    # print(points)
    output = []
    radAngle = (OriAngle / 360.0) * 2.0 * pi
    c = cos(radAngle)
    s = sin(radAngle)
    #
    for point in points:
        x = point[0] - center[0]
        y = point[1] - center[1]
        xr = round(x * c - y * s + center[0])
        yr = round(x * s + y * c + center[1])
        output.append([xr, yr])
    return output
