# 安装pytorch1.4版本的，在ubuntu16.04下，为系统可安装驱动下支持的最高版本，直接安装torchvision==0.5.0即可
## 傻瓜式步骤: 

    conda create -n hov python==3.6.9
    conda install cudatoolkit==9.0
    conda install cudnn
    conda install openmpi nccl
    pip install cmake
    pip install torchvision==0.5.0 (编译前，必须先安装好深度学习框架）
    pip install tensorflow-gpu
    HOROVOD_GPU_OPERATIONS=NCCL pip install horovod

## 检查是否安装成功
```horovodrun --check-build```

应该会出现： 

    Horovod v0.19.4:
    Available Frameworks:
        [X] TensorFlow
        [X] PyTorch
        [X] MXNet
    Available Controllers:
        [X] MPI
        [X] Gloo
    Available Tensor Operations:
        [X] NCCL
        [ ] DDL
        [ ] CCL
        [X] MPI
        [X] Gloo

## package-net所需pip
yacs, opencv-python, matplotlib, termcolor, tqdm, wandb, pandas, boto3, pyquaternion

# 第一次安装时的参考
### 如果是1.5版本，可参考[官方给出的版本](https://github.com/horovod/horovod/blob/master/docs/conda.rst)
## conda
### cudatoolkit==9.*
### cudnn
### nccl（版本可使用1.*或者2*，具体看安装的时候是否编译失败）
### mpi4py官网提供安装openmpi或者使用自己编译
RUN mkdir /tmp/openmpi && \
    cd /tmp/openmpi && \
    wget https://www.open-mpi.org/software/ompi/v4.0/downloads/openmpi-4.0.0.tar.gz && \
    tar zxf openmpi-4.0.0.tar.gz && \
    cd openmpi-4.0.0 && \
    ./configure --enable-orterun-prefix-by-default && \
    make -j $(nproc) all && \
    make install && \
    ldconfig && \
    rm -rf /tmp/openmpi

## 安装的时候如果安装失败，就要在非缓存情况下重装
HOROVOD_GPU_OPERATIONS=NCCL pip install --no-cache-dir horovod==0.19.*

# 运行
## 单机多卡
```$ horovodrun -np 4 -H localhost:4 python train.py ```
## 多机多卡
```$ horovodrun -np 16 -H server1:4,server2:4,server3:4,server4:4 python train.py ``` 
