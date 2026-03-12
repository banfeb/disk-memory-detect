![dmd](./assets/dmd.png)



<h1 align="center">DMD - Disk Memory Detector</h1>



`DMD` (Disk Memory Detector) 是一个功能强大的 Python 命令行工具，用于 检测磁盘文件大小、分析文件夹变化趋势、自动清理旧日志文件。它通过递归扫描文件夹、比较不同时间点的状态变化，帮助用户找出磁盘空间增长最快的目录，从而更好地管理磁盘空间。

- 当初次扫描时，只能统计前n天前的增加目录。
- 不是第一次扫描目录时，比较两次状态变化，找出空间增长最快的目录。



# 开始使用



## 安装

```powershell
// 打开终端cmd
git clone https://github.com/banfeb/disk-memory-detect.git
```



## 运行

进入工作目录

```cmd
cd disk-memory-detect
```

创建虚拟python环境或者激活已经存在的python环境

```cmd
// 创建python虚拟环境
python -m venv .venv
// 激活虚拟环境(powershell需要管理员权限)
.venv\Scripts\activate
// powershell的管理员权限命令
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

安装相关包

```
pip install -e .
```

运行命令

```cmd
// dmd run F:/F_Disk/projects/langchain_learn --topn 5 --minsize 0
dmd run [dir_path] [options]
```



| 参数               | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| `dir_path`         | 位置参数，需要扫描的磁盘，使用 `/`，比如`C:/`                |
| `--topn`           | 可选参数，显示变化最大的前 N 个目录                          |
| `--minsize`        | 可选参数，忽略小于指定大小（单位：字节）的变化               |
| `-- lookback_days` | 可选参数，当初次扫描磁盘时，检索前lookback_days天内增加文件夹 |



# 未来开发

- 通过监听避免每次扫盘
- 开发图形界面

