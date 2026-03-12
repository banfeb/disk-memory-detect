import time
import mmh3
from dmd.config import get_config
from dmd.file_manager.json_file_manager import TimesJSONFileManager
from dmd.logger import get_logger
from dmd.directory_usage_tracker import DirectoryUsageTracker

logger = get_logger(__name__)

def main():
    # 加载基本配置
    logger.info("开始加载配置文件")
    config = get_config()
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

if __name__ == '__main__':
    main()