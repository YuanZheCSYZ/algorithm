# 448 https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/

class Solution(object):

    """
    Runtime: 364 ms, faster than 20.17% of Python online submissions for Find All Numbers Disappeared in an Array.
    Memory Usage: 20.2 MB, less than 98.86% of Python online submissions for Find All Numbers Disappeared in an Array.
    O(N)
    O(1) except output
    """
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = 0
        while index < len(nums):
            n = nums[index]
            if n <= index + 1:
                nums[n - 1] = n
                index += 1
            else:
                if nums[n - 1] != n:
                    nums[index], nums[n - 1] = nums[n - 1], n
                else:
                    index += 1

        res = []

        for x in range(len(nums)):
            n = x + 1
            if nums[x] != n:
                res.append(n)
        return res

    """
    Runtime: 332 ms, faster than 38.05% of Python online submissions for Find All Numbers Disappeared in an Array.
    Memory Usage: 20.5 MB, less than 97.76% of Python online submissions for Find All Numbers Disappeared in an Array.
    O(N)
    O(1) except output
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/1583652/C%2B%2B-Short-Solution-%2B-Python-One-Liner-Explained-No-Extra-Space
    """
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])

        res = []
        for x in range(len(nums)):
            if nums[x] > 0:
                res.append(x + 1)
        return res

    """
    Runtime: 284 ms, faster than 97.27% of Python online submissions for Find All Numbers Disappeared in an Array.
    Memory Usage: 24.6 MB, less than 12.57% of Python online submissions for Find All Numbers Disappeared in an Array.
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/1583652/C%2B%2B-Short-Solution-%2B-Python-One-Liner-Explained-No-Extra-Space
    """
    def findDisappearedNumbers(self, nums):
        return set(range(1, len(nums) + 1)) - set(nums)
