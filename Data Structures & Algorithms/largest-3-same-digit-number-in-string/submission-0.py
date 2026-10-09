class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in range(9, -1, -1):
            sub = str(digit) * 3
            if sub in num:
                return sub
        return ""