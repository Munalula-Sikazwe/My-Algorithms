class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = x[::-1]
        if x.endswith('-'):
            x = x.replace('-', '')
            x = '-' + x
        x = int(x)
        if -2 ** 31 < x < 2 ** 31:
            return x
        else:
            return 0
