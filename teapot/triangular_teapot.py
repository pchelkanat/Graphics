import matplotlib.pyplot as plt
import numpy as np

from teapot.dotted_teapot import read, viewPort

def bresenhamLine(image, x0, y0, x1, y1, color):
    steep = abs(x1 - x0) < abs(y1 - y0)
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = y1 - y0
    derror = 2 * abs(dy)
    error = 0
    y_curr = y0
    y_incr = 1 if dy > 0 else -1
    for x in range(x0, x1):
        if steep:
            image[y_curr, x, :] = color
        else:
            image[x, y_curr, :] = color
        error += derror
        if error > dx:
            y_curr += y_incr
            error -= 2 * dx
    return image


def triangle(image, faces, vertices, color):
    for i in range(faces.shape[0]):
        p0 = np.int32(np.round(vertices[faces[i][0] - 1]))
        p1 = np.int32(np.round(vertices[faces[i][1] - 1]))
        p2 = np.int32(np.round(vertices[faces[i][2] - 1]))
        # print(p0.dtype)

        bresenhamLine(image, p0[0], p0[1], p1[0], p1[1], color)
        bresenhamLine(image, p1[0], p1[1], p2[0], p2[1], color)
        bresenhamLine(image, p0[0], p0[1], p2[0], p2[1], color)
    return np.flipud((image).transpose((1, 0, 2)))

def triangular_main():
    # _________SOME EXAMPLES_________
    # print(faces.shape[0], faces.shape[1], vertices.shape[0], vertices.shape[1])
    #   6320 3 3644 2
    # print(vertices[faces[1][0]].shape[0], faces[1].shape[0])
    #   2 3

    # print(faces[6319][0], vertices[3000])
    #   3001 as vertices[3000]
    # p0 = vertices[faces[6319][0]-1] #as like as vertices[3000] in .obj is 3001'th line
    #   p0 = np.int32(p0)
    # print(p0, p0[0],p0.dtype)
    #   x,y coordinates from vertices[3000]int32

    # print(faces.shape[0],faces[0],faces[6319])
    #   6320 3646'th 9965'th .obj's lines
    # print(vertices.shape[0], vertices[0],vertices[3643])
    #   3644 1'st 3644'th .obj's lines
    vertices, faces = read("teapot.obj")
    #Выбирать height<=width
    height, width = 800,800
    image = np.zeros((height, width, 3), dtype=np.uint8)
    color = np.array([155, 255, 155], dtype=np.uint8)
    vertices = viewPort(vertices, height, width)
    image = triangle(image, faces, vertices, color)

    plt.figure()
    plt.imshow(image)
    plt.show()
    #plt.imsave('pic_2.png',image)

if __name__ == '__main__':
    triangular_main()