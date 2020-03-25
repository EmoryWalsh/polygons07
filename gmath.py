import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

#Return the dot porduct of a . b
def dot_product(a, b):
    ax = a[0]
    ay = a[1]
    az = a[2]
    bx = b[0]
    by = b[1]
    bz = b[2]
    dp = ax * bx + ay * by + az * bz
    return dp

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    p0 = polygons[i]
    p1 = polygons[i+1]
    p2 = polygons[i+2]

    va = [p1[0]-p0[0], p1[1]-p0[1], p1[2]-p0[2]]
    vb = [p2[0]-p0[0], p2[1]-p0[1], p2[2]-p0[2]]

    vn = [va[1]*vb[2] - va[2]*vb[1], va[2]*vb[0] - va[0]*vb[2], va[0]*vb[1] - va[1]*vb[0]]
    return vn
