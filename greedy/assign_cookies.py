# 455 https://leetcode.com/problems/assign-cookies/

class Solution(object):

    """
    Runtime: 132 ms, faster than 82.96% of Python online submissions for Assign Cookies.
    Memory Usage: 14.8 MB, less than 48.60% of Python online submissions for Assign Cookies.
    """
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        gi = 0
        si = 0
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                gi += 1

            si += 1

        return gi
