
def rotLeft(a, d):
    # Write your code here
    rotated_array = []
    count = 0
    while count < d:
        for index, element in enumerate(a):
            if index == 0:
                rotated_array.insert(len(a) - 1, element)
            else:
                rotated_array.insert(index - 1, element)
        count += 1
        a = list(rotated_array)
        rotated_array = []
    return a


