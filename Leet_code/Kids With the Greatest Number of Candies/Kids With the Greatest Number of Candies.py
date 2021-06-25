class Solution:
    def kidsWithCandies(self, candies, extraCandies: int)  :
        solution=[]
        for kids in candies:
            if kids+extraCandies >= max(candies):
                solution.append(True)
            else:
                solution.append(False)
        return solution