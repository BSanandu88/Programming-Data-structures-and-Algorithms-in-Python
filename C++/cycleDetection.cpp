#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
       bool checkForCycle(int s,int v,vector<int>adj[],vector<int> &vis){
           vector<int> parent(v,-1);
           queue<pair<int,int>> q;
           vis[s] = true;
           q.push({s,-1});
           while(!q.empty()){
               int node = q.front().first;
               int par = q.front().second;
               q.pop();
               for(auto it : adj[node])
               {
                   if(!vis[it]){
                       vis[it] = true;
                       q.push({it,node});
                   }else if(par != it{
                       return true;
                   }
               }
           }
           return false;
       }
public:
       bool isCycle(int v,vector<int> adj[]){
           vector<int> vis(v,0);
           for(int i=0;i<v;i++){
               if(!vis[i]){
                   if(checkForCycle(i,v,adj,vis))
                        return true;
               }
           }
           return false;
       }
};


// Driver code 
int main(){
    int tc;
    cin >> tc;
    while(tc--){
        int V,E;
        cin >> V >> E;
        vector<int> adj[V];
        for(int i=0; i<E; i++){
            int u,v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        Solution obj;
        bool ans = obj.isCycle(V,adj);
        if(ans){
            cout << 1 << endl;
        }else{
            cout << 0 << endl;
        }
    }
    return 0;
}