# 101


## https://www.zhihu.com/question/36132386

1. Lower bound (target <=)
   - [Python built-in bisect_left](https://github.com/python/cpython/blob/3.9/Lib/bisect.py#L50)

   ```python
   # Searching for [l, r) first target <= x
   l = 0
   r = n # !!!
   while l < r:
       m = l + (r - l) // 2 # avoid overflow
       if array[m] < target:
           l = m + 1
       else:
           r = m
   
   return l # !!!
   ```

2. Upper bound (<= target)

   1. Lower bound - 1 
      - Upper bound < target: Lower bound (target <= target) - 1
      - Upper bound <= target: Lower bound (target < target) - 1
   1. (l, r]
      ```python
      l = 0
      r = n - 1 # !!!
      while l < r:
          m = r - (r - l) // 2
          if target < array[m]:
              r = m - 1
          else:
              l = m
      return r
      ```
3. Equal (target ==)

```python
# Searching for [l, r) first target <= x
l = 0
r = n
while l < r:
    m = l + (r - l) // 2 # avoid overflow
    if array[m] == target:
        return m
    if array[m] < target:
        l = m + 1
    else:
        r = m

return l    
```


## https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101

1. Use a logic that you can exclude `mid`

```python
if target < nums[mid]:
    hi = mid - 1
else:
    lo = mid
```

2. Keep simple loop, the only condition the loop exits is `lo == hi`

```python
while lo < hi:
```

3. Avoid infinity loop. 

   - The choice of `mid` and the shrinking logic need to work together to ensure everytime at least 1
 element is excluded
   - Think of the situation when there are only 2 elements left.
 
```python
# Right/upper mid
mid = lo + (hi - lo + 1) // 2
if nums[mid] < target:
    lo = mid + 1
else:
    hi = mid 
```

```python
# Left/lower mid
mid = lo + (hi - lo) // 2
if target < nums[mid]:
    hi = mid - 1
else:
    lo = mid
```
