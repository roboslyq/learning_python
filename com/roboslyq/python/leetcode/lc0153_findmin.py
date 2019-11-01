from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            raise Exception('程序出错')
        if size == 1:
            return nums[0]
        left = 0;
        right = len(nums) - 1;
        while left < right:
            middle = (right + left) >> 1
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                # assert nums[middle] < nums[right]
                right = middle
        return nums[left]


nums = [9, 8, 7, 1, 2, 3]
nums2 = [3, 4, 5, 1, 2]
so = Solution()
print(so.findMin(nums))
print(so.findMin(nums2))
