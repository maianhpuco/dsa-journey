#Link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/


class Solution:

    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        numsIdx = []
        for i in range(len(nums)):
            numsIdx.append((nums[i], i))

        def mergeSort(nums, start, end):
            # DEVIDE STEPS
            if start == end:
                return nums[start:end + 1]
            mid = start + (end - start) // 2
            leftSide = mergeSort(nums, start, mid)
            rightSide = mergeSort(nums, mid + 1, end)

            i, j = 0, 0
            res = []
            while i < len(leftSide) and j < len(rightSide):
                if leftSide[i][0] > rightSide[j][
                        0]:  #O(k-1) chia m phần mất m^2 để so sánh và merge lại
                    res.append(leftSide[i])
                    result[leftSide[i][1]] += len(rightSide) - j
                    i += 1
                else:
                    res.append(rightSide[j])
                    j += 1
            while i < len(leftSide):
                res.append(leftSide[i])
                i += 1
            while j < len(rightSide):
                res.append(rightSide[j])
                j += 1
            return res

        sortedNums = mergeSort(numsIdx, 0, len(nums) - 1)
        return result
