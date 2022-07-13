/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:     
    vector<vector<int>> ans;

    void dfs(TreeNode *node, int dep){
        if(node == NULL) return ; 
        if( ans.size() == dep) {
            ans.push_back( vector<int>()); } 

        ans[dep].push_back(node->val); 
        dfs(node->left , dep+1) ; 
        dfs(node->right, dep+1) ; 
    }

    vector<vector<int>> levelOrder(TreeNode* root) {

        dfs(root,0);
        return ans ; 

        
    }
};