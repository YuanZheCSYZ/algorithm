# 28 https://leetcode.com/problems/implement-strstr/submissions/

class Solution:
    """
    Runtime: 28 ms, faster than 94.46% of Python3 online submissions for Implement strStr().
    Memory Usage: 14.4 MB, less than 61.75% of Python3 online submissions for Implement strStr().
    """
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    """
    Runtime: 52 ms, faster than 54.89% of Python3 online submissions for Implement strStr().
    Memory Usage: 14.7 MB, less than 11.41% of Python3 online submissions for Implement strStr().
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        haystack_length = len(haystack)
        needle_length = len(needle)

        for i in range(len(haystack)):
            if haystack_length < i + needle_length:
                break

            if haystack[i: i + needle_length] == needle:
                return i

        return -1