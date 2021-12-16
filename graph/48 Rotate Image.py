# https://leetcode.com/problems/rotate-image/

class Solution:
    """
    Runtime: 36 ms, faster than 65.74% of Python3 online submissions for Rotate Image.
    Memory Usage: 14.2 MB, less than 85.63% of Python3 online submissions for Rotate Image.
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        n_1 = n - 1
        for y in range(n // 2):
            for x in range((n + 1) // 2):
                matrix[y][x], matrix[x][n_1 - y], matrix[n_1 - y][n_1 - x], matrix[n_1 - x][y] = \
                    matrix[n_1 - x][y], matrix[y][x], matrix[x][n_1 - y], matrix[n_1 - y][n_1 - x]

    """
    Runtime: 44 ms, faster than 20.08% of Python3 online submissions for Rotate Image.
    Memory Usage: 14.4 MB, less than 30.38% of Python3 online submissions for Rotate Image.
    https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)
    """
    def rotate(self, A):
        n = len(A)
        for i in range(n//2):
            for j in range(n-n//2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]