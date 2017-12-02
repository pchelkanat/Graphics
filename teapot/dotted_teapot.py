'''Задание 1.
Произвести отображение вершин модели teapot.obj на двумерную плоскость (изображение, представленное numpy массивом).
+ Использовать только информацию о вершинах. Координаты вершин находятся в строках, начинающихся с "v".
+ Использовать только x и y координаты вершины.
+++ Предусмотреть:
	1. Функцию считывания координат вершин из файлов и сохранение их в numpy массив.
	2. Функцию отображения вершин на изображении.
	3. Функцию отображения изображения на экран или сохранение в файл.
? Изображение представить в виде трехмерного numpy массива (rgb). Ширину и высоту выбрать самим. Цвет вершин так же выбрать самим.
'''

import numpy as np
import matplotlib.pyplot as plt


def read(file):
    global vertices, faces
    vertices = []
    faces = []
    with open(file, "r") as fp:
        for line in fp:
            if line.startswith('#'):
                continue
            values = line.split()
            if not values:
                continue
            if values[0] == 'v':
                v = [float(val) for val in values[1:3]]  # только x, y
                vertices.append(v)
            elif values[0] == 'f':
                face = [float(val) for val in values[1:]]  # все вершины
                faces.append(face)
        # vertices[i]=xi,yi as point; vertices[i][0]=xi; vertices[i][1]=yi
        vertices = np.array(vertices)
        # faces[i]=point0, point1, point2 in i row; faces[i][1]=point1 in i row
        faces = np.array(faces, dtype=np.uint32)
        return vertices, faces


def normalization(vertices, xd, yd):
    a = np.ones((3644, 2), dtype=np.float64)
    vertices = vertices * 100
    for i in range(a.shape[0]):
        a[i][1] = a[i][1] * yd / 2
        a[i][0] = a[i][0] * xd / 2
    # print(a)
    return vertices + a


def draw(image, vertices, color):
    vertices = np.int32(np.round(vertices))
    for i in range(vertices.shape[0]):
        image[vertices[i][0], vertices[i][1], :] = color
    return np.flipud(image.transpose((1, 0, 2)))


if __name__ == '__main__':
    vertices, faces = read("teapot.obj")

    xd = np.int32(np.max(vertices[0]) - np.min(vertices[0])) * 200
    yd = np.int32(np.max(vertices[1]) - np.min(vertices[1])) * 200
    # print(xd,yd)

    image = np.zeros((xd, yd, 3), dtype=np.uint8)
    color = np.array([155, 255, 155], dtype=np.uint8)

    # vertices = normalization(vertices,xd,yd)
    image = draw(image, vertices, color)

    plt.figure()
    plt.imshow(image)
    plt.show()
    # plt.imsave('pic_1.png', image)
