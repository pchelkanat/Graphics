import matplotlib.pyplot as plt
import numpy as np
from drawingmodel import draw_model
from model import Model
from scipy.misc import imread

ml = Model("african_head/african_head.obj")
texture = np.flipud(imread('african_head/african_head_diffuse.tga')).transpose((1, 0, 2))

image = np.zeros((500, 500, 3), dtype=np.uint8)
draw_model(ml.faces, ml.vertices, ml.texfaces, ml.texcoords, texture, image)

plt.figure()
plt.imshow(np.rot90(image))
plt.show()

# imsave('out2.png', np.flipud(image.transpose((1, 0, 2))))
