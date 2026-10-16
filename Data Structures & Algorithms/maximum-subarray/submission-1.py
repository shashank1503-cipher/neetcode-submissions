class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        curr_sum = 0
        for i in nums:
            curr_sum+= i
            ans = max(curr_sum,ans)
            if curr_sum <0:
                curr_sum =0
        return ans
