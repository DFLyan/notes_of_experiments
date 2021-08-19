# docker hub：镜像社区

### 查看
```
docker version
docker container ls（只显示已经开启的，ls官方推荐）
docker container ps -a（显示所有，-a起作用）
```

### 创建
```
docker container run ${镜像名字}
```

### 停止
```
docker container stop ${ID}(ID每次重启后都会变化）
```

### 删除
```
docker container rm ${ID}
```

