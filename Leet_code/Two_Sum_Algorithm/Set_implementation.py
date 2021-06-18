class Solution:
    def twoSum(self, nums, target) :
        seen = set()
        for index, number in enumerate(nums):
            current_target = target - number
            for seen_index, seen_number in seen:
                if seen_number == current_target:
                    return [index, seen_index]




            else:
                seen.add((index, number))
