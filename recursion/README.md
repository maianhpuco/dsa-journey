# Recursion 

# Memorization 
- Using @LRU_cache -> using stack for memorization.

# Backtracking 
**Template** 
```python
current_solution = []
def Choose(i):
  If (find solution or reject solution):
    record
  return
  For all candidate c of ith position:
    Choose(i+1)
    current_solution.pop()
``` 
