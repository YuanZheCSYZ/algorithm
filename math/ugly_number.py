# 263 https://leetcode.com/problems/ugly-number/

class Solution:
    """
    Time Limit Exceeded
    """
    def isUgly(self, n: int) -> bool:
        if n < 0:
            return False

        for x in [2, 3, 5]:
            while n % x == 0:
                n /= x

        return n == 1

    """
    Runtime: 32 ms, faster than 70.98% of Python3 online submissions for Ugly Number.
    Memory Usage: 14.2 MB, less than 46.20% of Python3 online submissions for Ugly Number.
    """
    def isUgly(self, n: int) -> bool:
        for x in [2, 3, 5]:
            n = self.biSearch(1, 31, x, n)

        return n == 1

    def biSearch(self, left, right, base, target):
        if target % base:
            return target

        while left < right:
            mid = (left + right) // 2
            mid_base = base ** mid
            if target < mid_base or target % mid_base:
                right = mid - 1
                continue

            if target % mid_base == 0 and target % (mid_base * base) != 0:
                return target // mid_base
            else:
                left = mid + 1

        return target // (base ** left)
