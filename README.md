
## Understanding `list.remove()` in Python

```python
list1 = [1,2,3,4,3,1,6,5,6]
list1.remove(6)
```

### Internal Working
1. Python searches for the value `6` from left to right.
2. Once found, all elements after it are shifted one position to the left.
3. The list length is reduced by one.
4. The list capacity usually remains unchanged.
5. The removed object's memory is reclaimed only when no references to it remain.

**Time Complexity:** O(n)
