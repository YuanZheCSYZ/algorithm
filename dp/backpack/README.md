

## Unlimited Size and Usage

### Target Value

The only restriction is `sum(candidate) == target`. consider as weight/capacity

dp mapping is 1 x (target+1) array storing possibility of capacity `i` 
- Finding existence: `[True] + [False for _ in target]`
- Finding combinations: `[[[]]] + [[] for _ in range(target)]`

Top-down find all combinations with weight `candidates[i]` 

```python
for x in candidates:
    for i in range(0, target-x+1):
        dp[i + x].extend([c + [x] for c in dp[i]])

return dp[-1]
```

- [39 Combination Sum](./39%20Combination%20Sum.py)
- [416 Partition Equal Subset Sum](./416%20Partition%20Equal%20Subset%20Sum.py)

## Unlimited Size

###  Target Value

The only restriction is `sum(candidate) == target`. consider as weight/capacity

dp mapping is 1 x (target+1) array storing possibility of capacity `i` 
- Finding existence: `[True] + [False for _ in target]`
- Finding combinations: `[set() for _ in range(target+1)]`

Bottom-up find all combinations with weight `candidates[i]` 

```python
candidates.sort()
for c in candidates:
    if target < c:
        continue

    for x in range(target - c, 0, -1):
        dp[x + c] |= {y + (c,) for y in dp[x]}

    dp[c].add((c,))

return dp[target]

```

Build DP map of 
- [40 Combination Sum II](./40%20Combination%20Sum%20II.py)