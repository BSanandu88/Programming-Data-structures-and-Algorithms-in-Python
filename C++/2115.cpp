// 2115. Find All Possible Recipes from Given Supplies
// User Accepted:1589
// User Tried:3510
// Total Accepted:1658
// Total Submissions:10341
// Difficulty:Medium
// You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

// You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

// Return a list of all the recipes that you can create. You may return the answer in any order.

// Note that two recipes may contain each other in their ingredients.
class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        int n = recipes.size(); int m = supplies.size();
        unordered_map<string, vector<string>>ingred;
        unordered_map<string, int> degree;
        for(int i=0; i<n; i++){
            degree[recipes[i]] = ingredients[i].size();
            for(auto &j : ingredients[i]){
                ingred[j].push_back(recipes[i]);
            }
        }
        unordered_set<string> s(recipes.begin(),recipes.end());
        vector<string> ans;
        queue<string> q;
        for(int i=0; i < m; i++){
            q.push(supplies[i]);
        }
        while(!q.empty()){
            string cur = q.front();
            q.pop();
            if(s.count(cur)){
                ans.push_back(cur);
            }
            for(auto &nxt : ingred[cur]){
                degree[nxt] -= 1;
                if(degree[nxt] == 0){
                    q.push(nxt);
                }
            }
        }
        return ans;
    }
};