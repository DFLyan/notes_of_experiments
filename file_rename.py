import os

'''txt文件内容命名'''
# f = open('splits/s8/test_files.txt', 'w')
# for i in range(0, 4071):
#     f.write("s8")
#     f.write(" ")
#     f.write(str(i).zfill(4))
#     f.write("\n")
# f.close()


'''文件夹所有文件统一命名'''
path = 'S8/s8'
n = 0
filelist = os.listdir(path)
for j in sorted(filelist):
    oldname = path + os.sep + str(j)
    newname = path + os.sep + str(n).zfill(10) + '.png'
    os.rename(oldname, newname)
    n+=1
