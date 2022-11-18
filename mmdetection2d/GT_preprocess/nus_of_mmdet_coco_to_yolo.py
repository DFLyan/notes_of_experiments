import contextlib
import json

import cv2
import pandas as pd
from PIL import Image
from collections import defaultdict

from utils import *


cams = ['CAM_FRONT_LEFT', 'CAM_FRONT', 'CAM_FRONT_RIGHT',
        'CAM_BACK_RIGHT', 'CAM_BACK', 'CAM_BACK_LEFT']

def convert_coco_json(json_dir='../coco/annotations/', use_segments=False, split_ = 'train'):
    max = 0
    min = 0
    save_dir = make_dirs('new_dir2/')  # output directory
    names_file = open(save_dir.stem + '/' + split_ + '.txt', 'w+')
    for cam in cams:
        fn = Path(save_dir) / 'labels' / cam
        fn.mkdir()

    # Import json
    for json_file in sorted(Path(json_dir).resolve().glob('nuscenes_infos_%s_mono3d*.json' % split_)):
        # fn = Path(save_dir) / 'labels' / json_file.stem.replace('instances_', '')  # folder name
        # fn.mkdir()
        with open(json_file) as f:
            data = json.load(f)

        # Create image dict
        images = {'%s' % x['id']: x for x in data['images']}
        # Create image-annotations dict
        imgToAnns = defaultdict(list)
        for ann in data['annotations']:
            imgToAnns[ann['image_id']].append(ann)

        # Write labels file
        for img_id, anns in tqdm(imgToAnns.items(), desc=f'Annotations {json_file}'):
            img = images['%s' % img_id]
            h, w, f = img['height'], img['width'], img['file_name']

            bboxes = []
            segments = []
            for ann in anns:
                if ann['iscrowd']:
                    continue
                # The COCO box format is [top left x, top left y, width, height]
                box = np.array(ann['bbox'], dtype=np.float64)

                ### check whether there is edge of bbox located out of the image
                if box.max() > max:
                    max = box.max()
                    print('max%s' % max)
                if box.min() < min:
                    min = box.min()
                    print('min%s' % min)

                box[:2] += box[2:] / 2  # xy top-left corner to center
                box[[0, 2]] /= w  # normalize x
                box[[1, 3]] /= h  # normalize y
                if box[2] <= 0 or box[3] <= 0:  # if w <= 0 and h <= 0
                    continue

                cls = nustoyolo[ann['category_name']]
                box = [cls] + box.tolist()
                if box not in bboxes:
                    bboxes.append(box)

            # Write
            f = f.split('/')
            label_save_dir = Path(save_dir) / 'labels' / f[-2]
            with open((label_save_dir / f[-1]).with_suffix('.txt'), 'a') as file:
                for i in range(len(bboxes)):
                    line = *(segments[i] if use_segments else bboxes[i]),  # cls, box or segments
                    file.write(('%g ' * len(line)).rstrip() % line + '\n')

            names_file.write('./images/%s/%s' % (f[6], f[7]))
            names_file.write('\n')
    names_file.close()


if __name__ == '__main__':
    source = 'COCO'

    if source == 'COCO':
        convert_coco_json('/data/jwchen/nuscenes/v1.0/',  # directory with *.json
                          use_segments=False,
                          split_='train')