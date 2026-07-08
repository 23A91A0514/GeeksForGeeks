class Solution:
   
    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
    
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            # Move i to the right as long as elements are <= pivot
            while i <= high - 1 and arr[i] <= pivot:
                i += 1

            # Move j to the left as long as elements are > pivot
            while j >= low + 1 and arr[j] > pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # Swap pivot into the correct position
        arr[low], arr[j] = arr[j], arr[low]
        return j