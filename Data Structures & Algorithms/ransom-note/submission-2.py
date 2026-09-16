class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        construct = ransomNote
        word = list(magazine)
        letters = ""

        if len(magazine) < len(construct):
            return False

        for i in construct:
            if i in word:
                word.remove(i)
            else: 
                return False
        return True 