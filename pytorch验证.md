import torch # 如果pytorch安装成功即可导入

print(torch.cuda.is_available()) # 查看CUDA是否可用

print(torch.cuda.device_count()) # 查看可用的CUDA数量

print(torch.version.cuda) # 查看CUDA的版本号


import torch   # 能否调用pytorch库

print(torch.cuda.current_device())   # 输出当前设备（我只有一个GPU为0）

print(torch.cuda.device(0))   # <torch.cuda.device object at 0x7fdfb60aa588>

print(torch.cuda.device_count())  # 输出含有的GPU数目

print(torch.cuda.get_device_name(0))  # 输出GPU名称 --比如1080Ti

x = torch.rand(5, 3)

print(x)  # 输出一个5 x 3 的tenor(张量)

