# from nuscenes.nuscenes import NuScenes
from nuscenes_modify import NuScenes_modify
from nuscenes.utils.splits import create_splits_logs
import cv2, os, shutil
import tqdm
from typing import List


dataroot = '/ssd/common_datasets/nuscenes/v1.0/'
# dataroot='/data/jwchen/nuscenes/v1.0-mini/'
version = 'v1.0-trainval'
# version = 'v1.0-mini'
nusc = NuScenes_modify(version=version, dataroot=dataroot, verbose=True)
# splits = ['mini_train', 'mini_val']
splits = ['train']


cams = ['CAM_FRONT_LEFT', 'CAM_FRONT', 'CAM_FRONT_RIGHT',
                     'CAM_BACK_RIGHT', 'CAM_BACK', 'CAM_BACK_LEFT']
k = 0
vis_out_path = 'image_label_visual_pair/'


def _split_to_samples(split_logs: List[str]) -> List[str]:
    """
    Convenience function to get the samples in a particular split.
    :param split_logs: A list of the log names in this split.
    :return: The list of samples.
    """
    samples = []
    for sample in nusc.sample:
        scene = nusc.get('scene', sample['scene_token'])
        log = nusc.get('log', scene['log_token'])
        logfile = log['logfile']
        if logfile in split_logs:
            samples.append(sample['token'])
    return samples

if not os.path.exists(vis_out_path):
    os.mkdir(vis_out_path)

for split in splits:
    if not os.path.exists(vis_out_path + split):
        os.mkdir(vis_out_path + split)
    for cam in cams:
        if not os.path.exists(vis_out_path + split + '/' + cam):
            os.mkdir(vis_out_path + split + '/' + cam)

for split in splits:
    # Get assignment of scenes to splits.
    split_logs = create_splits_logs(split, nusc)
    # Use only the samples from the current split.
    sample_tokens = _split_to_samples(split_logs)
    for sample_token in tqdm.tqdm(sample_tokens):
        sample = nusc.get('sample', sample_token)
        if k % 20 == 0:
            for cam in cams:
                img_data = nusc.get('sample_data', sample['data'][cam])
                if os.path.exists(vis_out_path + split + '/' + cam + "/%s_label.jpg" % k):
                    continue

                shutil.copy(dataroot + img_data['filename'],
                            vis_out_path + split + '/' + cam + "/%s.jpg" % k,
                            follow_symlinks=True)

                # img = cv2.imread(dataroot + img_data['filename'], cv2.IMREAD_COLOR)
                # cv2.imwrite(vis_out_path + split + '/' + cam + "/%s.jpg" % k, img)

                nusc._render_sample_data(img_data['token'],
                                        out_path=vis_out_path + split + '/' + cam + "/%s_label.jpg" % k,
                                        verbose=False)
        k = k + 1

# for i in tqdm.tqdm(range(len(nusc.scene))):
#     scene = nusc.scene[i]
#     sample_token = scene['first_sample_token']
#     for j in range(0, scene['nbr_samples']):
#         sample = nusc.get('sample', sample_token)
#         for cam in cams:
#             img_data = nusc.get('sample_data', sample['data'][cam])
#             if os.path.exists(vis_out_path + cam + "/%sscene%s_sample%s.jpg" % (k, i, j)):
#                 continue
#             img = cv2.imread('/data/jwchen/nuscenes/v1.0/' + img_data['filename'], cv2.IMREAD_COLOR)
#             nusc.render_sample_data(img_data['token'],
#                                     out_path=vis_out_path + cam + '/%sscene%s_sample%s_label.jpg' % (k, i, j),
#                                     verbose=False)
#             cv2.imwrite(vis_out_path + cam + "/%sscene%s_sample%s.jpg" % (k, i, j), img)
#         k = k + 1
#             # cv2.imshow("%s" % cam, img)
#             # cv2.waitKey()
#         sample_token = sample['next']

print(k)
