class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                
                if (prices[i] >=prices[j]):
                    prices[i] -= prices[j]
                    break 
                    
        return prices 
                
            
            
        
        # cannot use greedy, unless using -> O(n^2)