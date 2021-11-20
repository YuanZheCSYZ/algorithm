# 303 https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):

    """
    Runtime: 912 ms, faster than 31.62% of Python online submissions for Range Sum Query - Immutable.
    Memory Usage: 17 MB, less than 91.50% of Python online submissions for Range Sum Query - Immutable.
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if self.nums:
            return sum(self.nums[left:right + 1])

        return None

    """
    Runtime: 68 ms, faster than 67.19% of Python online submissions for Range Sum Query - Immutable.
    Memory Usage: 17.4 MB, less than 44.47% of Python online submissions for Range Sum Query - Immutable.
    https://leetcode.com/problems/range-sum-query-immutable/discuss/75184/5-lines-C%2B%2B-4-lines-Python
    """
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums:
            self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j + 1] - self.accu[i]
