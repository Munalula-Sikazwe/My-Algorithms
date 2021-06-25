class Solution:
    def maximumWealth(self, accounts) -> int:
        max= 0
        for customer in accounts:
            if sum(customer) > max:
                max = sum(customer)
        return max