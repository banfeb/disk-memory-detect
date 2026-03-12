import argparse
import time
import mmh3
from dmd.cli.types import CLISubcommand
from dmd.config import get_config
from dmd.directory_usage_tracker import DirectoryUsageTracker
from dmd.file_manager.json_file_manager import TimesJSONFileManager
from dmd.logger import get_logger

logger = get_logger(__name__)

class RunSubCommand(CLISubcommand):
    name = "run"
    @staticmethod
    def cmd(args: argparse.Namespace) -> None:
        # 加载基本配置
        logger.info("开始加载配置文件")
        config = get_config(args)
        save_path = config.SC.dir_path
        save_prefix = str(mmh3.hash(config.RC.dir_path))
        # 加载history目录下最后保存的记录
        file_manager = TimesJSONFileManager(save_path, prefix=save_prefix)
        old_folder_tree = file_manager.load()
        if old_folder_tree is None:
            logger.info("未检测到历史记录，首次执行扫描")
            start_time = time.time()
            tracker = DirectoryUsageTracker(config)
            tracker.get_add_of_folders()
            logger.info(f"扫描完成，运行时间: {(time.time() - start_time):.2f}秒")
            file_manager.save(tracker.new_folders_tree)
            print(tracker)
        else:
            logger.info("检测到历史记录，执行扫描并对比变化")
            start_time = time.time()
            tracker = DirectoryUsageTracker(config)
            logger.info(f"扫描完成，运行时间: {(time.time() - start_time):.2f}秒")
            start_time = time.time()
            result = tracker.get_change_of_folders(old_folder_tree)
            logger.info(f"对比完成，运行时间: {(time.time() - start_time):.2f}秒")
            file_manager.save(tracker.new_folders_tree)
            print(tracker)

    def validate_args(self, args: argparse.Namespace) -> None:
        pass

    def subparser_init(self, subparsers: argparse._SubParsersAction) -> argparse.ArgumentParser:
        run_parser = subparsers.add_parser(
            self.name,
            help="通过检索方式运行程序",
            usage="dmd run [dir_path][options]"
        )
        run_parser.add_argument('dir_path', help='检索文件夹路径')
        run_parser.add_argument('--topn',
                                type=int,
                                default=3,
                                help='结果显示的文件夹数量')
        run_parser.add_argument('--minsize',
                                type=int,
                                default=0,
                                help='文件夹增加的最小大小')
        run_parser.add_argument('--lookback_days',
                                type=int,
                                default=7,
                                help='检索前lookback_days到现在增加文件')
        return run_parser



def cmd_init() -> list[CLISubcommand]:
    return [RunSubCommand()]