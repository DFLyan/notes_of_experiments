```
mkdir ~/matlab        //用户主目录下新建文件夹 matlab
sudo mount -o loop MatlabR2018b_LinX64_disk1_Downloadly.ir.iso ~/matlab    //将 iso1 文件挂载在 ~/matlab 目录下
sudo ~/matlab/install        //执行安装程序
sudo umount /dev/loop5      //用df -h查看挂载在哪，然后卸载
sudo mount -o loop MatlabR2018b_LinX64_disk2_Downloadly.ir.iso ~/matlab    //将 iso 文件挂载在 ~/matlab 目录下
sudo apt install matlab-support    //安装 matlab-support，地址默认为/usr/local/MATLAB/R2018b
sudo cp -rvf R2018a/bin /usr/local/MATLAB/R2018b/        //将 Crack 文件夹下 bin 文件内容复制到 Matlab 安装目录下
sudo chown -R user_name ~/.matlab    //修改上述目录的所有者为当前用户
```
激活选择.lic文件\
iso的名字会有所不同，只要先挂载1，安装的时候提示换牒，卸载再挂载2在同一文件夹下即可
