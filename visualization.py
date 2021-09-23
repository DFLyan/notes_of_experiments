import cv2
import numpy as np
from layers import disp_to_depth
import moviepy.editor as mpe
import moviepy.video.io.ImageSequenceClip as mvi
from utils.utils import normalize_image_
import matplotlib.pyplot as plt


files = np.load('pt_models/dipe_eigen/disps_s8_split.npy')
# max = (5.0/ files).max()
# file = files[10, :, :]

# hot = cv2.applyColorMap(file.astype(np.uint8), cv2.COLORMAP_JET)
# cv2.imshow("1", hot)
# cv2.waitKey()

file_list = []
for i in range(0, 4071):
    # _, depth = disp_to_depth(files[i, :, :], 0.1, 100.0)

    image = normalize_image_(files[i, :, :]) * 250
    # image = cv2.resize(image, dsize=None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
    hot = cv2.applyColorMap(image.astype(np.uint8), cv2.COLORMAP_MAGMA)
    cv2.imwrite('hotimage/%s.png' % str(i), hot)

    # vmax = np.percentile(files[i, :, :], 95)
    # plt.imsave(files[i, :, :], cmap='magma', vmax=vmax)
    # cv2.imshow("1", hot)
    # cv2.waitKey()
    # file_list.append(np.expand_dims(5 / files[i, :, :], -1))

# cv2.imshow("1", file)
# width = file.shape[0]
# height = file.shape[1]
# video = cv2.VideoWriter('depth.mp4', cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height))
# # a = file[1, :, :]
# for i in range(1, 60):
#     image = files[i, :, :]
#     video.write(image)
# cv2.waitKey()

# a = mpe.concatenate_videoclips(files)
# a = mvi.ImageSequenceClip(file_list, with_mask=False, fps=10)
# a.write_videofile("pt_models/dipe_eigen/depth.mp4")
