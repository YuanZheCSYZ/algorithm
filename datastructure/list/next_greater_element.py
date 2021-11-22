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

    """
    Runtime: 28 ms, faster than 96.88% of Python online submissions for Next Greater Element I.
    Memory Usage: 14 MB, less than 13.86% of Python online submissions for Next Greater Element I.
    """
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mapping = {
            nums2[-1]: -1
        }
        for i in range(len(nums2) - 2, -1, -1):
            x = nums2[i]
            j = i + 1
            g = -1
            while j < len(nums2):
                y = nums2[j]
                if x < y:
                    g = y
                    break

                m_y = mapping[y]
                if y < x and (m_y == -1 or x < m_y):
                    g = m_y
                    break
                else:
                    j += 1

            mapping[x] = g

        return [mapping[x] for x in nums1]