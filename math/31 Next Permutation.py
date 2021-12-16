# https://leetcode.com/problems/next-permutation/

class Solution:
    """
    Runtime: 36 ms, faster than 94.49% of Python3 online submissions for Next Permutation.
    Memory Usage: 14.4 MB, less than 21.43% of Python3 online submissions for Next Permutation.
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n <= 1:
            return

        # Find the pivot where i-1 < i
        # Otherwise sort to the minimal format
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                break
        else:
            nums.sort()
            return

        # Find the least number bigger than nums[i-1]
        for j in range(n - 1, i - 1, -1):
            if nums[i - 1] < nums[j]:
                break
        else:
            j = n - 1

        # Swap
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        # Sort the remaining to the minimal format
        r = n - 1
        while i < r:
            nums[i], nums[r] = nums[r], nums[i]
            i += 1
            r -= 1

