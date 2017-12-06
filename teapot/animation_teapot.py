import matplotlib.animation as animation

from teapot.dotted_teapot import *
from teapot.triangular_teapot import triangle


# ----------Для анимации

def drawFrames(image, vertices, faces, delta, alpha, num_scale, frames_count, green, red, height, width):
    ims = []
    for i in range(1, frames_count + 1, ):
        # преобразуем в проективные СК, добавляем координату w
        newvertices = transform(vertices)
        # трансформируем
        translates = np.dot(newvertices, translation(-delta[0], -delta[1]))
        if (i * num_scale / frames_count) <= (2 * np.pi):
            scales = np.dot(translates, scale(i * num_scale / frames_count))
        else:
            scales = np.dot(translates, scale(i * (1 / num_scale) / frames_count))
        rotates = np.dot(scales, rotation(i * alpha / frames_count))
        detransletes = np.dot(rotates, translation(delta[0], delta[1]))
        # переводим в декартовую
        vertices = retransform(detransletes)
        # vertices=matrix(vertices,delta,num_scale, alpha)

        color = coloring(green, red)
        image = triangle(image, faces, vertices, color)

        im = plt.imshow(image, animated=True)
        ims.append([im])
        print("Frame", i, " creation finished.")

        # обнуляем картинку
        image = np.zeros((height, width, 3), dtype=np.uint8)

    return ims


def animation_main():
    vertices, faces = read("teapot.obj")
    height, width = 800, 800

    frames_count = 7  # с увеличением фреймов уменьшается чайник. min=6, после выходит за рамки
    num_scale = 2
    delta = [height / 2, width / 2]
    alpha = 2 * np.pi

    image = np.zeros((height, width, 3), dtype=np.uint8)
    color = np.array([155, 255, 155], dtype=np.uint8)
    green = np.array([0, 255, 0], dtype=np.int32)
    red = np.array([255, 0, 0], dtype=np.int32)

    # перед началом анимации преобразуем вершины
    vertices = vertexes_to_projective(vertices)
    vertices, w, h = ortho_project(vertices)
    vertices = screen_project(vertices, width, height, w, h)

    # ----------Анимация
    fig = plt.figure()
    ims = drawFrames(image, vertices, faces, delta, alpha, num_scale, frames_count, green, red, height, width)
    ani = animation.ArtistAnimation(fig, ims, interval=100, repeat=True, blit=True)

    # ani.save('teapot_animation.mp4')
    # plt.figure()
    plt.show()


if __name__ == '__main__':
    animation_main()
    """
    #Разбираемся. Если не будем переворачивать vertices в вектор x\y\w (вертикальный), а оставим x-y-w (горизонтальный)
    #по условиям умножаем матрицы на вектор справа налево, но если поменять значения в матрицах 1n 2n... и n1 n2...
    #то можно нормально умножить vertices на матрицы
    a=np.array([[1,0,4],[0,1,3],[0,0,1]])
    b=np.array([[1,2,3],[2,3,1],[-1,2,1],[3,2,0]])
    c=np.array([[1,0,0],[0,1,0],[4,3,1]])
    d=np.array([[1,2,-1,3],[2,3,2,2],[3,1,1,0]])

    print("a = matrix",a)
    print("b = vertices x-y-w",b)
    print("c = strange_swap matrix",c)
    print("d =vector x\y\w",d)

    print(".",np.dot(a,d))
    print("..",np.dot(b,c))
    """
