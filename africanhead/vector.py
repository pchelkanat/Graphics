# X, Y, Z, W = 0, 1, 2, 3


# Длина вектора
def length(vec):
    len = vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2
    return len ** 0.5


# Нормализация вектора
def normalize(vec):
    len = length(vec)
    if vec[0] != 0:
        vec[0] = vec[0] / len
    if vec[1] != 0:
        vec[1] = vec[1] / len
    if vec[2] != 0:
        vec[2] = vec[2] / len
    return vec


# Скалярное произведение
def dotProduct(vec1, vec2):
    return ((vec1[0] * vec2[0]) + (vec1[1] * vec2[1]) + (vec1[2] * vec2[2]))


# Векторное произведение (вычисление определителя матрицы) с нормализацией
def crossProduct(vec1, vec2):
    i = (vec1[1] * vec2[2]) - (vec2[1] * vec1[2])
    j = -((vec1[0] * vec2[2]) - (vec2[0] * vec1[2]))
    k = (vec1[0] * vec2[1]) - (vec2[0] * vec1[1])
    cross = normalize([i, j, k, 0])
    return cross


"""
a = [1, 2, 3]
b = [7, 8, 9]
print(crossProduct(a, b))
print(np.cross(a, b))

x = np.array([1, 2, 3])
y = np.array([7, 8, 9])
print(np.cross(x, y))
print(crossProduct(x, y))
"""
