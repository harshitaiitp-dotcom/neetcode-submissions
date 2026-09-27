from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        
        ROWS, COLS = len(matrix), len(matrix[0])
        # Build a prefix sum matrix with 1 extra row and column to simplify boundary conditions
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        for r in range(ROWS):
            for c in range(COLS):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.prefix[r][c + 1]
                    + self.prefix[r + 1][c]
                    - self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Translate to 1-indexed coordinates in self.prefix
        r1, c1, r2, c2 = row1, col1, row2 + 1, col2 + 1
        
        return (
            self.prefix[r2][c2]
            - self.prefix[r1][c2]
            - self.prefix[r2][c1]
            + self.prefix[r1][c1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)