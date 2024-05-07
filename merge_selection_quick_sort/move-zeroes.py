#link: https://leetcode.com/problems/move-zeroes/
class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # inplace: swap until 0 reach the end
        
                i^
        nums = [1,1,0,3,12] 
                        ^i 
               [1,1,3,0,12] 
                      ^l
        """
        i, l = 0, 0
        #l: value at (l-1) will be non-zero
        while i < len(nums):
            if nums[l] == 0 and nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[l] != 0:
                l += 1
            i += 1
