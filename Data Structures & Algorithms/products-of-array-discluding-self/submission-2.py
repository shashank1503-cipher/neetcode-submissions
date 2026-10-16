class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1]*len(nums)
        suffix_prod = [1]*len(nums)

        prefix_prod[0],suffix_prod[-1] = nums[0],nums[-1]


        for i in range(1,len(nums)):
            prefix_prod[i] = nums[i] * prefix_prod[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix_prod[i] = nums[i] * suffix_prod[i+1]

        output = [1]*len(nums)
        for i in range(len(nums)):
            before_prod = 1 if (i-1) < 0 else prefix_prod[i-1]
            after_prod = 1 if i+1 == len(output) else suffix_prod[i+1]
            output[i] = before_prod * after_prod
            
        return output
        

