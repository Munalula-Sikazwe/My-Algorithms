class Solution:
    def runningSum(self, nums):
        current_sum = 0
        running_sum = []
        for index in range(len(nums)):
            current_sum += nums[index]
            running_sum.append(current_sum)
        return running_sum