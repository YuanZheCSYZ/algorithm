# https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution:
    """
    Runtime: 24 ms, faster than 98.46% of Python3 online submissions for Domino and Tromino Tiling.
    Memory Usage: 14.8 MB, less than 26.15% of Python3 online submissions for Domino and Tromino Tiling.
    https://leetcode.com/problems/domino-and-tromino-tiling/discuss/1620766/Python-with-ASCII-Deduction

    f(n) = {|} x f(n-1) + {=} x f(n-2) + {L, F} * [f(n-3) + ... + f(0)]
         = f(n-1) + f(n-2) + 2 *[f(n-3) + ... + f(0)]
         = f(n-1) + {f(n-2) + f(n-3) + 2 *[f(n-4) + ... + f(0)]} + f(n-3)
         = f(n-1) + f(n-1) + f(n-3)
         = 2*f(n-1) + f(n-3)

    {L} * [f(n-3) + ... + f(0)]
         = {Lq} x f(n-3) + {L-J} x f(n-4) + {L-_q} x f(n-5) + {L-_-J} x f(n-6) + ...
         = {Lq} x f(n-3) + {L-J} x f(n-4) + ... + {L..q} x f(n-x) + {L..J} x f(n-x-1) + ...
    """
    def numTilings(self, n: int, mapping={1: 1, 2: 2, 3: 5}) -> int:
        if n < 1:
            return 0
        elif n not in mapping:
            mapping[n] = self.numTilings(n - 1, mapping) * 2 + \
                         self.numTilings(n - 3, mapping)

        return mapping[n] % (10 ** 9 + 7)

    """
    Runtime: 32 ms, faster than 83.59% of Python3 online submissions for Domino and Tromino Tiling.
    Memory Usage: 14.3 MB, less than 70.51% of Python3 online submissions for Domino and Tromino Tiling.
    """
    def numTilings(self, n: int) -> int:
        if n < 1:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        n1 = 2
        n2 = 1
        n3 = 1

        for x in range(n - 2):
            n1, n2, n3 = n1 * 2 + n3, n1, n2

        return n1 % (10 ** 9 + 7)
