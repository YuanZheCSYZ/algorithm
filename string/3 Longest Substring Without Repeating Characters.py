# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    """
    Runtime: 56 ms, faster than 86.09% of Python3 online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 14.5 MB, less than 25.31% of Python3 online submissions for Longest Substring Without Repeating Characters.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping = {}
        cnt = 0
        m = 0
        for i, x in enumerate(s):
            if x not in mapping:
                cnt += 1
                if m < cnt:
                    m = cnt
                mapping[x] = i
            else:
                for j in range(i - len(mapping), mapping[x]):
                    del mapping[s[j]]

                mapping[x] = i
                cnt = len(mapping)

        return m

    """
    Runtime: 48 ms, faster than 96.86% of Python3 online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 14.4 MB, less than 25.31% of Python3 online submissions for Longest Substring Without Repeating Characters.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping = {}
        b = 0
        m = 0
        for i, x in enumerate(s):
            if x in mapping and b <= mapping[x]:
                b = mapping[x] + 1
            else:
                l = i - b + 1
                if m < l:
                    m = l

            mapping[x] = i

        return m
