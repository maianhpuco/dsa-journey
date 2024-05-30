# Link : https://leetcode.com/problems/valid-triangle-number/


class Solution(object):

    def triangleNumber(self, nums):
        nums.sort()
        n = len(nums)
        c = n - 1
        ans = 0

        print(len(nums))
        while c > 1:
            a, b = 0, c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    ans += b - a
                    b -= 1
                else:
                    a += 1
            c -= 1
        return ans
