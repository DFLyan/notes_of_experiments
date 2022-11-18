import os


def store(input_path, outfile_name, split):
    file_name_list = os.listdir(input_path)
    f = open(outfile_name, 'w+')
    for file_name in file_name_list:
        f.write('./images/%s/' % split)
        f.write(file_name)
        f.write('\n')

if __name__ == '__main__':
    split = 'test'
    store('/data1/jwchen/yolov7/bdd100k/images/%s' % split, '%s.txt' % split, split)
    print('outputs: %s' % split)