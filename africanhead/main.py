import matplotlib.pyplot as plt
import numpy as np
from drawingmodel import draw_model
from model import Model

ah = Model("african_head/african_head.obj")
texture = np.flipud(plt.imread('african_head/african_head_diffuse.tga')).transpose((1, 0, 2))

image = np.zeros((1000, 1000, 3), dtype=np.uint8)
draw_model(ah.faces, ah.vertices, ah.texfaces, ah.texcoords, texture, image)

# plt.imsave('ah_pic1.png', np.rot(image))

plt.figure()
plt.imshow(np.rot90(image))
plt.show()
