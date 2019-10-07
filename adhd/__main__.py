"""
it's possible that `entry_points` in setup.py fail to create a command line entry
e.g. on windows when <python_dir>/Scripts is not in system path

this file gives an alternative of using `python -m adhd`
"""
from adhd.main import cmd_entry


if __name__ == '__main__':
    cmd_entry()
