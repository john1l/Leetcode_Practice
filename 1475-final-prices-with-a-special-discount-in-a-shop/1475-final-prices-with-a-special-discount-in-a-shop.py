class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        
        
        stack = [] 
        for i , p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                    prices[stack.pop( )] -=p 
            stack.append(i)
        return prices 
        
            
        
        # cannot use greedy, unless using -> O(n^2)