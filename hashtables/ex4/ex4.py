def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}
    result = []

    for i in a:
        if storage.get(abs(i)):
            result.append(abs(i))

        else:
             storage[abs(i)] = i   

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
