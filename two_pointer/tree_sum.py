class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        ans = []
        nums.sort()  # O(NlogN)
        # for k in range(n-2): #O(N*N)
        k = 0
        while k < n - 2:
            # nums[l]+num[r] = target = - nums[k]; k<l<r<n-2
            l, r = k + 1, n - 1
            print("- k", k)

            while l < r:
                if nums[l] + nums[r] + nums[k] == 0:
                    ans.append([nums[k], nums[l], nums[r]])
                    while l + 1 < n - 2 and nums[l + 1] == nums[l]:
                        l += 1  # skip when duplicate inside 2 sum
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > -nums[k]:
                    r -= 1
                else:
                    l += 1
            while k + 1 < n - 2 and nums[k + 1] == nums[k]:
                k += 1  # skip duplicate outside 2 sums
            k += 1
        return ans


if __name__ == "__main__":
    nums = [1, -1, -1, 0]
    s = Solution().threeSum(nums)
    print(s)
