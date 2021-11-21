# 459 https://leetcode.com/problems/repeated-substring-pattern/

class Solution(object):

    """
    Runtime: 16 ms, faster than 97.72% of Python online submissions for Repeated Substring Pattern.
    Memory Usage: 13.7 MB, less than 87.37% of Python online submissions for Repeated Substring Pattern.
    """
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False

        if s[0] == s[-1] and len(set(s)) == 1:
            return True

        pattern = s[-1] + s[0]
        n = len(s)
        i = 1
        while i < n - 1:
            x = s.find(pattern, i)
            if x < 0:
                return False

            tmp_pattern = s[:x + 1]
            if n % len(tmp_pattern) == 0 and s == tmp_pattern * (n // len(tmp_pattern)):
                return True
            else:
                i = x + 1

        return False

    """
    Runtime: 16 ms, faster than 97.72% of Python online submissions for Repeated Substring Pattern.
    Memory Usage: 13.6 MB, less than 87.37% of Python online submissions for Repeated Substring Pattern.
    https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination
    """
    def repeatedSubstringPattern(self, s):
        return s in (s * 2)[1:-1]