class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        note:
        - array need to be in-place
        - Return: int

        There are 2 array in total
        target (just in imagination), k is the pointer of the target, out objective is to construct the next position
        current: given from the input

        """
        k = 1  # pointing to the next position of the target array

        for i in range(len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    inputs = [1, 2, 2, 3, 4, 4, 5]
    s = Solution().removeDuplicates(inputs)
    print(s)
