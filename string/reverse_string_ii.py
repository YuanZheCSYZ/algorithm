# 541 https://leetcode.com/problems/reverse-string-ii/

class Solution(object):
    """
    Runtime: 12 ms, faster than 99.63% of Python online submissions for Reverse String II.
    Memory Usage: 13.8 MB, less than 51.12% of Python online submissions for Reverse String II.
    """
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        return "".join(s[i:i + k][::-1] + s[i + k:i + k * 2] for i in range(0, len(s), k * 2))
