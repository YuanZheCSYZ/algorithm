# https://leetcode.com/problems/nth-magical-number/submissions/
class Solution:
    """
    Runtime: 116 ms, faster than 12.12% of Python3 online submissions for Nth Magical Number.
    Memory Usage: 14.3 MB, less than 59.60% of Python3 online submissions for Nth Magical Number.
    """
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        a, b = min(a, b), max(a, b)
        lcm = self.getLCM(a, b)
        base_lcm = lcm // a + lcm // b - 1
        cnt_lcm = n // base_lcm

        n %= base_lcm
        base_a = 0
        base_b = 0
        res = 0
        while n:
            tmp_a = (base_a + 1) * a
            tmp_b = (base_b + 1) * b
            n -= 1
            if tmp_a < tmp_b:
                if n == 0:
                    res = tmp_a
                    break

                base_a += 1
            else:
                if n == 0:
                    res = tmp_b
                    break

                base_b += 1

        return (res + cnt_lcm * lcm) % (10 ** 9 + 7)

    """
    Runtime: 24 ms, faster than 95.96% of Python3 online submissions for Nth Magical Number.
    Memory Usage: 14.3 MB, less than 59.60% of Python3 online submissions for Nth Magical Number.
    https://leetcode.com/problems/nth-magical-number/discuss/1622600/Python-Binary-Search-%2B-LCM
    """
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        a, b = min(a, b), max(a, b)
        lcm = self.getLCM(a, b)
        base_lcm = lcm // a + lcm // b - 1
        cnt_lcm = n // base_lcm

        n %= base_lcm
        l = 0
        r = a * n

        while l <= r:
            m = (l + r) // 2
            if n <= m // a + m // b:
                r = m - 1
            else:
                l = m + 1

        return (l + cnt_lcm * lcm) % (10 ** 9 + 7)

    def getLCM(self, a, b):
        return a // self.getGCD(a, b) * b

    def getGCD(self, a, b):
        if b == 0:
            return a

        return self.getGCD(b, a % b)

