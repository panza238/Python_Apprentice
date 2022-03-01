from urllib.request import urlopen


# I can import this function from another script and use it freely
def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    for word in story_words: print(word)
    # print(undefined_var)  # This will fail ONLY when the function is executed. Not when the module is imported


# This will print the name of this file when imported. If it's being run directly, it will print "__main__"
print(__name__)
