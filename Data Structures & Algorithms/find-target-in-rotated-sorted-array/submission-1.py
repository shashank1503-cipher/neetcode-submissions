class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            l = 0
            r = len(nums)-1
            
            while l<r:
                mid = (r-l)//2 + l
                if nums[mid] > nums[r]:
                    l = mid +1
                else:
                    r = mid
            return l
        def binary_search(l,r,target):
            while l<=r:
                mid = (r-l)//2 + l
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid +1
            return -1
        
        pivot = find_pivot(nums)
        print(pivot)
        found_l = binary_search(0,pivot-1,target)
        if found_l != -1:
            return found_l
        found_r = binary_search(pivot,len(nums)-1,target)
        if found_r != -1:
            return found_r
        return -1
        