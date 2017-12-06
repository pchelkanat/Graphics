# Определим для удобства
import numpy as np

X, Y, Z, W = 0, 1, 2, 3


# Длина вектора
def length(vec):
    len = vec[X] ** 2 + vec[Y] ** 2 + vec[Z] ** 2
    return len ** 0.5


# Нормализация вектора
def normalize(vec):
    len = length(vec)
    if vec[X] != 0:
        vec[X] = vec[X] / len
    if vec[Y] != 0:
        vec[Y] = vec[Y] / len
    if vec[Z] != 0:
        vec[Z] = vec[Z] / len
    return vec


# Скалярное произведение
def dotProduct(vec1, vec2):
    return ((vec1[X] * vec2[X]) + (vec1[Y] * vec2[Y]) + (vec1[Z] * vec2[Z]))


# Векторное произведение
def crossProduct(vec1, vec2):
    i = (vec1[Y] * vec2[Z]) - (vec2[Y] * vec1[Z])
    j = -((vec1[X] * vec2[Z]) - (vec2[X] * vec1[Z]))
    k = (vec1[X] * vec2[Y]) - (vec2[X] * vec1[Y])
    cross = normalize([i, j, k, 0])
    return cross


a = [1, 2, 3]
b = [7, 8, 9]
print(crossProduct(a, b))
print(np.cross(a, b))

x = np.array([1, 2, 3])
y = np.array([7, 8, 9])
print(np.cross(x, y))
print(crossProduct(x, y))
