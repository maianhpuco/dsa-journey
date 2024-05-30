#link : https://leetcode.com/problems/subarray-product-less-than-k/submissions/1270556585/


class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        n = len(nums)
        count = 0
        product = 1

        for r in range(n):
            product *= nums[r]
            while product >= k and l < r:
                product /= nums[l]
                l += 1
            if product < k:
                count += (r - l + 1)  #[5] [5, 2]
        return count
