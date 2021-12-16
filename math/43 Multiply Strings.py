# https://leetcode.com/problems/multiply-strings/

class Solution:
    """
    Runtime: 48 ms, faster than 59.69% of Python3 online submissions for Multiply Strings.
    Memory Usage: 14.5 MB, less than 11.49% of Python3 online submissions for Multiply Strings.
    """
    def multiply(self, num1: str, num2: str) -> str:
        if num2 == "0" or num1 == "0":
            return "0"

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        n1 = len(num1)
        n2 = len(num2)
        n = n1 + n2 + 1
        s = 8
        res = [0 for _ in range((n + s - 1) // s)]
        num1_l = [0 for _ in range((n1 + s - 1) // s)]
        for x in range((n1 + s - 1) // s):
            num1_l[-x - 1] = int(num1[max(0, n1 - s * x - s): n1 - s * x])

        base = 10 ** s
        carry = 0

        for i, x in enumerate(num2[::-1]):
            bump = i // s
            x = int(x) * (10 ** (i % s))
            for i in range(-1, -len(num1_l) - 1, -1):
                tmp = num1_l[i] * x + carry + res[i - bump]
                carry = tmp // base
                res[i - bump] = tmp % base

            if carry:
                res[i - bump - 1] += carry
                carry = 0

        i = 0
        while i < len(res) and res[i] == 0:
            i += 1

        return str(res[i]) + "".join(map(lambda x: "{:08}".format(x), res[i + 1:]))
