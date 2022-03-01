# Demonstration:

m = [1, 2, 3]
print(m)


def replace_list(k):
    k = [4, 5, 6]
    print(k)


if __name__ == "__main__":
    replace_list(m)
    print(m)
    # m DOES NOT CHANGE. k referred to the same object when the function was invoked
    # but in the first line of the function, k's reference is changed, and is now pointing at a new object
    # This all happens in the local scope of the function.
    # So, k and m originally pointed at the same object,
    # then k pointed at a new one, but m's reference did not change
