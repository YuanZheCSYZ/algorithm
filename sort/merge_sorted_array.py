# 88 https://leetcode.com/problems/merge-sorted-array/submissions/

class Solution:
    """
    Runtime: 32 ms, faster than 90.83% of Python3 online submissions for Merge Sorted Array.
    Memory Usage: 14.4 MB, less than 32.22% of Python3 online submissions for Merge Sorted Array.
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        p = len(nums1) - 1
        # !!!! >= 0
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1

            p -= 1

        # !!! >= 0
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]
