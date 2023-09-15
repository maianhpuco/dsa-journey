class Solution:
    def treeSumSmaller(self, nums, target):
        """
        fix one element of the array, then use 2-sum to find the other elements (sorted the array)
        nums[k]
        nums[l] + nums[r]  < target - nums[k]
        [-2 [0L 1 3R]]
        L+R >= target -> remove right : r -=1
        L+R <

        Note: avoid duplication
        """

        k = 0
        n = len(nums)
        nums.sort()  # O(sorted)
        ans = 0
        while k < n - 2:
            l, r = k + 1, n - 1
            while l < r:
                if nums[l] + nums[r] < target - nums[k]:
                    ans += r - l  # --> SMART
                    l += 1  # -> #SMART
                else:
                    r -= 1
            k += 1

        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [-2, 0, 1, 3]
    target = 2
    output = solution.treeSumSmaller(nums, target)
    print(output)
