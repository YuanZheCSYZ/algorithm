# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    """
    Runtime: 32 ms, faster than 99.38% of Python3 online submissions for Self Dividing Numbers.
    Memory Usage: 14.2 MB, less than 83.87% of Python3 online submissions for Self Dividing Numbers.
    """
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            if i < 10:
                res.append(i)
                continue

            for j in str(i):
                j = int(j)
                if not j:
                    break

                if i % j:
                    break
            else:
                res.append(i)

        return res
