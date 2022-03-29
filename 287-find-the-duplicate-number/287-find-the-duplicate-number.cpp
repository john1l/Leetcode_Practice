class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        unordered_set<int> seen; 
        for (auto &n:nums) {
            if (seen.count(n))
                return n;
            seen.insert(n);
        }
        return -1;
    }
};