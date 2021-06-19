class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[1]*n]*m

        for row in range(m-1)[::-1]:
            for col in range(n)[::-1]:
                bottom_val = board[row+1][col] if row+1 < m else 0
                right_val = board[row][col+1] if col+1 < n else 0
                board[row][col] = bottom_val + right_val
        return board[0][0] 

 
