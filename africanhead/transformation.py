from africanhead import vector
from africanhead.сonstants import *

# X, Y, Z, W = 0, 1, 2, 3

identityMatrix = np.array([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])

# Матрица трансляции
worldMatrix = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [modelTranslateX, modelTranslateY, modelTranslateZ, 1]])
# обратная ей
_worldMatrix = np.linalg.inv(worldMatrix)

# Матрицы поворота по осям
xRotateMatrix = np.array([[1, 0, 0, 0],
                          [0, np.cos(XAxisRotation), -(np.sin(XAxisRotation)), 0],
                          [0, np.sin(XAxisRotation), np.cos(XAxisRotation), 0],
                          [0, 0, 0, 1]])

yRotateMatrix = np.array([[np.cos(YAxisRotation), 0, (np.sin(YAxisRotation)), 0],
                          [0, 1, 0, 0],
                          [np.sin(YAxisRotation), 0, np.cos(YAxisRotation), 0],
                          [0, 0, 0, 1]])

zRotateMatrix = np.array([[np.cos(ZAxisRotation), -np.sin(ZAxisRotation), 0, 0],
                          [np.sin(ZAxisRotation), np.cos(ZAxisRotation), 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])

# VIEW MATRIX
"""
https://show.ntu.edu.sg/home/ehchua/programming/opengl/CG_BasicsTheory.html#zz-4.3
"""
lookVector = vector.normalize([lookPointX - cameraX, lookPointY - cameraY, lookPointZ - cameraZ, 0.0])
# lookVector = Vector.normalize(lookVector)

rightVector = vector.normalize(vector.crossProduct([0, 1, 0, 0], lookVector))
# rightVector = Vector.normalize(rightVector)

upVector = vector.normalize(vector.crossProduct(lookVector, rightVector))
# upVector = Vector.normalize(upVector)

cameraPos = np.array([cameraX, cameraY, cameraZ, 1])

# M=RT
local2world = np.array([[rightVector[0], upVector[0], lookVector[0], 0],
                        [rightVector[1], upVector[1], lookVector[1], 0],
                        [rightVector[2], upVector[2], lookVector[2], 0],
                        [-(vector.dotProduct(cameraPos, rightVector)), -(vector.dotProduct(cameraPos, upVector)),
                        -(vector.dotProduct(cameraPos, lookVector)), 1]])

screenMatrix = np.array([[viewportWidth / 2, 0, 0, 0],
                         [0, -viewportHeight / 2, 0, 0],
                         [0, 0, 1, 0],
                         [viewportWidth / 2, viewportHeight / 2, 0, 1]])

# PROJECTION MATRIX
yScale = (np.cos(FOV / 2) / np.sin(FOV / 2))
xScale = yScale / aspectRatio
zf = farPlane / (farPlane - nearPlane)
zn = zf * nearPlane

"""
The final step is to flip the z-axis, so that the near plane is still located at z=0,
 but the far plane is flipped and located at z=1 (instead of z=-1). 
 In other words, the larger the z, the further is the object. 
 To perform flipping, we can simply negate the third row of the projection matrix.
"""
projectionMatrix = [[xScale, 0, 0, 0],
                    [0, yScale, 0, 0],
                    [0, 0, -zf, -1],
                    [0, 0, -zn, 0]]


# PERSPECTIVE DIVISON
def perspDiv(triangle):
    triangle.p1 = perspectiveDivision(triangle.p1)
    triangle.p2 = perspectiveDivision(triangle.p2)
    triangle.p3 = perspectiveDivision(triangle.p3)
    return Triangle(triangle.p1, triangle.p2, triangle.p3, triangle.colour)


def perspectiveDivision(point):
    point[0] /= point[3]
    point[1] /= point[3]
    point[2] /= point[3]
    point[3] /= point[3]
    return np.array([point[0], point[1], point[2], point[3]])


viewProjectionMatrix = np.dot(local2world, projectionMatrix)
