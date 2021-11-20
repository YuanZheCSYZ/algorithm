# 389 https://leetcode.com/problems/find-the-difference/submissions/

class Solution(object):
    """
    Runtime: 16 ms, faster than 96.60% of Python online submissions for Find the Difference.
    Memory Usage: 13.5 MB, less than 78.18% of Python online submissions for Find the Difference.
    """
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        for x in set(t):
            if s.count(x) < t.count(x):
                return x

    """
    Runtime: 24 ms, faster than 75.67% of Python online submissions for Find the Difference.
    Memory Usage: 13.7 MB, less than 20.75% of Python online submissions for Find the Difference.
    """

    def findTheDifference(self, s, t):
        r = 0
        for x in s:
            r ^= ord(x)

        for x in t:
            r ^= ord(x)

        return chr(r)