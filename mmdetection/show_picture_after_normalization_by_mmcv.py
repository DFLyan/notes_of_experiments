import matplotlib.pyplot as plt
import mmcv
import numpy as np

## visualization of image
a = sweep_imgs[0][0][1].permute(1, 2, 0).cpu()
b = mmcv.imdenormalize(np.array(a), np.array([123.675, 116.28, 103.53])/255.,
                       np.array([58.395, 57.12, 57.375])/255.)
plt.imshow(b)
plt.colorbar()
plt.show()


## visualization of image feature after backbone
c = img_feats[0][0][3].sum(0).cpu()
plt.imshow(c)
plt.colorbar()
plt.show()
for index in [0, 1, 50]:
    c = img_feats[0][0][3][index].cpu()
    plt.imshow(c)
    plt.colorbar()
    plt.show()

## visualization of box_2d_mask
d = box_2d_maskes[0][1].cpu()
e = box_2d_maskes_interpolate[0][1].cpu()
plt.imshow(d)
plt.colorbar()
plt.show()
plt.imshow(e)
plt.colorbar()
plt.show()

## visualization of bev feature after neck
f = fpn_output[0][0].sum(0).cpu()
plt.imshow(f)
plt.colorbar()
plt.show()
for index in [0, 50, 200]:
    f = fpn_output[0][0][index].cpu()
    plt.imshow(f)
    plt.colorbar()
    plt.show()
