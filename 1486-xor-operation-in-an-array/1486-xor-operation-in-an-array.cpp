class Solution {
public:
    int xorOperation(int n, int start) {
        
        
        int ans =0; 
        for ( auto i=0; i <n  ; i++){
    
    ans ^= start+i*2;    
}
        
        return ans;
        
        
        
        
    }
};