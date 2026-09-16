class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number = Counter(nums)
        print(number)
        for i in number:
            print(i)
            if number[i] > 1:             
                return True
        return False
