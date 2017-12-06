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


# Для нормального отображения в (?)ViewPoint
def minOfVertX(vertices):
    return np.min(vertices[:, 0])


def maxOfVertX(vertices):
    return np.max(vertices[:, 0])


def minOfVertY(vertices):
    return np.min(vertices[:, 1])


def maxOfVertY(vertices):
    return np.max(vertices[:, 1])


def modelXd(vertices):  # 3.217
    return abs(maxOfVertX(vertices) - minOfVertX(vertices))


def modelYd(vertices):
    return abs(maxOfVertY(vertices) - minOfVertY(vertices))


def modelSize(vertices):
    # отсчет начинается с 0, поэтому как минимум прибавляем 1
    size = [modelXd(vertices) + 1, modelYd(vertices) + 1]
    return size


# Центральная точка относительно модели
def centerPoint(vertices):
    center = [modelXd(vertices) / 2, modelYd(vertices) / 2]
    return center


def ortho_project(vertexes):
    x = vertexes[:, 0]
    y = vertexes[:, 1]
    z = vertexes[:, 2]
    l, r = min(x), max(x)
    b, t = min(y), max(y)
    n, f = min(z), max(z)
    ortho = np.array([[2 / (r - l), 0, 0, -((r + l) / (r - l))],
                      [0, 2 / (t - b), 0, -((t + b) / (t - b))],
                      [0, 0, 2 / (f - n), -((f + n) / (f - n))],
                      [0, 0, 0, 1]])
    w, h = r - l, t - b
    vertexes1 = ortho.dot(vertexes.T)
    # print(np.min(vertexes[0]), np.max(vertexes[0]), np.min(vertexes[1]), np.max(vertexes[1]))
    return vertexes1.T, w, h


# Проективная СК
def vertexes_to_projective(vertexes):
    return np.concatenate([vertexes.copy(), np.ones(vertexes.shape[0]).reshape(-1, 1)], axis=1)

def transform(vertices):
    return np.hstack((vertices, np.ones(vertices.shape[0])[:, np.newaxis]))


# Перенос
def translation(delta):
    return np.array([[1, 0, 0],
                     [0, 1, 0],
                     [delta[0], delta[1], 1]])


# Масштаб
def scale(num_scale):
    return np.array([[num_scale, 0, 0],
                     [0, num_scale, 0],
                     [0, 0, 1]])


# Поворот
def rotation(alpha):
    return np.array([[np.cos(alpha), -np.sin(alpha), 0],
                     [np.sin(alpha), np.cos(alpha), 0],
                     [0, 0, 1]])


# Декартовая СК+
def screen_project(vertexes, width, height, w, h):
    x = vertexes[:, 0]
    y = vertexes[:, 1]
    proj_1 = vertexes[:, 3]
    x = x / proj_1
    y = y / proj_1
    vertexes[:, 0] = x
    vertexes[:, 1] = y
    vertexes[:, 0] = width * 0.5 * vertexes[:, 0] + width * 0.5
    vertexes[:, 1] = height * 0.5 * vertexes[:, 1] + height * 0.5
    if w > h:
        vertexes[:, 1] = vertexes[:, 1] * h / w
    else:
        vertexes[:, 0] = vertexes[:, 0] * w / h

    vertexes = np.round(vertexes)
    vertexes = np.array(vertexes, dtype=int)
    vertexes = vertexes[:, :2]
    print(np.min(vertexes[0]), np.max(vertexes[0]), np.min(vertexes[1]), np.max(vertexes[1]))
    return vertexes


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


# матрица, заменяющая всю трансформацию
def matrix(vertices, delta, num_scale, alpha):
    # преобразуем в проективные СК, добавляем координату w
    vertices = transform(vertices)
    # трансформируем
    translates = np.dot(vertices, translation(-delta))
    scales = np.dot(translates, scale(num_scale))
    rotates = np.dot(scales, rotation(alpha))
    detransletes = np.dot(rotates, translation(delta))
    # переводим в декартовую
    vertices = retransform(detransletes)

    return vertices


# Изменение цвета
def coloring(color1, color2):
    for i in range(255):
        t = i / 255
        point = np.uint8([color1[0] * (1 - t) + color2[0] * t, color1[1] * (1 - t) + color2[1] * t])
        color = [point[0], point[1], 0]
    return color
