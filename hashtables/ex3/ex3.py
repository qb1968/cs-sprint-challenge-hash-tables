def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    dict = {}
    
    for array in arrays:
        for i in array:
            if i not in dict:
                dict[i] = 1
            else:
                if dict[i] < 2:
                    result.append(i)
                    dict[i] += 1

    return result


if __name__ == "__main__":
    arrays = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]

    

    print(intersection(arrays))
