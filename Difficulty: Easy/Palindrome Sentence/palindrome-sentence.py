class Solution:
    def isPalinSent(self, s):
        # Clean the string: keep only alphanumeric characters and convert to lowercase
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        
        # Check if cleaned string is a palindrome
        return cleaned == cleaned[::-1]
