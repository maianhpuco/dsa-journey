# problem:  https://leetcode.com/problems/sum-of-unique-elements/submissions/


# solution : 19%
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}

        for i in nums:
            c = 0
            if count_dict.get(i):
                count_dict[i] += 1
            else:
                count_dict.update({i: 1})

        result = 0
        for num, count in count_dict.items():
            if count == 1:
                result += num

        return result
