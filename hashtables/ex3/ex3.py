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
    arrays = [[1, 2, 3], [1, 5, 3], [1, 8, 3]]

    

    print(intersection(arrays))
