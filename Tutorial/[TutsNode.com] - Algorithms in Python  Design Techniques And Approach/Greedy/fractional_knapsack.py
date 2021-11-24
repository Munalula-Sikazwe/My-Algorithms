wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50


def get_max_value(wt, val, capacity):
    items = [0] * len(wt)
    for i in range(0, len(wt)):
        items[i] = Item(wt[i], val[i], i)
    total_value = 0
    items.sort(reverse=True)
    for item in items:
        print(total_value, item.wt, item.val,capacity)
        cur_wt = item.wt
        cur_val = item.val

        if capacity - cur_wt >= 0:
            capacity -= cur_wt
            total_value += cur_val
        else:
            total_value += cur_val * (capacity / cur_wt)
            break
    return total_value


class Item:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


print(get_max_value(wt, val, capacity))
