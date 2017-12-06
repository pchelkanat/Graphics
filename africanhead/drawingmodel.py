import numpy as np

from africanhead.transformation import screenMatrix
from africanhead.triangle import drawTriangle
from africanhead.vector import normalize


def verticesMatrix(faces, vertices, face_id):
    vert_mx = np.zeros((3, 3))
    vert_mx[0] = vertices[faces[face_id, 0]]
    vert_mx[1] = vertices[faces[face_id, 1]]
    vert_mx[2] = vertices[faces[face_id, 2]]
    return vert_mx


def texVerticesMatrix(texfaces, texcoords, face_id):
    vert_mx = np.zeros((3, 2))
    vert_mx[0] = texcoords[texfaces[face_id, 0]]
    vert_mx[1] = texcoords[texfaces[face_id, 2]]
    vert_mx[2] = texcoords[texfaces[face_id, 1]]
    return vert_mx


def draw_model(faces, vertices, texfaces, texcoords, texture, image):
    # пока, определим числами
    lightPoint = np.array([0.0, 0.0, -1.0])
    image_shape = np.array([image.shape[0], image.shape[1]])
    # z-buffer смотрит на расстояние, если ближнее - записываем, если дальнее - оставляем.
    z_buffer = np.zeros((image_shape[0], image_shape[1]))
    # зачем парится по поводу предела, когда у numpy есть бесконечность!
    z_buffer[:] = -np.inf
    for face_id in range(faces.shape[0]):
        vert_mx = verticesMatrix(faces, vertices, face_id)
        n = normalize(np.cross(vert_mx[2] - vert_mx[0], vert_mx[1] - vert_mx[0]))  # z-x  и y-x
        intensity = np.dot(n, lightPoint)
        vert_mx = screenMatrix(vert_mx, image_shape)
        tex_mx = texVerticesMatrix(texfaces, texcoords, face_id)
        if intensity > 0:
            drawTriangle(vert_mx, z_buffer, texture, tex_mx, intensity, image)
