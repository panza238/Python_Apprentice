"""This module creates a directory.
Also, it is meant to explain the functionality of the finally statement."""
import os
import sys


def make_dir(name: str, path=None):
    """Creates directory in a specified path
    Args:
        name: Directory name (str)
        path: path in which the directory should be created
    Returns:
        None"""

    current_dir = os.getcwd()
    if not path:
        path = current_dir

    try:
        os.chdir(path)
        os.mkdir(name)
    except OSError as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        raise
    finally:
        print("This runs even if it fails")
        os.chdir(current_dir)

