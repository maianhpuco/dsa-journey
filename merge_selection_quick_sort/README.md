Merge sort 
- divide
- merge
Template: 

  ```python 
  class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums, start, end):
            # DEVIDE STEPS 
            if start == end: 
                return nums[start:end+1]
            mid = start + (end - start)//2
            leftSide = mergeSort(nums, start, mid)
            rightSide = mergeSort(nums, mid + 1, end)

            i, j = 0, 0 
            res = []
            while i < len(leftSide) and j < len(rightSide): 
                if leftSide[i] < rightSide[j]:
                    res.append(leftSide[i])
                    i += 1 
                else:
                    res.append(rightSide[j])
                    j +=1 
            while i < len(leftSide):
                res.append(leftSide[i])
                i += 1  
            while j < len(rightSide):
                res.append(rightSide[j])
                j += 1 
            return res 
        return mergeSort(nums, 0, len(nums) - 1) 
  ```

  
