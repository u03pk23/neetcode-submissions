class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        length = len(g)
        length_s = len(s)
        i = 0
        j = 0


        while i < length and j < length_s:
            if s[j] >= g[i]:
                i +=1
            j +=1
        return i
        
         