def get_product_sum(array, depth=1):
    total_sum = 0

    for element in array:
        if isinstance(element, list):
            total_sum += get_product_sum(element, depth + 1)
        else:
            total_sum += element

    return total_sum * depth


print(get_product_sum([1, 2, [2, 3], 6, [[2, 3], 1], 7]))
