### 安装
根据官方的步骤安装，gcc和g++如果版本过高，无法编译。切换成5版本可以编译通过。

## nuscenses数据集
### 创建
数据集和数据输出文件夹得是在一个文件夹，因为gt的生成需要去读取同时生成的plk文件

### TypeError: expected dtype object, got 'numpy.dtype[bool_]'
创建GT的时候，出现这个报错，官方给出的说明是numpy大于等于1.20导致的，然而降到1.19或者1.18，就会出现另一个错误。

```
numpy.ndarray size changed, may indicate binary incompatibility. Expected 88 from C header, got 80 from PyObject
```
发现是导入pycocotools的时候报的错，需要重新安装pycocotools，原因是在自动安装的时候，会自己安装1.20的numpy，所以需要卸载了重新编译
```
pip uninstall pycocotools mmpycocotools
pip install mmpycocotools
```
问题即可解决，可参考官方[FAQ](https://github.com/open-mmlab/mmdetection3d/blob/master/docs/faq.md)

期间实现的一些代码：

docker挂载data文件夹处理数据
```
docker run --shm-size=32g -it -v /data1/jwchen/mmdetection3d/data:/mmdetection3d/data mmdetection3d
```

### 训练nuscenses-mini时，默认的version是完整数据集，如果使用mini会在测试bbox报错
暂时的方法是mmdet3d/datasets/nuscenses_mono_datasets里的类初始化直接修改version为v1.0-mini，在83行


## cofig的一些说明
### 输出所有参数
```
python tools/misc/print_config.py config_file
```

### model
type索引到类，然后后面的参数代表着类的初始化参数，传入类中
自己写可能需要重新编译

### data
类似于pytorch中的dataloader
pipline相当于transform，数据处理

### schedule
大部分设定类似前两个
