class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] < value:
                idx = stack.pop()
                result[idx] = value
            stack.append(i)

        return result
