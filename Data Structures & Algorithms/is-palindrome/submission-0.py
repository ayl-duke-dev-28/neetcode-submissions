class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        while i < len(s):
            if not s[i].isalnum():
                s = s[:i] + s[i+1:]
            else:
                i += 1
        
        for i in range(len(s)//2):
            if s[i] != s[len(s) - 1 - i]:
                return False

        return True