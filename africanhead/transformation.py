import numpy as np

import Vector
from africanhead.сonstants import *

X, Y, Z, W = 0, 1, 2, 3

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
                          [0, math.cos(XAxisRotation), -(math.sin(XAxisRotation)), 0],
                          [0, math.sin(XAxisRotation), math.cos(XAxisRotation), 0],
                          [0, 0, 0, 1]])

yRotateMatrix = np.array([[math.cos(YAxisRotation), 0, (math.sin(YAxisRotation)), 0],
                          [0, 1, 0, 0],
                          [-math.sin(YAxisRotation), 0, math.cos(YAxisRotation), 0],
                          [0, 0, 0, 1]])

zRotateMatrix = np.array([[math.cos(ZAxisRotation), -math.sin(ZAxisRotation), 0, 0],
                          [math.sin(ZAxisRotation), math.cos(ZAxisRotation), 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])

# VIEW MATRIX
"""
https://www.ntu.edu.sg/home/ehchua/programming/opengl/CG_BasicsTheory.html#zz-4.3
"""
lookVector = Vector.normalize([lookPointX - cameraX, lookPointY - cameraY, lookPointZ - cameraZ, 0.0])
# lookVector = Vector.normalize(lookVector)

rightVector = Vector.normalize(Vector.crossProduct([0, 1, 0, 0], lookVector))
# rightVector = Vector.normalize(rightVector)

upVector = Vector.normalize(Vector.crossProduct(lookVector, rightVector))
# upVector = Vector.normalize(upVector)

CameraPos = [cameraX, cameraY, cameraZ, 1]

viewMatrix = np.array([[rightVector[X], upVector[X], lookVector[X], 0],
                       [rightVector[Y], upVector[Y], lookVector[Y], 0],
                       [rightVector[Z], upVector[Z], lookVector[Z], 0],
                       [-(Vector.dotProduct(CameraPos, rightVector)), -(Vector.dotProduct(CameraPos, upVector)),
                        -(Vector.dotProduct(CameraPos, lookVector)), 1]])

ScreenMatrix = np.array([[ViewportWidth / 2, 0, 0, 0],
                         [0, -ViewportHeight / 2, 0, 0],
                         [0, 0, 1, 0],
                         [ViewportWidth / 2, ViewportHeight / 2, 0, 1]])

# PROJECTION MATRIX
yScale = (math.cos(FOV / 2) / math.sin(FOV / 2))
xScale = yScale / aspectRatio
zf = farPlane / (farPlane - nearPlane)
zn = -(nearPlane * farPlane) / (farPlane - nearPlane)

projectionMatrix = [[xScale, 0, 0, 0],
                    [0, yScale, 0, 0],
                    [0, 0, zf, 1],
                    [0, 0, zn, 0]]
