class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for i in s:
            t = ord(i)
            if  (65 <= t >= 90) or (48 <= t <= 57):
                new += i

        new = new.replace(" ", "")
        
        if new == new[::-1]:
            return True
        else: 
            return False
