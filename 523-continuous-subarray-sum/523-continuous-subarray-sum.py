class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        d = {0:-1}
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if k != 0:
                sums = sums %k 
            if sums in d:
                if i -d[sums]>1:
                    return True 
            if sums not in d: 
                d[sums] = i 
        return False 


