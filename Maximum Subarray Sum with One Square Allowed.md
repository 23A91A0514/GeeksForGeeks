## 01. Maximum Subarray Sum with One Square Allowed

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/maximum-sum-subarray--143510/1)

### Problem Description

**Task:** Given an integer array arr[], find the maximum subarray sum by squaring at most one element.Examples:Input: arr[] = [-1, -2, 3, -2, 3]Output: 10Explanation: The subarray {3, -2, 3} with squaring -2 will give the maximum sum as 3 + 4 + 3 = 10.Input: arr[] = [-4, -4, -2, 5, 2, -1]Output: 27Explanation: The subarray {5, 2} with squaring 5 will give a maximum sum of 25 + 2 = 27.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-01 17:27:51
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
        res = float('-inf')
        no_sq = float('-inf')
        sq = float('-inf')

        for x in arr:
            new_no_sq = max(x, no_sq + x)
            new_sq = max(x * x, sq + x, no_sq + x * x)

            no_sq = new_no_sq
            sq = new_sq

            res = max(res, no_sq, sq)

        return res
```

*Generated on: 11/1/2026, 5:28:26 PM*