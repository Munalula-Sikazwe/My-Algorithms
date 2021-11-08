def merge(leftside, rightside, arr):
    i = 0
    j = 0
    length_of_leftside = len(leftside)
    length_of_rightside = len(rightside)
    while 0 <= i < length_of_leftside and 0 <= i < length_of_rightside:
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
    while i < length_of_rightside:
        arr.append(rightside[j])
        j += 1
