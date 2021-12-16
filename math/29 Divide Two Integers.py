# https://leetcode.com/problems/divide-two-integers/

class Solution:
    """
    Runtime: 28 ms, faster than 92.31% of Python3 online submissions for Divide Two Integers.
    Memory Usage: 14.2 MB, less than 57.12% of Python3 online submissions for Divide Two Integers.
    """
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1

        neg = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        while divisor & 1 == 0:
            divisor >>= 1
            dividend >>= 1

        if divisor == 1:
            return -dividend if neg else dividend

        # !!!
        base = 0
        while divisor << 1 < dividend:
            divisor <<= 1
            base += 1

        res = 0
        while 0 <= base:
            tmp = 1 << base
            while divisor <= dividend:
                dividend -= divisor
                res += tmp

            base -= 1
            divisor >>= 1

        return -res if neg else res

    """
    Runtime: 20 ms, faster than 99.69% of Python3 online submissions for Divide Two Integers.
    Memory Usage: 14.3 MB, less than 23.04% of Python3 online submissions for Divide Two Integers.
    https://leetcode.com/problems/divide-two-integers/discuss/142849/C%2B%2BJavaPython-Should-Not-Use-%22long%22-Int
    """
    def divide(self, A, B):
        if (A == -2147483648 and B == -1): return 2147483647
        a, b, res = abs(A), abs(B), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (A > 0) == (B > 0) else -res
