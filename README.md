![dmd](./assets/dmd.png)



<h1 align="center">DMD - Disk Memory Detector</h1>



`DMD` (Disk Memory Detector) is a powerful Python command-line tool used for detecting disk file sizes, analyzing folder change trends, and automatically cleaning up old log files. It helps users identify the directories with the fastest disk space growth by recursively scanning folders and comparing status changes at different time points, thereby better managing disk space.

- When scanning for the first time, it can only count the increased directories from the past n days.
- When not scanning the directory for the first time, it compares changes between two states to identify the directories with the fastest space growth.



# Getting Started



## Installation

```powershell
// Open terminal cmd
git clone https://github.com/banfeb/disk-memory-detect.git
```



## Running

Enter the working directory

```cmd
cd disk-memory-detect
```

Create a virtual Python environment or activate an existing one

```cmd
// Create Python virtual environment
python -m venv .venv
// Activate virtual environment (PowerShell requires administrator privileges)
.venv\Scripts\activate
// PowerShell administrator privilege command
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Install related packages

```
pip install -e .
```

Run command

```cmd
// dmd run F:/F_Disk/projects/langchain_learn --topn 5 --minsize 0
dmd run [dir_path] [options]
```



| Parameter          | Description                                                     |
| ------------------ | --------------------------------------------------------------- |
| `dir_path`         | Positional parameter, the disk to scan, use `/`, e.g. `C:/`      |
| `--topn`           | Optional parameter, display the top N directories with the largest changes |
| `--minsize`        | Optional parameter, ignore changes smaller than the specified size (in bytes) |
| `-- lookback_days` | Optional parameter, when scanning the disk for the first time, retrieve folders added within the past lookback_days |