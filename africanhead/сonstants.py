import numpy as np

# ----------КАМЕРА----------
# откуда смотрим (позиция камеры)
cameraX = 0.0
cameraY = 0.0
cameraZ = 0.0

# куда смотрим из камеры
lookPointX = 0.0
lookPointY = 0.0
lookPointZ = 0.0

#
viewportWidth = 640
viewportHeight = 480
viewportX = 0
viewportY = 0

# ---------ТРАНСФОРМАЦИЯ----------
# координаты трансляция модели
ModelTranslateX = 2.0
ModelTranslateY = -2.0
ModelTranslateZ = -2.0

# повороты по осям
XAxisRotation = 0.0
YAxisRotation = 0.0
ZAxisRotation = 0.0

# радианные углы
XAxisRotation = np.radians(XAxisRotation)
YAxisRotation = np.radians(YAxisRotation)
ZAxisRotation = np.radians(ZAxisRotation)

"""
https://www.ntu.edu.sg/home/ehchua/programming/opengl/CG_BasicsTheory.html#zz-4.4
The camera has a limited field of view, which exhibits a view frustum (truncated pyramid), and is specified by four parameters:
fovy, aspect, zNear and zFar.

# Fovy: specify the total vertical angle of view in degrees.
# Aspect: the ratio of width vs. height. For a particular z, we can get the height from the fovy, and then get the width from the aspect.
# zNear; the near plane.
# zFar: the far plane.

Это Пирамида отсечения
"""
# fov
FOV = 90.0

# far and near для проективной матрицы
farPlane = 250.0
nearPlane = 1.0

# ??соотношение сторон, разобраться зачем точно оно нужно
# у нас же размер объектов не должен зависеть от расстояния...
aspectRatio = viewportWidth / viewportHeight

# ----------ОСВЕЩЕНИЕ----------
# Составляющие освещеия
ambientMatR = 0.4
ambientMatG = 0.4
ambientMatB = 0.4

diffuseMatR = 1.0
diffuseMatG = 0.6
diffuseMatB = 0.8

specularMatR = 0.6
specularMatG = 0.6
specularMatB = 1.0
