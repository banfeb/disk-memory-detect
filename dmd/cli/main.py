import argparse
from dmd.logger import get_logger

logger = get_logger(__name__)

def main():
    import dmd.cli.run
    CMD_MODULES = [dmd.cli.run]
    parser = argparse.ArgumentParser(
        description="dmd CLI"
    )
    subparsers = parser.add_subparsers(required=False, dest='subcommand')
    cmds = {}
    for cmd_module in CMD_MODULES:
        new_cmds = cmd_module.cmd_init()
        for cmd in new_cmds:
            cmd.subparser_init(subparsers).set_defaults(dispatch_function=cmd.cmd)
            cmds[cmd.name] = cmd
    args = parser.parse_args()
    if args.subcommand in cmds:
        cmds[args.subcommand].validate(args)
    if hasattr(args, 'dispatch_function'):
        args.dispatch_function(args)
if __name__ == "__main__":
    main()