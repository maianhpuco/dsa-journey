2 technique:
# Type 1: One fast and One slow
TYPE 1: Some example of this example 
- Remove duplicated from sorted array: EASY
  k đóng vai trò là con trỏ chỉ mảng đích, tìm kiếm phần tử để cho vào vị trí của nó: 
  ```python
  class Solution:
    def removeDuplication(self, nums):
      '''
      nums = [1, 1, 2, 2, 3, 4, 5, 5]
      i = 0, k=1,  
      k = 1
      
      ''' 
      if len(nums)==0
        return 0
      k = 1
      for i in range(len(nums)):
        if nums[k-1] != nums[i]:
          num[k] = nums[i]
          k+=1
    return k 
  ```
- middle of the linked list 
- linked list cycle 

# Type 2: One Pointing to the Start and One pointing to the end of the arra 
TYPE 2: One Pointer at the begining and one at the end
Note: Limit 10^6: can not using n\*n -> TLE in python

