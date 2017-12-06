import math

# откуда смотрим (позиция камеры)
cameraX = 2.0
cameraY = 2.0
cameraZ = -5.0

# куда смотрим из камеры
lookPointX = 2.0
lookPointY = 0.0
lookPointZ = -3.0

#
ViewportWidth = 640
ViewportHeight = 480
ViewportX = 0
ViewportY = 0

# ---------Трансформация----------
# координаты трансляция модели
ModelTranslateX = 2.0
ModelTranslateY = -2.0
ModelTranslateZ = -2.0

# повороты по осям
XAxisRotation = 0.0
YAxisRotation = 0.0
ZAxisRotation = 0.0

# радианные углы
XAxisRotation = math.radians(XAxisRotation)
YAxisRotation = math.radians(YAxisRotation)
ZAxisRotation = math.radians(ZAxisRotation)

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
aspectRatio = ViewportWidth / ViewportHeight

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

"""
shininess = 0.02

#position of global light source
lightSourceX = 1.0
lightSourceY = 0.5
lightSourceZ = 6.0

#colour of light source
lightSourceR = 0.6
lightSourceG = 0.6
lightSourceB = 0.8


#colour of ambientLight
ambientLightR = 0.6
ambientLightG = 0.3
ambientLightB = 0.4
"""
