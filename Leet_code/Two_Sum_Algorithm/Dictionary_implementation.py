from collections import defaultdict


class Solution:
    def twoSum(self, nums, target) :
        seen = defaultdict()
        for index, number in enumerate(nums):
            current_target = target - number
            if current_target in seen:
                return [index, seen[current_target]]





            else:
                seen[number] = index
