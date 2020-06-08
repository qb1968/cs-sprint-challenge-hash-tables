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

    print(get_indices_of_item_weights([4,6,10,15,16],5,21))