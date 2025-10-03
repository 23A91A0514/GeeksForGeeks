class Solution:
    def possibleWords(self, arr):
        mapping = {
            2: "abc", 3: "def", 4: "ghi", 5: "jkl",
            6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }

        result = [""]   

        for digit in arr:
            if digit not in mapping:   
                continue
            temp = []
            for prefix in result:          
                for char in mapping[digit]:  
                    temp.append(prefix + char)
            result = temp

        return result
