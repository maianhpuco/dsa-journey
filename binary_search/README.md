# Binary Search
- ý tưởng: search trên 1 dãy có tính chất đặc biệt 
  + đồng biến
  + nghịch biến
  + một tính chất đặc biệt nào khác
- binary search duy trì 3 chỉ số chính
  + `left`: biên trái của dãy tìm kiếm
  + `right`: biên phải của dãy tìm kiếm
  + `mid`: phần tử giữa của dãy tìm kiếm
- binary search áp dụng điều kiện tìm kiếm vào phần tử `mid`
- nếu điều kiện không thỏa thì 1 nửa của dãy sẽ bị loại
- tuật toán sẽ tìm kiếm trên 1 nửa còn lại cho đến khi dãy tìm kiếm rỗng hoặc đã tìm dc giá trị thỏa mãn

  - B1: xác định left, right, mid
  - B2: xác định hàm if
  - B3: base-case

# Dạng 1: Search a target in a sorted array - Basic 
Ví dụ: cho dãy `n` số nguyên `nums` sắp xếp theo thứ tự tăng dần, và 1 số nguyên `target`. Tìm kiếm `target` trên mảng `nums`, nếu tìm thấy `target` trả về chỉ số trên mảng, nếu không thì trả về -1. 
```
1 <= nums.length <= 10^5 --> để ko search O(n)
-10^4 < nums[i], target < 10^4
các phần tử phân biệt 
```
vd 
```
target=13
[1,5,6,10,13,17,18,20,25,30,32,40,45,49,60
```
![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/bf26f2e7-3eea-4071-9f16-7aec232a6ec1)

 ![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/ed19ff0b-c8d0-4ef0-bdd4-eb9eefe66077)

![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/c84b5787-13d9-4237-af21-85cebfc20e0e)

```python
class Solution:
  def search(self, nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] > target:
        right = mid -1
      else:
        left = mid +1
    return -1 
```
# Dạng 2: Search a target in a sorted array - lower bound: 
 ![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/837ddd01-f11b-4edc-83e6-add3493639c6)
- Chèn bên trái nhất (mà lớn hơn hoặc bằng target): 
   ![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/4056dd44-08b4-40d6-b057-ea2e39c05063)
  Implementation:
  ```python
  def lowerBound(nums, target):
    left = 0
    right = len(nums) - 1
    ans = len(nums)
  
    while left <= right:
      mid = start + (end - start) // 2
      if nums[mid] >= target:
        ans = mid
        right = mid -1
      else:
        left = mid + 1
    return ans 
  ```
  



