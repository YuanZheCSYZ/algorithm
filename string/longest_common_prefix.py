# 14 https://leetcode.com/problems/longest-common-prefix/submissions/
class Solution:
    """
    Runtime: 24 ms, faster than 98.69% of Python3 online submissions for Longest Common Prefix.
    Memory Usage: 14.5 MB, less than 25.62% of Python3 online submissions for Longest Common Prefix.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs, key=lambda x: len(x))
        common = sorted_strs[0]
        for i in range(1, len(sorted_strs)):
            pair = sorted_strs[i]
            for x in range(len(common)):
                if common[x] != pair[x]:
                    if x == 0:
                        return ""

                    common = common[:x]
                    break

        return common

    """
    Runtime: 16 ms, faster than 99.95% of Python3 online submissions for Longest Common Prefix.
    Memory Usage: 14.2 MB, less than 81.90% of Python3 online submissions for Longest Common Prefix.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for s in zip(*strs):
            if len(set(s)) != 1:
                break
            i += 1

        return strs[0][0:i]