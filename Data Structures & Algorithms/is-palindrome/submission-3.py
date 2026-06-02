class Solution:
    def isPalindrome(self, s: str) -> bool:
        newtxt=""
        for c in s:
            if c.isalnum():
                newtxt+=c.lower()
            
        return newtxt==newtxt[::-1]