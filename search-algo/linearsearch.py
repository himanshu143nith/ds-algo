def linear_search(arr, x):
    """
    Searches for the element x in the given array arr using linear search algorithm.
    
    Returns the index of the element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Test cases
assert linear_search([1, 2, 3, 4, 5], 3) == 2
assert linear_search([1, 2, 3, 4, 5], 6) == -1
assert linear_search([], 1) == -1
assert linear_search([1], 1) == 0
assert linear_search([1, 1, 1], 1) == 0
