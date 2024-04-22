#LINK: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:

    def findMin(self, nums: List[int]) -> int:
        '''
        example: [0,1,2,4,5,6,7] 
        [4,5,6,7,0,1,2],  [0,1,2,4,5,6,7] [2, 1]

        ans =? 
        #RIGHT < LEFT
        #1: [4,5,6,7][0,1,2] #2: [5,6,7][0,1,2,4] 
        [rev][ori]
        l,r 
        l > r, mid = 3
        if arr[mid] > left, right < left
        -> mid belong to the [rev]
        left = mid + 1 
       
        #2: [5,6,7][0,1,2,4] 
        arr[mid] < left 
        -> mid belong to the [ori]
        -> remove the rigght elements
        ans = arr[mid]  
        right = mid - 1 
        
        # [0,1,2,4,5,6,7] if left value < right value -> return left value 
        # 

        '''
        l, r = 0, len(nums) - 1  #0->2

        if nums[l] <= nums[r]:  # [0,1,2,4,5,6,7]
            return nums[l]

        if (r - l) < 2:  #1
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                return nums[r]

        ans = -1
        #print(r-l)
        while (r - l) >= 2:  # 3 element array only
            # and nums[l] >= nums[r]: #2: [5,6,7][0,1,2,4]  #[2, 1] #[3, 4, [mid^1, 2] #base-case
            # if len()
            mid = l + (r - l) // 2
            #print("mid", mid, nums)
            if nums[mid] > nums[
                    l]:  #mid belong to the reverse_arra; edge case [2, 1]
                l = mid
            else:  # mid belong to the original_array   [][ori]
                ans = nums[mid]  # mid = 1, r = 0
                #print(ans)
                r = mid

        if (r - l) < 2:  #1
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                return nums[r]
        return ans
