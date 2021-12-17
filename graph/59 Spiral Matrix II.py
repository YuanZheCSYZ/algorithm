# https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    """
    Runtime: 32 ms, faster than 71.21% of Python3 online submissions for Spiral Matrix II.
    Memory Usage: 14.2 MB, less than 77.60% of Python3 online submissions for Spiral Matrix II.
    """
    def generateMatrix(self, n: int, start=1) -> List[List[int]]:
        if n == 1:
            return [[start]]
        elif n == 2:
            return [
                [start, start + 1],
                [start + 3, start + 2],
            ]

        last = self.generateMatrix(n - 2, n * 4 - 4 + start)
        for y in range(n - 2):
            last[y] = [start + n * 4 - 4 - y - 1] + last[y] + [start + n + y]

        return [[start + x for x in range(n)]] + \
               last + \
               [[start + n * 3 - 2 - x - 1 for x in range(n)]]

    """
    Runtime: 37 ms, faster than 24.63% of Python3 online submissions for Spiral Matrix II.
    Memory Usage: 14.2 MB, less than 92.00% of Python3 online submissions for Spiral Matrix II.
    https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions
    """
    def generateMatrix(self, n):
        A, lo = [], n * n + 1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + list(zip(*A[::-1]))
        return A