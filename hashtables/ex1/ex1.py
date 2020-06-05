def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    for x in range(length):
        if limit-weights[x] in dict:
            return [x, dict[limit-weights[x]]]
        dict[weights[x]] = x     

    return None

    
weights_1 = [9]
answer_1 = get_indices_of_item_weights(weights_1, 1, 9)
weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

print(answer_1)
print(answer_4)