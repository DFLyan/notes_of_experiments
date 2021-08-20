### 安装
根据官方的步骤安装，gcc和g++如果版本过高，无法编译。切换成5版本可以编译通过。

## nuscenses数据集
### 创建
数据集和数据输出文件夹得是在一个文件夹，因为gt的生成需要去读取同时生成的plk文件

### TypeError: expected dtype object, got 'numpy.dtype[bool_]'
创建GT的时候，出现这个报错，官方给出的说明是numpy大于等于1.20导致的，然而降到1.19或者1.18，就会出现另一个错误。

采取docker挂载data文件夹处理数据
```
docker run --shm-size=32g -it -v /data1/jwchen/mmdetection3d/data:/mmdetection3d/data mmdetection3d
```

<font color=red>*未解决问题*</font>：按照docker中numpy为1.18.5可以跑通，在自己的环境下修改仍然报错
```
numpy.ndarray size changed, may indicate binary incompatibility. Expected 88 from C header, got 80 from PyObject
```
