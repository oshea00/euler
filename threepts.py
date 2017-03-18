from math import sqrt, pow, fabs


class Point3D:
    def __init__(self, name, coord):
        self.name = name
        self.coord = coord

    def distance(self, p):
        sumsq = sum([pow(self.coord[i] - p.coord[i], 2) for i in range(len(p.coord))])
        return sqrt(sumsq)

    def toString(self):
        return "{} - {}".format(self.name, self.coord)


points = [
    Point3D('A', (0.1, 0.)),
    Point3D('B', (11.2, 1.)),
    Point3D('C', (6.3, 8.)),
    Point3D('D', (4.4, 3.)),
    Point3D('E', (5.5, 15.)),
    Point3D('F', (8.6, 11.)),
    Point3D('G', (1.7, 6.)),
    Point3D('H', (7.8, 4.)),
    Point3D('I', (9.1, 7.)),
    Point3D('J', (14.2, 5.)),
    Point3D('K', (10.3, 13.)),
    Point3D('L', (16.4, 14.)),
    Point3D('M', (15.5, 2.)),
    Point3D('N', (13.6, 16.)),
    Point3D('O', (3.7, 12.)),
    Point3D('P', (12.8, 10.)),
    Point3D('P', (12.82, 10.))
]


def mindiff(pts):
    mindist = 999999999
    for i in range(len(pts)-1):
        for j in range(i+1, len(pts)):
            d = pts[i].distance(pts[j])
            if d < mindist:
                mindist = d
    return mindist


def finddist(a, b, pts, tol):
    r = []
    ab = a.distance(b)
    for i in range(len(pts)-1):
        for j in range(i+1, len(pts)):
            d = pts[i].distance(pts[j])
            if fabs(d - ab) <= tol:
                r.append(Point3D(pts[i].name, a.coord))
                r.append(Point3D(pts[j].name, b.coord))
                return r
    return r


tol = mindiff(points)
a = Point3D('a', (106.3, 108.))
b = Point3D('b', (115.5, 102.))
r = finddist(a, b, points, tol)

for p in r:
    print p.toString()

