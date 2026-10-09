## 01. Minimum Operations to Reach n

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/find-optimum-operation4504/1)

### Problem Description

**Task:** Given a number n. Find the minimum number of operations required to reach n starting from 0. You have two operations available:Double the number Add one to the numberExamples:Input: n = 8

#### Examples

##### Example 1

- **Output:**
```text
4
```
- **Explanation:** 0 + 1 = 1 -- > 1 + 1 = 2 -- > 2 * 2 = 4 -- > 4 * 2 = 8.

##### Example 2

- **Input:**
```text
n = 7
```
- **Output:**
```text
5
```
- **Explanation:** 0 + 1 = 1 -- > 1 + 1 = 2 -- > 1 + 2 = 3 -- > 3 * 2 = 6 -- > 6 + 1 = 7.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(log n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-10-09 19:38:03
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def minOperation(self, n):
        cnt=0
        while n:
            if n%2==0:
                n//=2
                cnt+=1
            else:
                n-=1
                cnt+=1
            
        return cnt
```

#### Solution 2 (Python)

- **Submitted:** 2026-10-09 19:12:03
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def minOperation(self, n):
        cnt=0
        while n:
            if n%2==0:
                n//=2
            else:
                n-=1
            cnt+=1
        return cnt
```

*Generated on: 10/9/2026, 7:48:44 PM*