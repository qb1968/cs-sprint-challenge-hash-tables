# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    query = {}
    for i in files:
        
        key = i.rsplit('/', 1)[1]
        value = i
        if key not in query:
            query[key] = []

        query[key].append(i)

    result = []
    
    for x in queries:
        if x in query:
            result += query[x]

    return result

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
