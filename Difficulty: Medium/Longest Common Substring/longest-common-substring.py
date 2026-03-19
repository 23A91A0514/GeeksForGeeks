class Solution:
    def longCommSubstr(self, s1, s2):
        n = len(s1)
        m = len(s2)

        prev = [0] * (m + 1)
        cur = [0] * (m + 1)

        ans = 0    

        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    cur[ind2] = 1 + prev[ind2 - 1]
                    ans = max(ans, cur[ind2])
                else:
                    cur[ind2] = 0 
            prev = cur[:]        
        return ans  