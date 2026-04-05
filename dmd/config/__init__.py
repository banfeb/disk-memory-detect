import argparse
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Optional


@dataclass(frozen=True)
class SaveConfig:
    """保存的相关配置"""
    dir_path: str = "./history"
    """保存的文件夹路径"""
    max_retention_days: int = 30
    """扫盘得到的详细最长保存的天数"""


@dataclass(frozen=True)
class RunnerConfig:
    """运行(检索)的相关配置"""
    dir_path: str = "C:/"   # F:/F_Disk/projects/langchain_learn, F:/
    """
      传入"F:\\"，会被解析为F:\进行扫盘并保存，因而保存为F:\\
      传入r"F:\\"，会被解析为F:\\进行扫盘，因而保存为F:\\\\
    """
    """检索的文件夹路径"""
    top_n: int = 3
    """显示增加内容最多的文件夹数目"""
    min_size: int = 0
    """文件夹增加的最小大小"""
    lookback_days: int = 365
    """检索的时间范围，单位天"""


@dataclass(frozen=True)
class Config:
    SC: SaveConfig = field(default_factory=SaveConfig)
    RC: RunnerConfig = field(default_factory=RunnerConfig)
    @classmethod
    def from_env(cls, args: Optional[argparse.Namespace] = None) -> "Config":
        sv = SaveConfig()
        if args is None:
            rc = RunnerConfig()
        else:
            rc = RunnerConfig(
                dir_path=args.dir_path if args.dir_path is not None else RunnerConfig.dir_path,
                top_n=args.topn if args.topn is not None else RunnerConfig.top_n,
                min_size=args.minsize if args.minsize is not None else RunnerConfig.min_size,
                lookback_days=args.lookback_days if args.lookback_days is not None else RunnerConfig.lookback_days)
        return cls(sv, rc)


#@lru_cache()
def get_config(args: Optional[argparse.Namespace] = None) -> Config:
    return Config.from_env(args)