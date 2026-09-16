class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arrMap = Counter(arr)
        highest = -1 

        for i in arrMap:
            if i == arrMap[i]:
                if highest < i:
                    highest = i
        return highest
