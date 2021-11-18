# 69 https://leetcode.com/problems/sqrtx/submissions/

class Solution:
    """
    Runtime: 28 ms, faster than 96.67% of Python3 online submissions for Sqrt(x).
    Memory Usage: 14.1 MB, less than 70.21% of Python3 online submissions for Sqrt(x).
    """
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start <= end:
            pivot = (start + end) // 2
            pivot_square = pivot * pivot
            if pivot_square <= x < (pivot + 1) * (pivot + 1):
                return pivot
            if pivot_square < x:
                start = pivot + 1
            else:
                end = pivot - 1

        return start
