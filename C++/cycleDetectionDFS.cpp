class Solution{
    public:
            bool checkForCycle(int node,int parent,vector<int> &vis,vector<int> adj[]){
                vis[node] = 1;
                for(auto it : adj[node]){
                    if(!vis[it]){
                        if(checkForCycle(it,node,vis,adj))
                            return true;
                    }else if(it != parent)
                            return true;
                }
                return false;
            }
    public:
            bool isCycle(int v,vector<int> adj[]){
                vector<int> vis(v+1,0);
                for(int i=0;i<v;i++){
                    if(!vis[i]){
                        if(checkForCycle(i,-1,vis,adj)) return true;
                    }
                }
                return false;
            }
}