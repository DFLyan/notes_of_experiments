## 单节点多gpu
官方给出教程为pytest，使用时，将pytest改为python运行，去除“-s”和“-v”
```
  #!/bin/bash

  echo "=============================================================================================================="
  echo "Please run the script as: "
  echo "bash run_gpu.sh DATA_PATH"
  echo "For example: bash run_gpu.sh /path/dataset"
  echo "It is better to use the absolute path."
  echo "=============================================================================================================="
  DATA_PATH=$1
  export DATA_PATH=${DATA_PATH}

  rm -rf device
  mkdir device
  cp ./resnet50_distributed_training.py ./resnet.py ./device
  cd ./device
  echo "start training"
  mpirun -n 8 pytest -s -v ./resnet50_distributed_training.py > train.log 2>&1 &
```
可使用以上的bash文件，也可单独运行最后一行。注意：要先安装pytest

其中：
```
  -v 用于显示每个测试函数的执行结果
  -q 只显示整体测试结果
  -s 用于显示测试函数中print()函数输出
  -x, --exitfirst, exit instantly on first error or failed test
  -h 帮助
```

对比教程和示例，代码中还需加入：
```
from mindspore.context import ParallelMode
context.set_auto_parallel_context(parallel_mode=ParallelMode.AUTO_PARALLEL, gradients_mean=True)
```
