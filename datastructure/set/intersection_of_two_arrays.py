# 349 https://leetcode.com/problems/intersection-of-two-arrays/submissions/

class Solution(object):
    """
    Runtime: 28 ms, faster than 88.55% of Python online submissions for Intersection of Two Arrays.
    Memory Usage: 13.9 MB, less than 14.58% of Python online submissions for Intersection of Two Arrays.
    """
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1).intersection(set(nums2))
