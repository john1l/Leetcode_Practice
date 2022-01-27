class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # easy 1. solution min(nums)
        # easy 2. linear search 
        # easy 3. use sort() and fine nums[0]
        if len(nums) == 1:
            return nums[0]

        left , right = 0 , len(nums)-1
        if nums[right] > nums[0]:
                    return nums[0]

        while right >= left:

            mid = (left+right)//2

            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid+1
            else: 
                right = mid-1 
        # this is an binary search that finds the max value!