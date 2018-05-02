def binary_search(arr, val):
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        mid = (lo + hi) / 2
        if val == arr[mid]:
            return mid
        elif val < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


arr1 = [1,3,8,10,123, 268, 269]
val1 = 10
out1 = 3

arr2 = [1,3,8,10,123, 268, 269]
val2 = 11
out2 = -1

assert binary_search(arr1, val1) == out1
assert binary_search(arr2, val2) == out2
