class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []

        for i in range(n+1):
            binary = bin(i)
            num = Counter(binary)
            print(num)
            ones = num['1'] 
            count.append(ones)
        return count