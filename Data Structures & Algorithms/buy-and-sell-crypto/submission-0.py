class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow, fast = 0,1
        ans = 0
        while fast < len(prices):
            if prices[slow] > prices[fast]:
                slow +=1
            else:
                diff = prices[fast] - prices[slow]
                ans = max(diff,ans)
                fast +=1
            if slow == fast:
                fast = slow +1
        return ans
        