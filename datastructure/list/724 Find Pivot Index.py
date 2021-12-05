# https://leetcode.com/problems/find-pivot-index/
class Solution:
    """
    Runtime: 192 ms, faster than 34.86% of Python3 online submissions for Find Pivot Index.
    Memory Usage: 16.2 MB, less than 6.02% of Python3 online submissions for Find Pivot Index.
    """
    def pivotIndex(self, nums):
        n = len(nums)
        if n <= 1:
            return True

        tmp = [[0, 0] for x in range(n)]
        tmp[1][0] = nums[0]
        tmp[-2][1] = nums[-1]
        m_l = n
        for x in range(2, n):
            tmp[x][0] = nums[x - 1] + tmp[x - 1][0]
            y = n - 1 - x
            tmp[y][1] = nums[y + 1] + tmp[y + 1][1]
            if y <= x:
                if tmp[x][0] == tmp[x][1]:
                    m_l = min(m_l, x)
                if tmp[y][0] == tmp[y][1]:
                    m_l = min(m_l, y)

        return -1 if m_l == n else m_l

    """
    Runtime: 140 ms, faster than 95.78% of Python3 online submissions for Find Pivot Index.
    Memory Usage: 15.3 MB, less than 93.50% of Python3 online submissions for Find Pivot Index.
    https://leetcode.com/problems/find-pivot-index/discuss/109255/Short-Python-O(n)-time-O(1)-space-with-Explanation
    """
    def pivotIndex(self, nums):
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1