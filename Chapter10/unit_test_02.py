"""text analyzer function"""


def analyze_text(filename):
    """Calculate the number of lines and characters in a file.
    Args:
        filename = path to the text file to analyze
    Returns
        file_length = number of lines in the file
        character_count = number of characters in the file."""
    with open(filename, mode="rt", encoding="utf-8") as file:
        file_length = 0
        character_count = 0
        for line in file:
            character_count += len(line)
            file_length += 1

    return file_length, character_count
