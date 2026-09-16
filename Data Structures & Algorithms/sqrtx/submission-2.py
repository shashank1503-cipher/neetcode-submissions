class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0
        while l<=r:
            mid = (r-l)//2 + l
            print(mid)
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid -1
            else:
                l = mid+1
                res = mid
        return res
        