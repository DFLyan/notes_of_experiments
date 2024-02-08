### 无法获得锁
```
ps aux | grep "apt-get"
sudo kill ...
或者
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock
```

### Anaconda安装
bash A...sh

### pip安装
sudo apt-get install python-pip python-dev

### bazel安装
```
sudo apt-get install openjdk-8-jdk
(sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update && sudo apt-get install oracle-java8-installer)
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install bazel
sudo apt-get upgrade bazel
```

### cuda安装
sudo sh cuda_....

### 配置cuda路径
```
vim ~/.bashrc
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:/usr/local/cuda-8.0/extras/CUPTI/lib64:$LD_LIBRARY_PATH
export CUDA_HOME=/usr/local/cuda-8.0
export PATH=/usr/local/cuda-8.0/bin:$PATH
source ~/.bashrc
```

### 解压cudnn文件并安装
```
cp  cudnn-8.0-linux-x64-v5.1.solitairetheme8 cudnn-8.0-linux-x64-v5.1.tgz
cd /usr/local
```

### 查看进程及对应文件夹
```
sudo cd /proc/pid
sudo ls -l exe
sudo tar -xzvf ~/downloads/cudnn-.....tgz
```

### 安装GPU版
```
export TF_BINARY_URL=http://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.0.0rc0-cp35-cp35m-linux_x86_64.whl
pip install --upgrade $TF_BINARY_URL
(出现版本出错,查看python版本是否对应)
pip install --upgrade --ignore-installed setuptools  //如果出现setuptools问题，升级版本
```

若是不兼容，进行源码编译
```
wget http://github.com/tensorflow/tensorflow/archive/v1.0.0-rc0.tar.gz
tar -xzvf v...
```

### 测试
```
import tensorflow as tf
hello=tf.constant('Hello, TensorFlow')
sess=tf.Session()
print(sess.run(hello))
```

### 升级
pip install --upgrade tensorflow

```
Python版本的切换
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150
或者查看Python然后输入对应序号进行切换
sudo update-alternatives --config python


出现：Intel MKL FATAL ERROR: Cannot load libmkl_avx2.so or libmkl_def.so
conda install nomkl numpy scipy scikit-learn numexpr

pip install easydict  //安装easydict

module 'pandas' has no attribute 'computation'解决办法
pip install --upgrade pandas
pip install --upgrade dask
```

### 建立软链接
```
sudo rm -rf /usr/local/cuda
sudo ln -s /usr/local/cuda-8.0/ /usr/local/cuda
```

### 子进程 已安装 post-removal 脚本 返回错误状态 1
```
cd /var/lib/dpkg
sudo mv info info.bak
sudo mkdir info
```

### 服务器添加新用户
```adduser jenny --home /ssd/jenny```
```
sudo vim /etc/sudoers
# User privilege specification
root    ALL=(ALL:ALL) ALL
jwchen  ALL=(ALL:ALL) ALL
jenny   ALL=(ALL:ALL) ALL
```

### 如果用户有root权限，修改root账户的密码
sudo passwd root

### 删除用户
sudo userdel -r username（如果没有-r，只会删除用户，不会删除对应的用户文件夹）

## 修改用户根目录
```
vim /etc/passwd
```
修改对应用户的目录即可

### 修改用户根目录后出现/usr/bin/xauth: timeout in locking authority file /home/sam/.Xauthority,原因userA对/home/userA目录没有写权限 
```
sudo chown userA:userA -R /home/userA
通过这方式也可以使得用户对非根目录下的文件夹获取读写权限
```
### 修改用户根目录后登录后不直接是anaconda的base环境（不确定是机器原因还是别的，只有治标的方法）
```
source ~/.bashrc
```

### 105号机重启硬盘挂载掉线
```
sudo fdisk -l   查看待挂载的硬盘设备
sudo mount /dev/sda /ssd/   挂载到文件夹
```

### 网络配置
```
sudo vim /etc/netplan/01-netcfg.yaml
或者 /etc/network/inter...
10.20.221.253
10.20.232.47
```

### 查看服务器端某文件夹
```
python3 -m http.server 8080
服务器地址：8080
```

### pip超时
pip --default-timeout=100 install  Pillow

### titanXP的pytorch配置
```
直接安装torchvision 0.5.0，会自动安装1.4版本
cuda版本9.0可以跑起来
```

### 缺少google module
pip install protobuf

### 查看id相对应的文件及目录
```
sudo cd /proc/3093
sudo ls -l exe
```

### 禁止root远程登录
```
/etc/ssh/sshd_config中permitrootlogin改为no
service ssh restart
```

### gcc和g++软连接
```
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 80 --slave /usr/bin/g++ g++ /usr/bin/g++-5
（通过以上建立gcc和g++之间的关系，然后通过下面设置好gcc的优先级之后，只要切换gcc，g++也能跟着切换）
或者

sudo update-alternatives --install /usr/bin/gcc(g++) gcc(g++) /usr/bin/gcc-5 100(100为优先级）
sudo update-alternatives --config gcc(g++)（手动选择）
```

### 关闭客户端不打断进程
```
nohup python -u ....py >>logname.out & (之前有一次出现过关闭还停止，但忘了是什么情况了，最后还是解决了，如果遇到以后再补充)
tail -f logname.out(查看)
```

### apt源
cd /etc/apt/sources.list.d/ （进入后ls，查看，.list.bak是备份）

### 修改github的IP，能ping通
（修改 /etc/hosts）
sudo vim /etc/hosts
(更新一下hosts)
source /etc/hosts

### Sub-process /usr/bin/dpkg returned an error code (1)
**治标不治本，还会有重复的情况出现，只能不停的重复**
```
cd /var/lib/dpkg/
sudo mv info/ info_bak          # 现将info文件夹更名
sudo mkdir info                 # 再新建一个新的info文件夹
sudo apt-get update             # 更新
sudo apt-get -f install         # 修复
sudo mv info/* info_bak/        # 执行完上一步操作后会在新的info文件夹下生成一些文件，现将这些文件全部移到info_bak文件夹下
sudo rm -rf info                # 把自己新建的info文件夹删掉
sudo mv info_bak info           # 把以前的info文件夹重新改回名
```
### hash mismatch
产生原因：
所使用的网络供应商，有些会设置一些透明缓存，以增加网络内部速度，减少出口的流量，所获取的某些文件不是源服务器上的真正文件，是从缓存中获取的，当缓存中获取的一些校验信息跟源中不一致的时候，自然提示校验失败，无法继续更新。
```
1）删掉/var/lib/apt/lists 这个目录下的东西
sudo rm -fR /var/lib/apt/lists/*
2）新建相应文件夹
sudo mkdir /var/lib/apt/lists/partial
3）重新update
sudo apt-get update
```

### 命令打开软件与更新
sudo software-properties-gtk

### [dpkg报错](https://blog.csdn.net/dou3516/article/details/105120221/)--dpkg: error processing package *** (--configure)

### 查看文件夹大小
```
du -h --max-depth=1
```

### 两个文件夹合并
cp -rp 源目录/* 合并目录/

参数说明：/*是拷贝目录下所有内容，不拷贝“源目录”名

参数说明：
-r 递归复制，包含目录   
-p 保持新文件的属性不变   

其他参数说明：
-f 强制覆盖，不询问yes/no（-i的默认的，即默认为交互模式，询问是否覆盖）   
-a 做一个备份，这里可以不用这个参数，我们可以先备份整个test目录   

### 批量解压
```
for tar in *.tar;do tar xvf $tar;done
```
### g++/gcc版本更改
```
update-alternatives --config g++
```
