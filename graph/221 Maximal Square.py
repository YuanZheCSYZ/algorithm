# https://leetcode.com/problems/maximal-square/

class Solution:
    """
    Runtime: 715 ms, faster than 6.12% of Python3 online submissions for Maximal Square.
    Memory Usage: 15.7 MB, less than 30.72% of Python3 online submissions for Maximal Square.
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        m = len(matrix)
        n = len(matrix[0])
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == "0":
                    continue

                res = max(res, self.findSquare(matrix, m, n, x, y, res))

        return res ** 2

    def findSquare(self, matrix, m, n, x, y, tmp_max):
        cnt = 1
        while y + cnt < m and x + cnt < n:
            if matrix[y + cnt][x + cnt] == "0":
                break

            cnt += 1

        if cnt <= tmp_max:
            return cnt

        for i in range(1, cnt):
            for j in range(i):
                if matrix[y + i][x + j] == "0" or matrix[y + j][x + i] == "0":
                    return i

        return cnt

    """
    Runtime: 200 ms, faster than 82.14% of Python3 online submissions for Maximal Square.
    Memory Usage: 15.7 MB, less than 54.93% of Python3 online submissions for Maximal Square.
    https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach
    
    DP
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if matrix[0][0] == "1":
            dp[0][0] = 1

        for i in range(1, max(n, m)):
            if i < n and matrix[0][i] == "1":
                dp[0][i] = 1
            if i < m and matrix[i][0] == "1":
                dp[i][0] = 1

        res = any(dp[0]) or any(dp[j][0] for j in range(m))
        for j in range(1, m):
            for i in range(1, n):
                if matrix[j][i] == "1":
                    dp[j][i] = min(dp[j - 1][i], dp[j][i - 1], dp[j - 1][i - 1]) + 1
                    res = max(res, dp[j][i])

        return res ** 2