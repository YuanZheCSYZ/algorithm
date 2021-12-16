# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    """
    Runtime: 36 ms, faster than 92.48% of Python3 online submissions for Search in Rotated Sorted Array.
    Memory Usage: 14.6 MB, less than 56.42% of Python3 online submissions for Search in Rotated Sorted Array.
    """
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            mid = (l + r) // 2
            tmp = nums[mid]
            if tmp == target:
                return mid

            if nums[l] < nums[r]:
                if tmp < target:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[r]:
                    if tmp < target or nums[r] < tmp:
                        l = mid + 1
                    else:
                        r = mid - 1
                elif target < nums[l]:
                    if tmp < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if target < tmp or tmp < nums[l]:
                        r = mid - 1
                    else:
                        l = mid + 1

        return l if nums[l] == target else -1