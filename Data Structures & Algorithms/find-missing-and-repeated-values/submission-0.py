class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        total_numbers = n * n
        counts = [0] * (total_numbers + 1)
        for row in grid:
            for val in row:
                counts[val] += 1              
        repeated = -1
        missing = -1       
        for num in range(1, total_numbers + 1):
            if counts[num] == 2:
                repeated = num
            elif counts[num] == 0:
                missing = num                
        return [repeated, missing]