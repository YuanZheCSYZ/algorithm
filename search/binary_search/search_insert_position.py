# 35 https://leetcode.com/problems/search-insert-position/submissions/

class Solution:

    """
    Runtime: 44 ms, faster than 92.03% of Python3 online submissions for Search Insert Position.
    Memory Usage: 15.2 MB, less than 24.41% of Python3 online submissions for Search Insert Position.
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.biSearch(nums, 0, len(nums) - 1, target)

    def biSearch(self, nums, start, end, target):
        if end <= start:
            if nums[start] < target:
                return start + 1

            return start

        pivot = (start + end) // 2
        if nums[pivot] == target:
            return pivot

        elif nums[pivot] < target:
            return self.biSearch(nums, pivot + 1, end, target)

        else:
            return self.biSearch(nums, start, pivot - 1, target)