/* You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|. */

// 1 method
class Solution {
public:
    vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        vector<vector<int>> res;
        multimap<int,vector<int>> mp;
        for(int r = 0;r<rows;r++){
            for(int c=0;c<cols;c++){
                auto dist = abs(rCenter - r) + abs(cCenter - c);
                mp.insert({dist,{r,c}});
            }
        }
        for(const auto &[dist,coordinates] : mp){
            res.push_back(coordinates);
        }
        return res;
    }
};

// 2nd method
vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        vector<pair<int,vector<int>>> pr;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                int d = abs(rCenter-i)+abs(cCenter-j);
                vector<int> temp;
                temp.push_back(i);
                temp.push_back(j);
                pr.push_back({d,temp});
            }
        }
    sort(pr.begin(),pr.end());
    vector<vector<int>> ans;
    for(int i=0;i<pr.size();i++){
        ans.push_back(pr[i].second);
    }
    return ans;

}

// 3rd approach

vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
     vector<vector<int >> res;
     for(int i=0; i < rows; i++){
         for(int j = 0; j < cols; j++){
             res.push_back({i,j});
         }
     }
     sort(res.begin(),res.end(),[r,c](vector<int> &left,vector<int> &right){
         return abs(left[0] - r) + abs(left[1] - c) < abs(right[0] - r) + abs(right[1] - c);
     });
     return res;
}

// 4th approach
vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0){
    vector<vector<int>> m;
    m.reserve(R * C);
    queue<pair<int,int>> q;
    q.push({ro,co});
    bool v[100][100];
    memset(v,0,sizeof(v));
    v[ro][co] = true;
    pair<int,int> n[4] = {{1,0},{-1,0},{0,1},{0,-1}};
    while(!q.empty()){
        pair<int,int> u = q.front();
        q.pop();
        m.push_back({u.first,u.second});
        for(const auto &p : n){
            auto w = make_pair(u.first + p.first,u.second+p.second);
            if(w.first >= 0 and w.first < R and w.second >= 0 and w.second < C and ! v[w.first][w.second]){
                v[w.first][w.second] = true;
                q.push({w.first,w.second});
            }
        }
    }
    return m;
}