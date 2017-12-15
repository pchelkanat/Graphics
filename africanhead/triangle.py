import numpy as np

from africanhead.vector import cross


# X, Y, Z, W = 0, 1, 2, 3
# R, G, B = 0, 1, 2

class Triangle:
    def __init__(self, p1, p2, p3, colour):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self.averagePoint = []
        self.normal = [0, 0, 0, 0]
        self.colour = colour


# центр грани, который потом используем для определения diffuse, specular
def averagePoint(triangle):
    x = (triangle.p1[0] + triangle.p2[0] + triangle.p3[0]) / 3.0
    y = (triangle.p1[1] + triangle.p2[1] + triangle.p3[1]) / 3.0
    z = (triangle.p1[2] + triangle.p2[2] + triangle.p3[2]) / 3.0
    return [x, y, z, 1.0]


# нормаль грани, после всех трансформаций
def createTransformedNormal(triangle):
    vec1 = [triangle.p1[0] - triangle.p2[0], triangle.p1[1] - triangle.p2[1],
            triangle.p1[2] - triangle.p2[2]]
    vec2 = [triangle.p3[0] - triangle.p2[0], triangle.p3[1] - triangle.p2[1],
            triangle.p3[2] - triangle.p2[2]]
    triangle.normal = cross(vec2, vec1)
    return triangle.normal


# Барицентрические координаты
def toBarycentric(v_coords, p):
    tri_mat = np.zeros((3, 3))
    tri_mat[0] = v_coords[1] - v_coords[0]  # Y-X
    tri_mat[1] = v_coords[2] - v_coords[0]  # Z-X
    tri_mat[2] = v_coords[0] - p  # Z-P
    cp = cross(tri_mat[:, 0], tri_mat[:, 1])
    if np.abs(cp[2]) < 1:
        return np.array([0.0, 0.0, 0.0])  # нужно, иначе devision by zero
    bc_coords = np.zeros(3)  # бк
    bc_coords[0] = 1.0 - (cp[0] + cp[1]) / cp[2]
    bc_coords[1] = cp[1] / cp[2]
    bc_coords[2] = cp[0] / cp[2]
    return bc_coords



