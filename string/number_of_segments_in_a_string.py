# 434 https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution(object):
    """
    Runtime: 16 ms, faster than 79.61% of Python online submissions for Number of Segments in a String.
    Memory Usage: 13.6 MB, less than 12.62% of Python online submissions for Number of Segments in a String.
    """
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

    """
    Runtime: 16 ms, faster than 79.61% of Python online submissions for Number of Segments in a String.
    Memory Usage: 13.7 MB, less than 12.62% of Python online submissions for Number of Segments in a String.
    """
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        found = False
        for x in s:
            if x != " ":
                if found:
                    continue

                cnt += 1
                found = True
            else:
                found = False

        return cnt