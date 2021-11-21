# 496 https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    """
    Runtime: 32 ms, faster than 90.86% of Python online submissions for Next Greater Element I.
    Memory Usage: 13.7 MB, less than 38.39% of Python online submissions for Next Greater Element I.
    """
    def nextGreaterElement(self, nums1, nums2):
        mapping = {}
        for i, x in enumerate(nums2):
            j = i + 1
            g = -1
            while j < len(nums2):
                y = nums2[j]
                if x < y:
                    g = y
                    break
                else:
                    j += 1
            mapping[x] = g

        return [mapping[x] for x in nums1]
