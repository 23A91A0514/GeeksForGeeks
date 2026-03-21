class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
       
        for i in range(len(arr)):
            map = {}
           
            for j in range(i+1, len(arr)):
                n3 = target - arr[i] - arr[j]
                
                if n3 in map:
                    return True
                else:
                    map.update({arr[j]:j})
                
        return False