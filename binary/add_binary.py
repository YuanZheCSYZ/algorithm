# 67 https://leetcode.com/problems/add-binary/submissions/

class Solution:
    """
    Runtime: 32 ms, faster than 80.48% of Python3 online submissions for Add Binary.
    Memory Usage: 14.2 MB, less than 80.53% of Python3 online submissions for Add Binary.
    """
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, base=2)+int(b, base=2))

    """
    Runtime: 32 ms, faster than 80.48% of Python3 online submissions for Add Binary.
    Memory Usage: 14.1 MB, less than 80.53% of Python3 online submissions for Add Binary.
    """
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]