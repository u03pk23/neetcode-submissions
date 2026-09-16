class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #checking if all the letters in ransome note are a part of magagzine.
        #but magazine can have other letters.

        ransomMap = Counter(ransomNote)
        magazineMap = Counter(magazine)

        for ch in ransomMap: #for each character in ransomeNote
            if magazineMap.get(ch, 0) < ransomMap[ch]: #if ransome note has a hi freq
                return False
        return True
            