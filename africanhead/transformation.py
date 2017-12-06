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
                        [ModelTranslateX, ModelTranslateY, ModelTranslateZ, 1]])
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
https://www.ntu.edu.sg/home/ehchua/programming/opengl/CG_BasicsTheory.html#zz-4.3
"""
lookVector = vector.normalize([lookPointX - cameraX, lookPointY - cameraY, lookPointZ - cameraZ, 0.0])
# lookVector = Vector.normalize(lookVector)

rightVector = vector.normalize(vector.crossProduct([0, 1, 0, 0], lookVector))
# rightVector = Vector.normalize(rightVector)

upVector = vector.normalize(vector.crossProduct(lookVector, rightVector))
# upVector = Vector.normalize(upVector)

cameraPos = [cameraX, cameraY, cameraZ, 1]

viewMatrix = np.array([[rightVector[0], upVector[0], lookVector[0], 0],
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
zn = -(nearPlane * farPlane) / (farPlane - nearPlane)

projectionMatrix = [[xScale, 0, 0, 0],
                    [0, yScale, 0, 0],
                    [0, 0, zf, 1],
                    [0, 0, zn, 0]]
