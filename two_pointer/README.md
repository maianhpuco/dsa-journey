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

# Type 2: One Pointing to the Start and One pointing to the end of the array 
Bài toán two sum: 
Ví dụ: Cho dãy `n` số nguyên `arr` sắp xếp theo thứ tự tăng dần và số nguyên `target`. Hỏi, có tồn tại 2 phần tử nào trong mảng sao cho tổng của chúng bằng target hay không? Nếu tồn tại trả về chỉ số vị trí của 2 phần tử đó, nếu không thì trả về [-1, -1] 

Note: mảng có sắp xếp, trông có vẻ như là cần vét cạn nhưng nếu dùng cách này có thể tận dụng dc tính đã sắp xếp của mảng.
Bài toán này: 
=> 2 pointers sẽ là O(n)
Trong khi dùng binary search là O(nlogn)
Còn TH ko dùng cách này có thể dùng Hash cũng là O(n) (nhưng dùng cách này thì ko tận dụng dc tính chất mảng sắp xếp tăng dần)
Example: 
```python
def two_sum(nums: List[int], target: int) -> List[int]:
  left = 0
  right = len(nums)-1
  while left < right:
    if nums[left] + nums[right] == target:
      return [left, right]
    elif nums[left] + nums[right] > target: #nếu nums[left] đã lớn hơn thì nums[left++] đều không thỏa
      right+=1 #get rid of current right
    else:
      left-=1
  return [-1, -1]    
```
TYPE 2: One Pointer at the beginning and one at the end
Note: Limit 10^6: can not using n\*n -> TLE in python 

