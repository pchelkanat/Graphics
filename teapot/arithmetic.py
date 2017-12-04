import numpy as np


# Длина
def length2D(vec):
    return (vec[0] ** 2 + vec[1] ** 2) ** 0.5


# Нормализация вектора
def normalize2D(vec):
    len = length2D(vec)
    if vec[0] != 0:
        vec[0] = vec[0] / len
    if vec[1] != 0:
        vec[1] = vec[1] / len
    return vec

#Для нормального отображения в (?)ViewPoint
def minOfVertX(vertices):
    return np.min(vertices[:, 0])
def maxOfVertX(vertices):
    return np.max(vertices[:, 0])
def minOfVertY(vertices):
    return np.min(vertices[:, 1])
def maxOfVertY(vertices):
    return np.max(vertices[:, 1])

def modelXd(vertices):  # 3.217
    return abs(maxOfVertX(vertices)-minOfVertX(vertices))
def modelYd(vertices):
    return abs(maxOfVertY(vertices) - minOfVertY(vertices))

def modelSize(vertices):
    #отсчет начинается с 0, поэтому как минимум прибавляем 1
    size = [modelXd(vertices)+1, modelYd(vertices)+1]
    return size
#Центральная точка относительно модели
def centerPoint(vertices):
    center=[modelXd(vertices) / 2, modelYd(vertices) / 2]
    return center



# Проективная СК
def transform(vertices):
    vertices = np.hstack((vertices, np.ones(vertices.shape[0])[:, np.newaxis]))
    return vertices


# Перенос
def translation(Ex, Ey):
    temp = [1, 0, -Ex], [0, 1, -Ey], [0, 0, 1]
    Tr = np.int32(temp)
    # print(Tr)
    return Tr


# Масштаб
def scale(num_scale):
    temp = [num_scale, 0, 0], [0, num_scale, 0], [0, 0, num_scale]
    S = np.int32(temp)
    # print(S)
    return S


# Поворот
def rotation(delta):
    delta = np.radians(delta)
    temp = [np.cos(delta), -np.sin(delta), 0], [np.sin(delta), np.cos(delta), 0], [0, 0, 1]
    R = np.float32(temp)
    # print(R)
    return R


# Обратное перемещение
def retranslation(Ex, Ey):
    temp = [0, 1, Ex], [1, 0, Ey], [0, 0, 1]
    Tr_ = np.int32(temp)
    # print(Tr_)
    return Tr_


# Декартовая СК
def retransform(vertices):
    # print(vertices.shape)
    # 3644,3
    for i in range(vertices.shape[0]):
        for j in range(vertices.shape[1]):
            vertices[i][j] = vertices[i][j] / vertices[i][2]
    vertices = vertices[:vertices.shape[0], :vertices.shape[1] - 1]
    # print(vertices.shape)
    # 3644,2
    return vertices
