[?] inner traversal là gì? trái -> cha -> phải là gì?? 

# Recursion 
4 bước thực hiện hàm recursion:
- B1:
- B2:
- B3:
- B4: 

# Memorization 
- Using @LRU_cache -> using stack for memorization.

# Backtracking
- Độ phức tạp thường là hàm mũ 
**Template** 
Example: Counting the combination that: 1st character: F, 2nd character: S, 4th character: E 

 ![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/dab88b6e-d437-426f-90f5-f37b1d73a118)


```python
current_solution = []
def Choose(i):
  '''
  - choose(i) điểm đến tiếp theo trong hành trình
  ví dụ chọn kí tự thứ 2 
  '''
  if (find solution or reject solution):
    #đi hết rùi mới dừng 
    record
  return
  for all candidate c of ith position:
    current_solution.append(c) 
    Choose(i+1)
    current_solution.pop()
```


