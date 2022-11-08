import os


def store(input_path, outfile_name):
    file_name_list = os.listdir(input_path)
    f = open(outfile_name, 'w+')
    for file_name in file_name_list:
        f.write(file_name)
        f.write('\n')

if __name__ == '__main__':
    store('/data1/jwchen/yolov7/bdd100k/images/test', 'test.txt')
