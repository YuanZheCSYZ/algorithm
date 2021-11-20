# 392 https://leetcode.com/problems/is-subsequence/submissions/

class Solution(object):

    """
    Runtime: 12 ms, faster than 97.38% of Python online submissions for Is Subsequence.
    Memory Usage: 13.6 MB, less than 49.50% of Python online submissions for Is Subsequence.
    """
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) < len(s):
            return False

        i_t = 0
        for x in s:
            tmp = t.find(x, i_t)
            if tmp >= 0:
                i_t = tmp + 1
            else:
                return False

        return True

    """
    Runtime: 12 ms, faster than 97.38% of Python online submissions for Is Subsequence.
    Memory Usage: 13.5 MB, less than 90.00% of Python online submissions for Is Subsequence.
    https://leetcode.com/problems/is-subsequence/discuss/87258/2-lines-Python
    """
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)