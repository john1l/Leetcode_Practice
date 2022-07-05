class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        nums = set(nums) 
        ans = 0 
        for x in nums: 
            if x-1 not in nums: 
                y = x+1 
                while y in nums: 
                    y +=1 
                ans = max(ans,y-x) 
        return ans 