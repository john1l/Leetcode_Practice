class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        return [ a for a , b in Counter(nums).most_common(k) ]