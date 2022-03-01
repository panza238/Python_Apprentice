# Demonstration:

m = [1, 2, 3]
print(m)


def append_9_to_list(k):
    k.append(9)
    print(k)


if __name__ == "__main__":
    append_9_to_list(m)
    print(m)
    # m has changed, because de local variable k referenced the same object.
