def merge(leftside, rightside, arr):
    i = 0
    j = 0
    length_of_leftside = len(leftside)
    length_of_rightside = len(rightside)

    while 0 <= i < length_of_leftside and 0 <= j < length_of_rightside:
        if leftside[i] < rightside[j]:
            arr.append(leftside[i])
            i += 1
        else:
            if leftside[i] > rightside[j]:
                arr.append(rightside[j])
                j += 1

    while i < length_of_leftside:
        arr.append(leftside[i])
        i += 1
    while j < length_of_rightside:
        arr.append(rightside[j])
        j += 1


def merge_sort(arr):
    sorted_arr = []
    length_of_array = len(arr)
    if length_of_array == 1:
        return arr
    middle_value = length_of_array // 2

    leftside = arr[:middle_value]
    rightside = arr[middle_value:]

    leftside = merge_sort(leftside)
    rightside = merge_sort(rightside)
    print(leftside)
    print(rightside)
    merge(leftside, rightside, sorted_arr)

    return sorted_arr


print(merge_sort([2, 4, 3]))
