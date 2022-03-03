"""Module to demonstratingthe difference between iterables and iterators"""
import sys

iterable = ["Autumn", "Winter", "Spring", "Summer"]
iterator = iter(iterable)
# The iterable stores everything in memory. The iterator gets the objects one by one

for idx, item in enumerate(iterable):
    print("Iterable: ", iterable[idx])
    print("Iterator: ", next(iterator))

# Once the iterator has reached the the end, it is gone. It is "already used"
try:
    print(next(iterator))
except StopIteration as e:
    print("No more items is this iterator!", file=sys.stderr)
    # DO NOT RAISE
