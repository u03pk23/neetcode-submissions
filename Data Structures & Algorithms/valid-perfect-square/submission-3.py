class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        l = 0
        while l <= r:
            mid = (r+l) // 2 
            if mid * mid > num:
                r = mid - 1 
            elif mid * mid < num: 
                l = mid + 1
            else: return True 
        return False
