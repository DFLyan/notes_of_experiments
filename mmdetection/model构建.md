## init中
### RuntimeError: Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same
表示模型在初始化的时候没有被加载进cuda中，解决方法：
```
import torch.nn as nn
```
在类的__init__中，使用nn.ModuleList(),例如：
```
self.conv = nn.ModuleList()
self.conv.append(ConvMoudule(...))
