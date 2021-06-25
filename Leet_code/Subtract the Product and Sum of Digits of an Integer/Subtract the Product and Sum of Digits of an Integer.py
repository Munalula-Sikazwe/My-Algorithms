class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def add(number):
            if number == 0:
                return 0
            else:
                return number % 10 + add(number // 10)

        def product(number):
            if number == 0:
                return 1
            else:
                return number % 10 * product(number // 10)

        return product(n) - add(n)