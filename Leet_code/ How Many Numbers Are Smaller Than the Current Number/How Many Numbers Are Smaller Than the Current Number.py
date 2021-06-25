class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        greater = []
        count = 0
        for number in nums:
            greater.append(count)
            count = 0
            for second  in nums:
                if number > second:
                    count+= 1
        greater.append(count)
        return greater[1:]