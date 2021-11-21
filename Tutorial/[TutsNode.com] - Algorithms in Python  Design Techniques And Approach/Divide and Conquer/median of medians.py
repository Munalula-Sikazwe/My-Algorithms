from math import ceil


def find_median(arr):
    n = len(arr)
    mid_point = (n / 2) + 1

    median = median_utility(arr, mid_point, 0, n)
    print(median)


def median_utility(arr, mid_point, low_point, high_point):
    m = partition(arr, low_point, high_point)


def partition(arr, low_point, high_point):
    pivot = get_pivot(arr, low_point, high_point)

    while low_point < high_point:
        while arr[low_point] < pivot and arr[low_point] == arr[high_point]:
            low_point += 1
        while arr[high_point] > pivot:
            high_point -= 1
    if low_point < high_point:
        arr[low_point], arr[high_point] = arr[high_point], arr[low_point]

    return high_point


def get_pivot(arr, low_point, high_point):
    medians = [0] * int(ceil(high_point - low_point + 1) / 5)

    median_index = 0

    while low_point <= high_point:
        temp = [0] * min(5, high_point - low_point + 1)
