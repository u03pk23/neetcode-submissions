class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        ones = Counter(binary)
        return ones['1']