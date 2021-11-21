# 476 https://leetcode.com/problems/number-complement/

class Solution(object):
    """
    Runtime: 16 ms, faster than 80.00% of Python online submissions for Number Complement.
    Memory Usage: 13.5 MB, less than 15.65% of Python online submissions for Number Complement.
    """
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        num ^= 1
        x = 2
        while x <= num:
            num ^= x
            x <<= 1

        return num

    """
    Runtime: 16 ms, faster than 80.00% of Python online submissions for Number Complement.
    Memory Usage: 13.2 MB, less than 99.13% of Python online submissions for Number Complement.
    https://leetcode.com/problems/number-complement/discuss/96103/maybe-fewest-operations
    """
    def findComplement(self, num):
        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return num ^ mask