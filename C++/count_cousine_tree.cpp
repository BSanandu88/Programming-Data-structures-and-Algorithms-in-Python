// Given a binary tree and a node, print all cousins of given node in order of their appearance. Note that siblings should not be printed.

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    vector<int> printCousins(Node* root, Node* node_to_find)
    {
        //code here
        bool found = true;
        queue<Node*> q;
        q.push(root);
        while(!q.empty() && found){
            int n = q.size();
            for(int i = 0; i < n; i++){
                Node* node = q.front(); q.pop();
                if(node->left == node_to_find or node->right == node_to_find){
                    found = false;
                }else{
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }
        }
    }
    if(q.empty()) return {-1};
    else{
        vector<int> res;
        while(!q.empty()){
            res.emplace_back(q.front()->data);
            q.pop();
        }
        return res;
        }
    }  
    
};

