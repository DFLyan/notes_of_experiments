## lr_congfig
  [warmup](https://github.com/open-mmlab/mmcv/blob/v1.3.7/mmcv/runner/hooks/lr_updater.py#L9)\
  可选择“linear”线性增加、“exp”、constan\
  
## transformer
embed_dims必须是positonal_encoding中num_feats的两倍，不然会报错

## pipline中RandomScaleImageMultiViewImage
1. detr3d中的函数，图像和gt都进行了resize，但只有训练时用，这种情况下，原作者提供的函数，测试时不能使用，只能测试原图像分辨率；

2. 在bevformer中，并未对gt进行resize，训练和测试都用resize；

3. 在bevdepth中，对image使用ida，对bbox使用bda，训练时，都是用数据增强，其中ida会对图像大小在一定范围内进行resize，也就是说会生成不同大小的图像；测试时，ida只取一个大小--final_dim,bda不使用数据增强。

个人理解：如果训练时同时resize输入和输出，那么测试时可以不用resize函数，视为学习一一对应关系，即情况1；如果训练时只resize输入，那么，测试时也可以只resize输入，这样可能结果对尺度更鲁棒。不过究竟哪种更合理，还有待探讨。

总结：测试的时候都是要输出物体的属性，所以不能缩放gt。关键就在于训练时需不需要缩放GT。
