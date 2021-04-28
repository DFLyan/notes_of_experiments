### tar -zxvf openssl-1.1.0k.tar.gz

### 编译安装
cd openssl-1.1.0k
sudo ./config
sudo make install

### 删除旧版本
sudo rm /usr/bin/openssl

### 建立新的软连接
sudo ln -s /usr/local/bin/openssl /usr/bin/openssl

### 如果报错
sudo cp libssl.so.1.1 /lib/x86_64-linux-gnu<br>
sudo cp libcrypto.so.1.1 /lib/x86_64-linux-gnu　　
