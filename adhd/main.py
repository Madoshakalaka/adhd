import argparse
import sys


def ensure_daemon():
    """
    ensure adhd is running in the background
    """
    pass


def cmd_entry(argv=sys.argv):
    """
    """

    # todo: fill command line functionality

    ensure_daemon()

    parser = argparse.ArgumentParser(description="keep somebody focused on work")

    subparsers = parser.add_subparsers(dest="command_name", required=True)

    intensify_parser = subparsers.add_parser(
        "intensifies", help="run adhd at background at startup"
    )

    for_parser = subparsers.add_parser("for", help="start monitoring")

    for_parser.add_argument(
        "duration",
        help="Duration of the monitoring. Formats like 30m or 1h are supported",
    )

    argv = parser.parse_args(argv[1:])

    if argv.command_name == "for":
        start_monitoring(argv.duration)
    else:
        pass


def start_monitoring(duration):
    """
    try to connect to
    """
    pass


if __name__ == "__main__":
    # run at startup
    pass
