# 504 https://leetcode.com/problems/base-7/

class Solution(object):
    """
    Runtime: 27 ms, faster than 21.94% of Python online submissions for Base 7.
    Memory Usage: 13.4 MB, less than 68.88% of Python online submissions for Base 7.
    """
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        neg = num < 0
        num = abs(num)
        while True:
            res.append(str(num % 7))
            if num < 7:
                break

            num //= 7

        return ("-" * neg) + "".join(res[::-1])



