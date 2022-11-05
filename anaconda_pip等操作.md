# 1. Anaconda
## 1.1 常用操作
### 1.1.1 添加清华源
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
```
### 1.1.2 查看已有源
```
conda config --show-sources
```
### 1.1.3 移除源
```
conda config --remove channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
```
### 1.1.4 创建环境
```
conda create -n 虚拟环境名字 python==3.7 -y
```

### 1.1.5 删除环境
```
conda remove -n 虚拟环境名字 --all
```

### 1.1.6 更新基础conda环境
```
conda update -n base -c defaults conda
```
## 1.2. conda源

# 2. pip
## 2.1 常用操作
## 2.2 pip源
### https://pypi.tuna.tsinghua.edu.cn/simple (清华)
### https://repo.huaweicloud.com/repository/pypi/simple (华为)

# 3. ubuntu源
