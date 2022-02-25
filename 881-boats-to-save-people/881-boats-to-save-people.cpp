class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        
        int l = 0 , r = people.size()-1;
        int cnt =0;
        sort(people.begin(),people.end());
        while(l <=r){
            cnt ++;
            if( people[l]+people[r]<=limit) l++;
            r--;
        }
        return cnt; 
        
    }
};