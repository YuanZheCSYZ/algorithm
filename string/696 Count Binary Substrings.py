# 696 https://leetcode.com/problems/count-binary-substrings/

class Solution:
    """
    Runtime: 212 ms, faster than 39.60% of Python3 online submissions for Count Binary Substrings.
    Memory Usage: 14.6 MB, less than 34.11% of Python3 online submissions for Count Binary Substrings.
    """
    def countBinarySubstrings(self, s: str) -> int:
        matching = s[0]
        cnt = 1
        i = 1
        res = 0
        while i < len(s):
            if s[i] == matching:
                cnt += 1
                i += 1
            else:
                cnt_o = cnt
                cnt = 1
                matching = s[i]
                i += 1
                while i < len(s) and s[i] == matching:
                    cnt += 1
                    i += 1

                res += min(cnt, cnt_o)

        return res

    """
    Runtime: 104 ms, faster than 99.44% of Python3 online submissions for Count Binary Substrings.
    Memory Usage: 15.8 MB, less than 5.32% of Python3 online submissions for Count Binary Substrings.
    https://leetcode.com/problems/count-binary-substrings/discuss/108625/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation
    """
    def countBinarySubstrings(self, s: str) -> int:
        s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a, b) for a, b in zip(s, s[1:]))

    """
    Runtime: 108 ms, faster than 99.09% of Python3 online submissions for Count Binary Substrings.
    Memory Usage: 15.7 MB, less than 5.32% of Python3 online submissions for Count Binary Substrings.
    """
    def countBinarySubstrings(self, s: str) -> int:
        s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(s[x - 1], s[x]) for x in range(1, len(s)))
