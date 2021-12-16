# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    """
    Runtime: 76 ms, faster than 97.49% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    Memory Usage: 15.5 MB, less than 12.43% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                break

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if r < l:
            return [-1, -1]
        if l == r:
            if nums[l] != target:
                return [-1, -1]
            else:
                return [l, l]

        if l < mid and nums[mid - 1] == target:
            ll = l
            rr = mid
            while ll < rr:
                mm = (ll + rr) // 2
                if nums[mm] == target:
                    rr = mm
                else:
                    ll = mm + 1

            if ll == rr:
                mm == ll

            l = mm if nums[mm] == target else mm + 1

        else:
            l = mid

        if mid < r and nums[mid + 1] == target:
            ll = mid
            rr = r
            while ll < rr:
                mm = (ll + rr + 1) // 2
                if nums[mm] == target:
                    ll = mm
                else:
                    rr = mm - 1

            if ll == rr:
                mm == ll

            r = mm if nums[mm] == target else mm - 1

        else:
            r = mid

        return [l, r]

    """
    Runtime: 76 ms, faster than 97.49% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    Memory Usage: 15.5 MB, less than 54.86% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.biSearch(nums, target)
        return [l, self.biSearch(nums, target + 1) - 1] if target in nums[l:l + 1] else [-1, -1]

    def biSearch(self, nums, target):
        l = 0
        r = len(nums)
        while l < r:
            m = (l + r) // 2
            if target <= nums[m]:
                r = m
            else:
                l = m + 1

        return l