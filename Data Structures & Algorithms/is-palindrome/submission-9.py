class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str=""
        for i in s:
            if i.isalnum():
                cleaned_str+=i.lower()

        if cleaned_str==cleaned_str[::-1]:
            return True
        
        else:
            return False