# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1
    middle = (start + end) // 2

    if target == arr[middle]:
        return middle
    elif target < arr[middle]:
        return binary_search(arr, target, start, middle - 1)
    else:
        return binary_search(arr, target, middle + 1, end)

    # while begin <= end:
    #     middle = (begin + end) // 2
    #     if target == arr[middle]:
    #         return middle
    #     elif target < arr[middle]:
    #         end = middle - 1
    #     else:
    #         begin = middle + 1
    #
    # return -1


a = [2, 6, 4, 7, 1, 5, 8, 9, 12]
target = 7
result = binary_search(a, target, 0, len(a)-1)
print(result)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    pass
