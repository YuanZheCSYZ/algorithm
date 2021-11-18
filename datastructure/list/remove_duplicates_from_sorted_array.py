# 26 https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

class Solution:
    """
    Runtime: 80 ms, faster than 93.64% of Python3 online submissions for Remove Duplicates from Sorted Array.
    Memory Usage: 15.7 MB, less than 47.91% of Python3 online submissions for Remove Duplicates from Sorted Array.

    """
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt_dup = 0
        void_index = 0
        for index in range(1, len(nums)):
            if nums[index - 1] == nums[index]:
                cnt_dup += 1
                if not void_index:
                    void_index = index

                continue

            if void_index:
                nums[void_index] = nums[index]
                void_index += 1

        return len(nums) - cnt_dup
