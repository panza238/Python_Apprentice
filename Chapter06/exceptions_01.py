"""A module to demonstrate how exceptions work"""
import sys


# call dir() on this function to inspect it!
def convert_to_int(s):
    """This is the preferred Docstring style
    Args:
        s: element to convert to int
    Returns:
        None"""
    try:
        converted = int(s)
        print("Conversion OK!", converted)
        return converted
    except (ValueError, TypeError) as ex:
        print(f"Conversion failed! Info on the error:\n{str(ex)}\n",
              file=sys.stderr)  # file=sys.stderr prints everything to the stderr output
        raise  # raise raises the exception and stops excecution
