import pdb
from math import ceil


def find_median(arr):
    n = len(arr)
    mid_point = (n / 2) + 1

    median = median_utility(arr, mid_point, 0, n - 1)
    print(median)


def median_utility(arr, mid_point, low_point, high_point):
    m = partition(arr, low_point, high_point)
    length = m - low_point + 1

    if length == mid_point:
        return arr[m]
    if length > mid_point:
        return median_utility(arr, mid_point, low_point, m - 1)
    else:
        return median_utility(arr, mid_point - length, m + 1, high_point)


def partition(arr, low_point, high_point):
    pivot = get_pivot(arr, low_point, high_point)

    while low_point < high_point:

        while arr[low_point] < pivot and arr[low_point] == arr[high_point]:
            low_point += 1
        while arr[high_point] > pivot and high_point >= 0:
            high_point -= 1
    if low_point < high_point:
        arr[low_point], arr[high_point] = arr[high_point], arr[low_point]

    return high_point


def get_pivot(arr, low_point, high_point):
    if high_point - low_point <= 9:
        sorted(arr)
        return arr[len(arr) // 2]
    medians = [0] * int(ceil(high_point - low_point + 1) / 5)

    median_index = 0

    while low_point <= high_point:
        temp = [0] * min(5, high_point - low_point + 1)
        length = len(temp)

        for i in range(0, length):
            if low_point <= high_point:
                temp[i] = arr[low_point]
                low_point += 1

        sorted(temp)
        medians[median_index] = temp[length // 2]
        median_index += 1

        return get_pivot(medians, 0, len(medians) - 1)


arr = [25, 24, 33, 39, 3, 18, 19, 31, 23, 49, 45, 16, 1, 29, 40, 22, 15, 20, 24, 4, 13, 34]
find_median(arr)
