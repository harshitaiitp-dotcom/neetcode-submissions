class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        return sum(h != exp for h, exp in zip(heights, expected))