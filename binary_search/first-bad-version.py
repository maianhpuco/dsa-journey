#Link: https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:

    def firstBadVersion(self, n: int) -> int:
        '''
        [1, 2, 3, 4, 5] -> 4
        isBadVesion(v)
        '''
        l, r = 0, n
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
