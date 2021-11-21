# 414 https://leetcode.com/problems/third-maximum-number/

class Solution(object):

    """
    Runtime: 36 ms, faster than 82.57% of Python online submissions for Third Maximum Number.
    Memory Usage: 14 MB, less than 98.93% of Python online submissions for Third Maximum Number.
    """
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = None
        b = None
        c = None
        for x in nums:
            if not a or a < x:
                c = b
                b = a
                a = x
            elif (not b or b < x) and a != x:
                c = b
                b = x
            elif (not c or c < x) and a != x and b != x:
                c = x

        if c != None:
            return c
        else:
            return a