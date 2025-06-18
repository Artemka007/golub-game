def binary_search_left(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def binary_search_right(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left