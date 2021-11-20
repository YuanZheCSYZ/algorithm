# 374 https://leetcode.com/problems/guess-number-higher-or-lower/submissions/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    """
    Runtime: 12 ms, faster than 96.61% of Python online submissions for Guess Number Higher or Lower.
    Memory Usage: 13.6 MB, less than 12.92% of Python online submissions for Guess Number Higher or Lower.
    """
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            if res == 0:
                return mid
            if res < 0:
                right = mid - 1
            else:
                left = mid + 1

        return -1