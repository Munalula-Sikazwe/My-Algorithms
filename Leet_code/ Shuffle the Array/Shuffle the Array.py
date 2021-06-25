class Solution:
    def shuffle(self, nums, n: int) :
        array1 = nums[:n]
        array2 = nums[n:]
        shuffled_array = []
        for index in range(n):
            shuffled_array.append(array1[index])
            shuffled_array.append(array2[index])
        return shuffled_array
