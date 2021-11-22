# 521 https://leetcode.com/problems/longest-uncommon-subsequence-i/

class Solution(object):
    """
    Runtime: 11 ms, faster than 89.19% of Python online submissions for Longest Uncommon Subsequence I.
    Memory Usage: 13.4 MB, less than 47.30% of Python online submissions for Longest Uncommon Subsequence I.
    """
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """

        if a == b:
            return -1
        return max(len(a), len(b))
