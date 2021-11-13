def partition(arr, lb, ub):
    pivot = arr[lb]
    left = lb
    right = ub

    while left < right:

        while arr[left] <= pivot and left < len(arr) - 1:
            left += 1
        while arr[right] >= pivot and right > 0:
            right += 1

        while left < right:
            arr[right], arr[left] = arr[left], arr[right]

    arr[lb], arr[right] = arr[right], arr[lb]

    return right


def quick_sort(arr, lb, ub):
    if lb < ub:
        index = partition(arr, lb, ub)
        quick_sort(arr, lb, index - 1)
        quick_sort(arr, index + 1, ub)
