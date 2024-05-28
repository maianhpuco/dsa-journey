# Link: https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1270077622/ 

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        - subarray have sum >= target = 10 
        nums = [2,3,1,2,4,3] 
        
        [2,[3,1,2,4],3]
        left: + update when [right is update]
        right: 
            + change window: update when target is not found            
        curr_sum 
        '''
        min_length = float('inf')
        l = 0
        curr_sum = 0 

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target: 
                min_length = min(min_length, r - l + 1)
                curr_sum -= nums[l]
                l += 1

        return 0 if min_length == float('inf') else min_length
