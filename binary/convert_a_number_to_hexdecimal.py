# 405 https://leetcode.com/problems/convert-a-number-to-hexadecimal/submissions/

class Solution(object):
    """
    Runtime: 20 ms, faster than 45.83% of Python online submissions for Convert a Number to Hexadecimal.
    Memory Usage: 13.5 MB, less than 43.75% of Python online submissions for Convert a Number to Hexadecimal.
    """
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = 16
        mapping = {
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f"
        }

        fast_mapping = []
        for x in range(8):
            fast_mapping.insert(0, 15 * (16 ** x))

        if num == 0:
            return "0"

        if num < 0:
            num += 2 ** 32

        res = []
        while num:
            remaining = num % base
            res.append(str(remaining) if remaining < 10 else mapping[remaining])
            num //= 16

        return "".join(res[::-1])
