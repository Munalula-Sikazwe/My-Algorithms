from math import floor


def get_area(area):

    result = []

    while area > 0:
        largest_square_root = floor(area ** 0.5)
        occupied_area = largest_square_root ** 2
        result.append(occupied_area)
        area -= occupied_area
    return result

print(get_area(12))