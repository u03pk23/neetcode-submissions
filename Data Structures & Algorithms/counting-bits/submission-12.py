class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []

        for i in range(n+1):
            binary = bin(i).count('1')
            count.append(binary)
        return count