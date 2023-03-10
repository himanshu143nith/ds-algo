def main():
    def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

    # Test cases
    arr1 = [1, 3, 5, 7, 9]
    target1 = 5
    assert binary_search(arr1, target1) == 2

    arr2 = [2, 4, 6, 8, 10]
    target2 = 6
    assert binary_search(arr2, target2) == 2

    arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target3 = 10
    assert binary_search(arr3, target3) == -1

    arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target4 = 1
    assert binary_search(arr4, target4) == 0

    arr5 = []
    target5 = 5
    assert binary_search(arr5, target5) == -1

    print("All test cases pass")

if __name__ == '__main__':
    main()
