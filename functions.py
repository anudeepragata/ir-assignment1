import math
from pty import slave_open
from re import A

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class linesegment:
    def __init__(self, p, q):
        self.p = p
        self.q = q

class Polygon:
    def __init__(self, lslist):
        if len(lslist) < 3:
            raise Exception("Side count must be 3 or more.")
        self.lslist = lslist

def dist_2_points(p, q):
    return ((p.x - q.x)**2 + (p.y - q.y)**2)**0.5

def line_2_points(p, q):
    return line(q.y - p.y, p.x - q.x, (q.x - p.x)*p.y - (q.y - p.y)*p.x)

def dist_line_point(l, p):
    return abs(l.a*p.x + l.b*p.y + l.c)/(l.a**2 + l.b**2)**0.5

def angle_lines(l, m):
    a1, b1, a2, b2 = l.a, l.b, m.a, m.b
    if a1*b2 + a2*b2 != 0:
        return math.degrees(math.atan((a2*b1 - a1*b2)/(a1*b2 + a2*b2)))
    else:
        return math.degrees(math.pi/2)

def point_on_line(p, ls):
    l1 = line_2_points(p, ls.p)
    l2 = line_2_points(p, ls.q)
    l = line_2_points(ls.p, ls.q)

    if angle_lines(l, l1) >= 0 and angle_lines(l, l2) >= 0:
        return True
    else:
        return False


p = Polygon([
    linesegment(point(1,1), point(0,0)),
    linesegment(point(1,0), point(1,1)),
    linesegment(point(1,0), point(0,0)),
])
# for i in p.lslist:
#     print(i.p.x, i.p.y, i.q.x, i.q.y)

# print(point_on_line(point(-1,1), linesegment(point(0,0), point(1,0))))