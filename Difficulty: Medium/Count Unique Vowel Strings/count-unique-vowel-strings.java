import java.util.*;

class Solution {
    public int vowelCount(String s) {
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        Map<Character, Integer> freq = new HashMap<>();
        
        for (char c : s.toCharArray()) {
            if (vowels.contains(c)) {
                freq.put(c, freq.getOrDefault(c, 0) + 1);
            }
        }
        
        int count = freq.size();
        if (count == 0) return 0;
        
        int waysToPick = 1;
        for (int val : freq.values()) {
            waysToPick *= val;
        }
        
        int permutations = factorial(count);
        return waysToPick * permutations;
    }
    
    private int factorial(int n) {
        int res = 1;
        for (int i = 2; i <= n; i++) {
            res *= i;
        }
        return res;
    }
}
