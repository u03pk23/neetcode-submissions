class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = Counter(nums)
        highest = numsMap.most_common()
        new = []
        for i in range(k):
            new.append(highest[i][0])
        return new