## 一 报错与警告
### 1.1 dpkg: warning: files list file for package（apt install的时候可能会出现）[参考博客](https://blog.csdn.net/youlinhuanyan/article/details/99575493)
先把警告都复制下来，创建“warning.txt”文件，复制进去；同一文件夹下，创建“autoinstall”脚本文件，内容为：
```
#!/bin/bash
i=1
for package in $(cat warning.txt | grep "dpkg: warning: files list file for package " | grep -Po "'[^']*'" | sed "s/'//g")；
do
  echo "No.${i} ==================start intall ${package}==================="
  apt-get install --reinstall "$package" -y;
  #如果没有安装aptitude, 则可以用apt-get --reinstall "$package";
  i=`expr $i + 1`
done
```
终端输入指令，启动脚本，重新安装这些包：
```
sudo chmod 777 autoinstall
sudo ./autoinstall
```
