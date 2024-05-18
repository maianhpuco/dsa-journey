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

Dạng bài toán tiêu biểu là 2 sum và 3 sum 
```python
class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Sort the array first
        n = len(nums)
        res = []
        
        for k in range(n - 2):
            # Skip the same element to avoid duplicate triplets
            if k > 0 and nums[k] == nums[k - 1]:
                continue
                
            target = -nums[k]
            l, r = k + 1, n - 1
            
            while l < r:
                current_sum = nums[l] + nums[r]
                if current_sum == target:
                    res.append([nums[k], nums[l], nums[r]])
                    
                    # Skip duplicates for l
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # Skip duplicates for r
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
                elif current_sum < target:
                    l += 1
                else:
                    r -= 1
        
        return res 
```
3 sum smaller :
```python
class Solution:
    def treeSumSmaller(self, nums, target):
        k = 0
        n = len(nums)
        nums.sort()  # O(sorted)
        ans = 0
        while k < n - 2:
            l, r = k + 1, n - 1
            while l < r:
                if nums[l] + nums[r] < target - nums[k]:
                    ans += r - l  # --> SMART
                    l += 1  # -> #SMART # các số từ right trổ về trc sẽ thỏa mãn đk đề 
                else: # các ở right thì dùng left nào cũng ko thỏa mãn đk đề 
                    r -= 1
            k += 1

        return ans 
```

[?] Time complexity * Space complexity của bài toán này là gì (thường 2 sum là N), vì mỗi lần loop mình cập nhật left hoặc right. 

# Slicing Window 
Có 2 con trỏ và 1 biến data 
2 con trỏ l, r giữ biên của array và biến data curSum giữa giá trị của array
