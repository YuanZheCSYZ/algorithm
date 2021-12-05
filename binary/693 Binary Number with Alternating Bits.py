# 693 https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    """
    Runtime: 28 ms, faster than 83.08% of Python3 online submissions for Binary Number with Alternating Bits.
    Memory Usage: 14.4 MB, less than 6.70% of Python3 online submissions for Binary Number with Alternating Bits.
    """
    def hasAlternatingBits(self, n: int) -> bool:
        l = n & 1
        while n:
            n >>= 1
            if not n:
                break

            c = n & 1
            if c == l:
                return False

            l = c
        return True

    """
    Runtime: 28 ms, faster than 83.08% of Python3 online submissions for Binary Number with Alternating Bits.
    Memory Usage: 14.2 MB, less than 67.00% of Python3 online submissions for Binary Number with Alternating Bits.
    https://leetcode.com/problems/binary-number-with-alternating-bits/discuss/108427/Oneliners-(C%2B%2B-Java-Ruby-Python)
    """
    def hasAlternatingBits(self, n: int) -> bool:
        n ^= n // 4
        return not (n & n - 1)

    """
    Runtime: 28 ms, faster than 83.08% of Python3 online submissions for Binary Number with Alternating Bits.
    Memory Usage: 14.2 MB, less than 67.00% of Python3 online submissions for Binary Number with Alternating Bits.
    https://leetcode.com/problems/binary-number-with-alternating-bits/discuss/108427/Oneliners-(C%2B%2B-Java-Ruby-Python)
    """
    def hasAlternatingBits(self, n: int) -> bool:
        return not (n * 3) & (n * 3 + 1) & (n * 3 + 2)