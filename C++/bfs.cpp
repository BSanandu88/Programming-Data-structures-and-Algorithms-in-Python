// BFS
#include<bits/stdc++.h>
#include<vector>
#include<queue>
using namespace std;

class Solution {
  public:
        vector<int> bfsOfGraph(int v, vector<int> adj[]){
            vector<int> bfs;
            vector<int> visited(v,0);
            queue<int> q;
            q.push(0);
            visited[0] = 1;
            while (!q.empty())
            {
                /* code */
                int node = q.front();
                q.pop();
                bfs.push_back(node);
                for(auto it : adj[node]){
                    if (!visited[it]){
                        q.push(it);
                        visited[it] = 1;
                    }
                }
            }
            return bfs;
        }
};

int main(){
    int testcase;
    cin >> testcase;
    // multiple graphs
    while(testcase--){
        int v,e;
        cin >> v >> e;
        vector<int> adj[v];
        for(int i=0; i<e; i++){
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        Solution obj;
        vector<int> ans = obj.bfsOfGraph(v,adj);
        for(int i=0;i<ans.size();i++){
            cout << ans[i] << " ";
        }
        cout << endl;
    }
    return 0;
}