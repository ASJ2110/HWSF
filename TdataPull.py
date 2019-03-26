
import numpy as np
from matplotlib import pyplot as plt
from skimage import io
from skimage import data
from skimage.color import rgb2gray
from skimage.transform import resize, integral_image

fig, axes = plt.subplots(1, 5, figsize=(20, 4))
ax = axes.ravel()
fig.tight_layout()

def genTdata():
    for i in range(0,5):
        ori = io.imread('./Training_set/face'+str(i)+'.png')
        res = resize(ori, (24,24))
        mono = rgb2gray(res)
        ax[i].imshow(mono)
genTdata()
plt.show()
#inter= integral_image(mono)
#fig, axes = plt.subplots(1, 4, figsize=(16, 4))
#ax = axes.ravel()
#ax[0].imshow(ori)
#ax[1].imshow(res)
#ax[2].imshow(mono, cmap=plt.cm.gray)
#ax[3].imshow(inter)
#fig.tight_layout()
#plt.show()

