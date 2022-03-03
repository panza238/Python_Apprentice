"""Module to explain how generators work!"""
# Generators ARE Iterators
# generators generate iterators


def gen246():
    print("Yielding 2!")
    yield 2
    print("Yielding 4!")
    yield 4
    print("Yielding 6!")
    yield 6


# Create a new iterator
h = gen246()
