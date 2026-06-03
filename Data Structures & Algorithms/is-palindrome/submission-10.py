class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s=""
        for i in s:
            if i.isalnum():
                clean_s+=i.lower()

        if clean_s[::-1]==clean_s:
            return True
        
        else:
            return False