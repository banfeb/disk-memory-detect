import argparse

from dmd.logger import get_logger

logger = get_logger(__name__)
def main():
    parser = argparse.ArgumentParser(description='dmd CLI')
    subparsers = parser.add_subparsers(title='subcommand', dest='subcommand', required=True)
    run_parser = subparsers.add_parser('run', help='执行程序')
    run_parser.add_argument('dir_path', help='检索文件夹路径')
    run_parser.add_argument('--topn',
                            type=int,
                            default=3,
                            help='结果显示的文件夹数量')
    run_parser.add_argument('--minsize',
                            type=int,
                            default=0,
                            help='文件夹增加的最小大小')

    args = parser.parse_args()
    if args.subcommand == 'run':
        print(args.dir_path)
        print(args.topn)
        print(args.minsize)
if __name__ == "__main__":
    main()