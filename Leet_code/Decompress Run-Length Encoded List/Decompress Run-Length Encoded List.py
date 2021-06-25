class Solution:
    def decompressRLElist(self, nums: [int]) -> [int]:
        decompressed = []
        for index in range(0,len(nums),2):
            for subindex in range(nums[index]):
                decompressed.append(nums[index+1])
        return decompressed