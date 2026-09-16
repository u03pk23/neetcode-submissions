class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ""
        for i in digits:
            number = number + str(i)
        length_n = len(number)
        number = str(int(number) + 1)

        return list(number)
        
        

        