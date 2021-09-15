```
mkdir ~/matlab        //用户主目录下新建文件夹 matlab
sudo mount -o loop MatlabR2018b_LinX64_disk1_Downloadly.ir.iso ~/matlab    //将 iso 文件挂载在 ~/matlab 目录下
sudo ~/matlab/install        //执行安装程序
sudo apt install matlab-support    //安装 matlab-support
sudo cp -rvf R2018a/bin /usr/local/MATLAB/R2018b/        //将 Crack 文件夹下 bin 文件内容复制到 Matlab 安装目录下
sudo chown -R user_name ~/.matlab    //修改上述目录的所有者为当前用户
```
激活选择.lic文件
