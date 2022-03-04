""" with keyword!"""
import sys
from urllib.request import urlopen


def main(filename):
    """Two context managers"""
    with open(filename, mode='rt', encoding='utf-8') as f:
        print([num.strip() for num in f])

    with urlopen("http://sixty-north.com/c/t.txt") as web_file:
        print([len(line) for line in web_file])


if __name__ == '__main__':
    main(sys.argv[1])
