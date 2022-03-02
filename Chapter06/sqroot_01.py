"""A module to demonstrate exception handling.
To this end the module will contain a function that calculates the square root of numbers"""


def sqrt(input_num):
    """Calculates the square root of a given number
    Args:
        input_num: number. int or float
    Returns:
        sqrt: square root of the number"""

    if input_num < 0:
        raise ValueError("Cannot compute the square root of a negative number!")

    current = input_num
    i = 0
    while ((current ** 2) != input_num) and (i < 20):
        current = (current + input_num / current) / 2.0
        i += 1
    return current


def main():
    print(sqrt(2))
    print(sqrt(9))
    print(sqrt(19))
    print(sqrt(-4))


if __name__ == "__main__":
    main()