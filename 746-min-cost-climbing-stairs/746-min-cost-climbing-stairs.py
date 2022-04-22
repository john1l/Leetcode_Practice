class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        


        cl = len(cost)
        dp = [0]*(cl+2)
        for i in range(cl-1,-1,-1):
            dp[i] = cost[i]+ min(dp[i+1] ,dp[i+2] )
        return min(dp[0] , dp[1])