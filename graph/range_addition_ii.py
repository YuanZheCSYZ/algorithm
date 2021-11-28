# 598 https://leetcode.com/problems/range-addition-ii/

class Solution:
    """
    Runtime: 80 ms, faster than 25.74% of Python3 online submissions for Range Addition II.
    Memory Usage: 16.2 MB, less than 18.30% of Python3 online submissions for Range Addition II.
    """
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        m_x = m
        m_y = n
        for x, y in ops:
            m_x = min(m_x, x)
            m_y = min(m_y, y)

        return m_x * m_y

    """
    Runtime: 64 ms, faster than 92.13% of Python3 online submissions for Range Addition II.
    Memory Usage: 16.1 MB, less than 63.62% of Python3 online submissions for Range Addition II.
    https://leetcode.com/problems/range-addition-ii/discuss/103610/Python-solution-beat-100
    """
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        x, y = zip(*ops)
        return min(x) * min(y)

