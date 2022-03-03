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
# Create another generator
g = gen246()

for i in range(4):
    try:
        print(next(h))
    except StopIteration:
        print("generator depleted!\n")


# Once created, generators are INDEPENDENT from each other. They ARE different objects!
print("meanhile, gen g = ", next(g))
