class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        ones = Counter(binary)
        print(ones)
        return ones['1']