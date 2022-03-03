"""Module to further explore generators!"""


def take(count, iterable):
    """Take items from the front of an iterable.
    Args:
        count: The maximum number of items to retrieve.
        iterable: The source of the items.
    Yields:
        At most 'count' items from 'iterable'.
    """
    counter = 0  # This counter variable is stored INSIDE the iterator
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    """Runs take function"""
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def distinct(iterable):
    """Return unique items by eliminating duplicates.
    Args:
        iterable: The source of the items.
    Yields:
        Unique elements in order from 'iterable'.
    """
    seen = set()  # This seen set is stored IN the iterator created by the generator.
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)


def run_pipeline():
    """example to run two previous generators as a pipeline."""
    items = [3, 6, 6, 2, 1, 1]
    # NO effort is wasted in this pipeline. distinct never even sees the last two items,
    # because take does not require them
    for item in take(3, distinct(items)):
        print(item)


# Also, there are generator expressions!
thousand_squares = (x * x for x in range(1, 1000))  # Just like a list comprehension!
print(thousand_squares)
print(type(thousand_squares))
for i in range(5):
    print(next(thousand_squares))
