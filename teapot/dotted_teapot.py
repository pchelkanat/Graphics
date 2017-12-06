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

import matplotlib.pyplot as plt

from teapot.arithmetic import *

# root = tkinter.Tk()
width = 800  # root.winfo_screenwidth()
height = 800  # root.winfo_screenheight()
pic_size = min(int(width / 2), int(height / 2))


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
                v = [float(val) for val in values[1:]]  # только x, y
                vertices.append(v)
            elif values[0] == 'f':
                face = [float(val) for val in values[1:]]  # все вершины
                faces.append(face)
        # vertices[i]=xi,yi as point; vertices[i][0]=xi; vertices[i][1]=yi
        vertices = np.array(vertices)
        # faces[i]=point0, point1, point2 in i row; faces[i][1]=point1 in i row
        faces = np.array(faces, dtype=np.uint32)
        return vertices, faces


def draw(image, vertices, color):
    vertices = np.int32(np.round(vertices))
    print(vertices.shape)
    for i in range(vertices.shape[0]):
        # print(i)
        image[vertices[i, 0], vertices[i, 1], :] = color
    return image  # np.flipud(image.transpose((1, 0, 2)))


"""Ненужная вещь
Зато мысли были интересные...
def view(vertices, height, width):
    model = modelSize(vertices)
    for i in range(vertices.shape[0]):
        vertices[i, 0] = (vertices[i, 0]) * width / model[0] * 0.5
        vertices[i, 1] = (vertices[i, 1]) * height / model[0] * 0.5
    # определяем новые минимумы увеличенной модели
    xMin, yMin = minOfVertX(vertices), minOfVertY(vertices)
    centerPoint = centerPoint(vertices)
    # print(centerPoint)
    # перемещение на H/h W/w
    for i in range(vertices.shape[0]):
        vertices[i, 0] += width / 2 - centerPoint[0] + abs(xMin)
        vertices[i, 1] += height / 2 - centerPoint[1] + abs(yMin)
    # новый vertices
    # print(arithmetic.minOfVertX(vertices), arithmetic.minOfVertY(vertices))
    return vertices
"""


def prepare_image(pic_size):
    img = np.zeros(shape=(pic_size + 1, pic_size + 1, 3), dtype=np.uint8)
    # img = np.eye(pic_size+1)
    # img.fill(0)
    return img


def dotted_main():
    vertices, faces = read("teapot.obj")
    vertices = vertexes_to_projective(vertices)
    vertices, w, h = ortho_project(vertices)
    vertices = screen_project(vertices, width, height, w, h)

    # image = prepare_image(pic_size)# для pic_size не хватает
    image = np.zeros((height, width, 3), dtype=np.uint8)
    print(image.shape)
    color = np.array([155, 255, 155], dtype=np.uint8)

    image = draw(image, vertices, color)

    plt.figure()
    plt.imshow(np.rot90(image))
    plt.show()
    # plt.imsave('pic_1.png', image)


if __name__ == '__main__':
    dotted_main()
