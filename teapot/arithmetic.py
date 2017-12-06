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
    # отсчет начинается с 0, поэтому прибавляем 1
    # !!!не прибавляем
    size = [modelXd(vertices), modelYd(vertices)]
    return size


# Центральная точка относительно самой модели
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
    # отсчет начинается с 0, прибавлять 1?
    w, h = r - l, t - b
    vertexes1 = ortho.dot(vertexes.T)
    # print(np.min(vertexes[0]), np.max(vertexes[0]), np.min(vertexes[1]), np.max(vertexes[1]))
    return vertexes1.T, w, h


# Проективная СК
def vertexes_to_projective(vertexes):
    return np.concatenate([vertexes.copy(), np.ones(vertexes.shape[0]).reshape(-1, 1)],
                          axis=1)  # А зачем Петровец делал reshape?


def transform(vertices):
    TF = np.hstack((vertices, np.ones(vertices.shape[0])[:, np.newaxis]))
    return TF


# Перенос
def translation(delta):
    TR = np.array([[1, 0, 0],
                   [0, 1, 0],
                   [delta[0], delta[1], 1]])
    return TR


# Масштаб
def scale(num_scale):
    SC = np.array([[num_scale, 0, 0],
                   [0, num_scale, 0],
                   [0, 0, 1]])
    return SC


# Поворот
def rotation(alpha):
    RT = np.array([[np.cos(alpha), -np.sin(alpha), 0],
                   [np.sin(alpha), np.cos(alpha), 0],
                   [0, 0, 1]])
    return RT


# Декартовая СК+
def screen_project(vertexes, width, height, w, h):
    width, height = width - 1, height - 1
    x = vertexes[:, 0]
    y = vertexes[:, 1]
    proj_1 = vertexes[:, 3]
    x = x / proj_1
    y = y / proj_1
    vertexes[:, 0] = x
    vertexes[:, 1] = y

    # стыковка к осям Ox,Oy
    vertexes[:, 0] = width * 0.5 * vertexes[:, 0] + width * 0.5
    vertexes[:, 1] = height * 0.5 * vertexes[:, 1] + height * 0.5
    if w > h:
        vertexes[:, 1] = vertexes[:, 1] * h / w
    else:
        vertexes[:, 0] = vertexes[:, 0] * w / h

    vertexes = np.round(vertexes)
    vertexes = np.array(vertexes, dtype=int)
    vertexes = vertexes[:, :2]

    """
    center = centerPoint(vertexes)
    size = modelSize(vertexes)
    # print(center,size)
    # помещаем ровно посередине
    if size[0] <= size[1]:
        size[0], size[1] = size[1], size[0]
        height, width = width, height
    vertexes[:, 0] = vertexes[:, 0] + (width * 0.5 - center[0])
    vertexes[:, 1] = vertexes[:, 1] + (height * 0.5 - center[1])
    """
    return vertexes


# Еще одна формула
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


"""
# матрица, заменяющая всю трансформацию
def matrix(vertices, delta, num_scale, alpha):
    # преобразуем в проективные СК, добавляем координату w
    newvertices = transform(vertices)
    # трансформируем
    translates = np.dot(newvertices, translation(-delta[0], -delta[1]))
    scales = np.dot(translates, scale(i * num_scale / frames_count))
    rotates = np.dot(scales, rotation(i * alpha / frames_count))
    detransletes = np.dot(rotates, translation(delta))
    # переводим в декартовую
    vertices = retransform(detransletes)

    return vertices
"""


# Изменение цвета
def coloring(color1, color2):
    for i in range(256):
        t = i / 255
        point = np.uint8([color1[0] * (1 - t) + color2[0] * t, color1[1] * (1 - t) + color2[1] * t])
        color = [point[0], point[1], 0]
    return color
