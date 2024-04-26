# Merge sort: 
Ý tưởng là chia để trị 
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
                if leftSide[i] < rightSide[j]: #O(k-1) chia m phần mất m^2 để so sánh và merge lại 
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
TC: O(nlogn) 
SC: O(n)

[?] nếu chia thành 3 phần thì complexity là O(nlog_{3}n) (chiều cao của cây là logn) 
[?] nếu chia thành n phần thì complexity là O(n^2)  

# Quick sort: 
Ý tưởng cũng là chia để trị,
- chọn 1 phần tử để sort 
- đưa phần từ về đúng vị trí đã sort của nó bằng cách đưa các số nhỏ hơn sang bên trái và các số lớn hơn sang bên phải
- Sau đó gọi đệ quy SORT TRÁI & SORT PHẢI 
![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/a575400e-cb93-406b-a4ac-00703bb038ce)

TC: 
- Best case: O(nlogn) -> best case là binary tree -> nhưng cây có thể ko balance
- Worst case: O(n^2) (chọn ngay phải số đầu hoặc số cuối; dãy có tất cả các số bằng nhau) 
Note: Chọn random một vị trí trong array


```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        số 0, 1, 2 thì sort được nhưng nếu cho âm,0, dương thì ko dc 
        
        Có 2 pointer [2, 0, 2, 1, 1, 0] 
                    ^i  
        [0, 0, 1, 1, 2, 2]
            ^l
                     ^r  
        [-----] [-----] [-----]
        Con trỏ trái keep track mảng đầu tiên 
        Con trỏ phải keep track mảng cuối cùng 
        ví dụ :
        i = 0, j = 5 -> swap cho nhau, j sang trái vì 2 đã đúng vị trí, i vẫn = 0
        l -> before l, all value should be 0
        r -> after r, all value should be 2 
        l, r can exchange their head with the correct number   
        """ 

        left, right = 0,  len(nums) - 1
        i = 0 
        while i <= right: 
            if nums[i] == 0: 
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1  
```

Vậy nếu ko phải cờ Hà Lan mà cờ LGBT thì làm thế nào ? swap rất nhiều -> O(n) luôn 

Cách giải tổng quát hơn: 
```python
    def sortColors(self, nums: List[int]) -> None: 
        '''
        general solution
        [2, 0, 2, 1, 1, 0] 
        -> move tất cả số 0 sang trái, 1&2 sang phải 
        -> move số 1 sang trái 
        (đưa từng số vào đúng vị trí của nó)
        l: chặn đầu các số đã đưa về đúng vị trí
        r: tìm số để bán cho left (l)
        '''
        def move_left(nums, left, right, value):
            while left <= right: #value có thể là 0,1,2 
                if nums[right] == value:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1 
                else:
                    right -= 1
            return left 
        n = len(nums)
        left = move_left(nums, 0, n-1, 0) 
        move_left(nums, left , n-1, 1) 
```
Cờ k màu chạy k - 1 vòng for: 

![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/38eae28b-2f8c-48d5-9c2a-6d453d06dddc)

TC: Cờ k màu thì phải chạy k - 1 vòng for => complexity là k*n 
Nếu dùng phép sort: thì chỉ là nlogn 



