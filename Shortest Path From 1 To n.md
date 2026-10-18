## 01. Shortest Path From 1 To n

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/shortest-path-from-1-to-n0156/1)

### Problem Description

**Task:** Consider a directed graph whose vertices are numbered from 1 to n. There is an edge from a vertex i to a vertex j if and only if either j = i + 1 or j = 3 * i. The task is to find the minimum number of edges in a path from vertex 1 to vertex n.Examples:Input: n = 4

#### Examples

##### Example 1

- **Output:**
```text
4
```
- **Explanation:** Many paths are possible from 1 to 15. Shortest one possible is, 1 - > 3 - > 4 - > 5 - > 15, of length 4.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(log n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-10-18 16:23:49
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def minimumStep (self, n):
        ret=-1
        while n:
            ret+=1
            if n%3==0:
                n//=3
            else:
                n-=1
        return ret
```

#### Solution 2 (Python)

- **Submitted:** 2026-10-18 16:23:30
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def minimumStep (self, n):
        ret=-1
        while n:
            ret+=1
            if n%3==0:
                n//=3
            else:
                n-=1
        return ret
```

*Generated on: 10/18/2026, 4:24:09 PM*