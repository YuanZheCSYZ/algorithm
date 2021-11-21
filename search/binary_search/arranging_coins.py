# 441 https://leetcode.com/problems/arranging-coins/

class Solution(object):
    """
    Runtime: 20 ms, faster than 87.81% of Python online submissions for Arranging Coins.
    Memory Usage: 13.4 MB, less than 33.15% of Python online submissions for Arranging Coins.
    """
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            tmp = (1 + mid) * mid // 2
            if tmp == n:
                return mid
            elif n < tmp:
                right = mid - 1
            elif n < (1 + mid + 1) * (mid + 1) // 2:
                return mid
            else:
                left = mid + 1

    """
    Runtime: 16 ms, faster than 95.94% of Python online submissions for Arranging Coins.
    Memory Usage: 13.6 MB, less than 13.07% of Python online submissions for Arranging Coins.
    https://leetcode.com/problems/arranging-coins/discuss/1559984/C%2B%2BJavaPython-O(sqrt(n))-O(logn)-O(1)-Approaches-with-Explanation
    """
    def arrangeCoins(self, n):
        return int((math.sqrt(8 * n + 1) - 1) // 2)