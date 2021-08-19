### 安装
根据官方的步骤安装，gcc和g++如果版本过高，无法编译。切换成5版本可以编译通过。

## nuscenses数据集
### 创建
数据集和数据输出文件夹得是在一个文件夹，因为gt的生成需要去读取同时生成的plk文件

### TypeError: expected dtype object, got 'numpy.dtype[bool_]'
创建GT的时候，出现这个报错
