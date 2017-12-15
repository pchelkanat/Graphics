import numpy as np

from africanhead.triangle import toBarycentric
from africanhead.vector import normalize, cross


# координаты вершин для одной грани (относительно v x y z)
def verticesMatrix(faces, vertices, face_id):
    vert_mx = np.zeros((3, 3))
    vert_mx[0] = vertices[faces[face_id, 0]]  # 1 точка, имеющая 3 координаты x,y,z
    vert_mx[1] = vertices[faces[face_id, 1]]
    vert_mx[2] = vertices[faces[face_id, 2]]
    return vert_mx


# текстурные координаты вершин для одной грани
# (относительно vt u v (w=0), поэтому не используем с самого начала)
def texVerticesMatrix(texfaces, texcoords, face_id):
    vert_mx = np.zeros((3, 2))
    vert_mx[0] = texcoords[texfaces[face_id, 0]]  # 1 точка, имеющая 2 координаты u,v
    vert_mx[1] = texcoords[texfaces[face_id, 1]]  # 2 ...
    vert_mx[2] = texcoords[texfaces[face_id, 2]]  # 3 ...
    return vert_mx


# нормали вершин для одной грани(относительно vn i j k)
def normVerticesMatrix(normfaces, normcoords, face_id):
    vert_mx = np.zeros((3, 3))
    vert_mx[0] = normcoords[normfaces[face_id, 0]]  # 1 точка, имеющая 3 координаты i,j,k
    vert_mx[1] = normcoords[normfaces[face_id, 1]]  # 2 ...
    vert_mx[2] = normcoords[normfaces[face_id, 2]]  # 3 ...
    return vert_mx


def show(vert_matrix, image_shape):
    result = vert_matrix.copy()
    result[:, :-1] = np.trunc((result[:, :-1] + 1.0) * 0.5 * image_shape)
    return result


# Изображаем с текстурами
def drawTriangle(v_coords, z_buffer, texture, tex_coords, intensity, image):
    min_x, max_x = np.min(v_coords[:, 0]), np.max(v_coords[:, 0])
    min_y, max_y = np.min(v_coords[:, 1]), np.max(v_coords[:, 1])

    for x in range(int(min_x), int(max_x)):
        for y in range(int(min_y), int(max_y)):
            p = np.array([x, y, 0])  # x,y,w
            bc = toBarycentric(v_coords, p)
            if np.all(bc >= 0):
                z = v_coords[0, 2] * bc[0] + v_coords[1, 2] * bc[1] + v_coords[2, 2] * bc[2]
                if z_buffer[x, y] < z:  #
                    z_buffer[x, y] = z
                    tc = tex_coords[0] * bc[0] + tex_coords[2] * bc[1] + tex_coords[1] * bc[2]
                    color = texture[int(tc[0] * texture.shape[0]),  #
                            int(tc[1] * texture.shape[1]), :] * intensity
                    image[x, y, :] = color


# полное отображение с освещением
def draw_model(faces, vertices, texfaces, texcoords, texture, image):
    # пока, определим числами
    lightPoint = np.array([0.0, 0.0, -1.0])
    # lightPoint= calculateColor()
    image_shape = np.array([image.shape[0], image.shape[1]])
    # определение z-buffer, зачем парится по поводу предела, когда у numpy есть бесконечность!:D
    z_buffer = np.zeros((image_shape[0], image_shape[1]))
    z_buffer[:] = -np.inf
    for face_id in range(faces.shape[0]):
        vert_mx = verticesMatrix(faces, vertices, face_id)
        n = normalize(cross(vert_mx[2] - vert_mx[0], vert_mx[1] - vert_mx[0]))
        intensity = np.dot(n, lightPoint)
        vert_mx = show(vert_mx, image_shape)
        tex_mx = texVerticesMatrix(texfaces, texcoords, face_id)
        if intensity > 0:
            drawTriangle(vert_mx, z_buffer, texture, tex_mx, intensity, image)
