import numpy as np


class Model:
    def __init__(self, filename):
        vertices = []
        faces = []
        texcoords = []
        texfaces = []
        normcoords = []
        normfaces = []
        with open(filename) as fp:
            for line in fp:
                if line.startswith('#'):
                    continue
                values = line.split()
                if not values:
                    continue
                if values[0] == 'v':
                    v = [float(val) for val in values[1:]]
                    vertices.append(v)
                elif values[0] == 'vt':
                    vt = [float(values[1]), float(values[2])]
                    texcoords.append(vt)
                elif values[0] == 'vn':
                    vn = [float(val) for val in values[1:]]
                    normcoords.append(vn)
                elif values[0] == 'f':
                    face = []
                    texface = []
                    normface = []
                    for v in values[1:]:
                        w = v.split('/')
                        face.append(int(w[0]) - 1)
                        texface.append(int(w[1]) - 1)
                        normface.append(int(w[2]) - 1)
                    faces.append(face)
                    texfaces.append(texface)
                    normfaces.append(normface)
        self.vertices = np.array(vertices)
        self.faces = np.array(faces, dtype=np.uint32)
        self.texcoords = np.array(texcoords)
        self.texfaces = np.array(texfaces, dtype=np.uint32)
        self.normcoords = np.array(normcoords)
        self.normfaces = np.array(normfaces, dtype=np.int32)
