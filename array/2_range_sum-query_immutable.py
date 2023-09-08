# https://leetcode.com/problems/range-sum-query-immutable/submissions/
# Note: tips is to use the prefix sum


# class NumArray(object):

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums


#     def sumRange(self, left, right):
#         """
#         :type left: int
#         :type right: int
#         :rtype: int
#         """
#         ans = 0
#         for pos in range(left, right+1):
#             ans += self.nums[pos]
#         return ans

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


class NumArray(object):
    """
    prefix sum array:
    A[0] = 0
    A[n] = A[n-1] + nums[n+1]
    A[1] = A[0] + nums[0]

    A[5] = sum(nums[i for i in [0, 1, 2, 3, 4, 5]])
    A[3] = nums(nums[i for i in [0, 1, 2, 3]])
    A[5] - A[3-1] = nums(nums[i for i in [3, 4, 5]])

    """

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.prefix_sums = [0]
        sum_val = 0
        for i in range(len(nums)):
            sum_val += nums[i]
            self.prefix_sums.append(sum_val)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
