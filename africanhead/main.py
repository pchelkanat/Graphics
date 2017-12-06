import numpy as np
from scipy.misc import imread, imsave

from drawing import draw_model
from model import Model

ml = Model("obj/african_head.obj")
texture = np.flipud(imread('obj/african_head_diffuse.tga')).transpose((1, 0, 2))

image = np.zeros((2000, 2000, 3), dtype=np.uint8)
draw_model(ml.faces, ml.vertices, ml.texfaces, ml.texcoords, texture, image)

imsave('out2.png', np.flipud(image.transpose((1, 0, 2))))
