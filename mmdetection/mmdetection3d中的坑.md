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
发现是导入pycocotools的时候报的错，需要重新安装pycocotools，原因是在自动安装的时候(也可能是安装cudnn的时候被升级了），会自己安装1.20的numpy，所以需要卸载了重新编译
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
大部分设定类似前两个\
load_from是仅加载参数，resume_from除参数之外还包含了epoch等\
workflow中，修改数字只会修改loss的显示，而精确度等评价指标还是会每个epoch打印一次

### analysis
里面有很多分析结果的文件，其他的工具可能在tools下的别的问价内，比如可视化

## 来自大佬的咨询
### 多视角数据处理
loading.py第46行

### 数据传输
所有的数据都是以一个字典的形式进行传送的：results\

### pipeline
1、pipeline的最后会有一个collect3D，根据collect层里面的给的字段来拿这个字典里面的最终结果。\
2、collect返回的是一个datacontainer，是一个类似字典的数据容器类：pipeline/formating/DC\
3、使用装饰器后，装饰器会首先把这个函数注册到一个内存空间里，不管这个函数会不会被调用，就像一个全局字典一样。
会不会被用到，我不管，但是记录在了字典里 谁要用只要根据函数名字索引一下就行。\
4、build_from_cfg就是把pipeline的东西，从上到下，
按着顺序去这个全局字典里搜一遍，组成一个可以挨个调用的pipeline对象。
就跟torchvision.transforms.compose一样。

