from collections import defaultdict


class Solution:
    def restoreString(self, s: str, indices: [int]) -> str:
        list1, list2 = zip(*sorted(zip(indices, s)))
        return ''.join(list2)
