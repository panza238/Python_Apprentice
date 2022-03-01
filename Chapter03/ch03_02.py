from urllib.request import urlopen
import sys

default_url = 'http://sixty-north.com/c/t.txt'


def fetch_words(url):
    """gets words from a website and returns them in a list"""
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_words(story_words):
    """print list of words"""
    for word in story_words:
        print(word)


# By putting everything inside a main() function, we can import this function and test it from the REPL!
def main(url):
    # Run functions
    words = fetch_words(url)
    print_words(words)


if __name__ == "__main__":
    # define URL
    url = default_url if (len(sys.argv) < 2) else sys.argv[1]
    # run main
    main(url)
