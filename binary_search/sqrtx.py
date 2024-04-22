# link : https://leetcode.com/problems/sqrtx/


class Solution:

    def mySqrt(self, x: int) -> int:
        '''
        the largest among the smaller that than y that y**y <= x 
        '''
        left = 0
        right = 46340
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        return ans
