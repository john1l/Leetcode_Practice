class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        minCost = [0]*(len(cost)+1)

        for i in range(2, len(cost)+1):
            oneStep = minCost[i-1] + cost[i-1]
            twoStep = minCost[i-2] + cost[i-2]
            minCost[i] = min(oneStep , twoStep )
        return minCost[-1]