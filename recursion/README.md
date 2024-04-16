# Recursion 

# Memorization 
- Using @LRU_cache -> using stack for memorization.

# Backtracking 
**Template** 
Example: Counting the combination that: 1st character: F, 2nd character: S, 4th character: E 

 ![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/dab88b6e-d437-426f-90f5-f37b1d73a118)


```
current_solution = []
def Choose(i):
  If (find solution or reject solution):
    record
  return
  For all candidate c of ith position:
    Choose(i+1)
    current_solution.pop()
``` 
