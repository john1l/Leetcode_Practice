class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ret = [] 

        for i in range(len(nums)):

            if i == 0  or nums[i-1] != nums[i]:

                left = i +1 
                right = len(nums)-1 
                while left < right: 

                    sumv = nums[i] + nums[left] + nums[right]

                    if sumv  > 0:
                        right -=1 

                    elif sumv < 0:
                        left +=1 

                    elif sumv ==0: 
                        ret.append([ nums[i] , nums[left] , nums[right] ] )
                        left +=1 
                        right -=1 
                        while left < right  and nums[left] == nums[left -1]:
                            left +=1 

        return ret 