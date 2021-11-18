# 20 https://leetcode.com/problems/valid-parentheses/submissions/
class Solution:

    """
    Runtime: 32 ms, faster than 69.50% of Python3 online submissions for Valid Parentheses.
    Memory Usage: 14.2 MB, less than 87.15% of Python3 online submissions for Valid Parentheses.
    """
    def isValid(self, s: str) -> bool:
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for x in s:
            if x in mapping.values():
                stack.append(x)
            else:
                if not stack or stack[-1] != mapping[x]:
                    return False
                else:
                    stack.pop()

        return not stack
