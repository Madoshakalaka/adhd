import argparse
import sys


def cmd_entry(argv=sys.argv):
    # todo: fill command line functionality

    parser = argparse.ArgumentParser(description="keep somebody focused on work")

    # parser.add_argument(
    #     "blah",
    #     action="store",
    #     type=str,
    #     help="blah",
    # )

    argv = parser.parse_args(argv[1:])

    # add your command line program here

    print("reserved command line entry for python package adhd")
