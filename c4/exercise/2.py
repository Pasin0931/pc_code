def print_map(map):
    """
    Display 2D array by replacing 0 with ., 1 with #, and 2 with X
    :params 2D array contains integer 0,1,2
    :return nothing

    >>> print_map([[1,0],[0,2]])
    #.
    .X
    >>> print_map([[2,2,1],[0,0,0],[1,2,0]])
    XX#
    ...
    #X.
    >>> print_map([[0],[1],[2]])
    .
    #
    X
    """
    for row in map:
        for col in range(len(row)):
            if row[col] == 2:
                row[col] = "X"
            elif row[col] == 1:
                row[col] = "#"
            elif row[col] == 0:
                row[col] = "."
        print("".join(row))

map1 = [[1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 1, 1],
        [0, 2, 0, 1],
        [1, 1, 0, 1]]

map2 = [[1, 1, 1, 1, 0, 0, 0, 1],
        [0, 2, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 2, 1]]

# Show Map 1
print("Map 1")
print_map(map1)
print()

# Show Map 2
print("Map 2")
print_map(map2)
print()