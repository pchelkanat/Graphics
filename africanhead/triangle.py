import numpy as np


# X, Y, Z, W = 0, 1, 2, 3
# R, G, B = 0, 1, 2


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


# Барицентрические координаты
def toBarycentric(vertices, point):
    triangle_mx = np.zeros((3, 3))
    triangle_mx[0] = vertices[1] - vertices[0]  # разница между Y X
    triangle_mx[1] = vertices[2] - vertices[0]  # между Z X
    triangle_mx[2] = vertices[0] - point  # между X и точкой
    # хранилище векторное произведение
    cp = np.cross(triangle_mx[:, 0], triangle_mx[:, 1])
    if np.abs(cp[2]) < 1:
        return np.array([-99.0, -99.0, -99.0])  # костыль, тут выдаются ошибки
    bc_coords = np.zeros(3)  # будем хранить тут барицентрические координаты
    bc_coords[0] = 1.0 - (cp[0] + cp[1]) / cp[2]
    bc_coords[1] = cp[1] / cp[2]
    bc_coords[2] = cp[0] / cp[2]
    return bc_coords


# Изображаем с текстурами
def drawTriangle(vertices, z_buffer, texture, tex_coords, intensity, image):
    xMin, xMax = np.min(vertices[:, 0]), np.max(vertices[:, 0])
    yMin, yMax = np.min(vertices[:, 1]), np.max(vertices[:, 1])

    for x in range(int(xMin), int(xMax)):
        for y in range(int(yMin), int(yMax)):
            p = np.array([x, y, 0])
            bc_coords = toBarycentric(vertices, p)
            # проверка принадлежности точки к треугольнику
            if np.all(bc_coords >= 0):
                z = vertices[0, 2] * bc_coords[0] + vertices[1, 2] * bc_coords[1] + vertices[2, 2] * bc_coords[2]
                #смотрим в z-buffer
                if z_buffer[x, y] < z:
                    z_buffer[x, y] = z
                    tc = tex_coords[0] * bc_coords[0] + tex_coords[1] * bc_coords[1] + tex_coords[2] * bc_coords[2]
                    color = texture[int(tc[0] * texture.shape[0]),
                            int(tc[1] * texture.shape[1]), :] * intensity
                    image[x, y, :] = color
                    # return


