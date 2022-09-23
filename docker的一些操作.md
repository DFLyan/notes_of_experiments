### docker的默认的安装位置在主文件夹，如果需要修改iamge保存路径，如下进行：
```
sudo service docker stop
sudo vi /lib/systemd/system/docker.service
```
修改相关文字：
```
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock --graph="/home/xiaoyuanzi/python/Docker" --storage-driver=overlay
ExecReload=/bin/kill -s HUP $MAINPID
```
保存退出后：
```
sudo systemctl daemon-reload
sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl status docker
sudo docker info
```

### 每次都要sudo的解决办法
1.创建docker组：sudo groupadd docker
2.将当前用户加入docker组：sudo gpasswd -a ${USER} docker
3.重启服务：sudo service docker restart
4.刷新docker成员：newgrp - docker

### 改名（通过ID重新创建一个新的镜像）
docker images
docker image tag ID newname

### 停止
docker stop ID

### 查看端口
netstat -aptn

### 端口映射
docker run -t -p 8080:80 nginx

### 外部ssh连接（主要思路为打开端口供外部ssh访问：镜像-->本地端口eg:0.0.0.0:2367-->连接外部的端口eg:22-->外部即可通过用户名@服务器ip进行访问）
docker run -t -P --expose 22 --name server 镜像名字
docker ps (查看端口port）
之后，可通过pycharm中的环境添加里，ssh选项，填写服务器的ip地址，即可访问镜像

### 开始/关闭/删除所有容器
docker start/stop/rm $(docker ps -a | awk '{ print $1}' | tail -n +2)
