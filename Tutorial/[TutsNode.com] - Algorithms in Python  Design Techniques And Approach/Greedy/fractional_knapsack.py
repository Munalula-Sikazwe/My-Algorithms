wt = [10, 40, 20, 20]
val = [60, 40, 100, 120]
capacity = 50


def get_max_value(wt, val, capacity):
    items = [0] * len(wt)
    for i in range(0, len(wt)):
        item[i] = Item()


class Item:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost
