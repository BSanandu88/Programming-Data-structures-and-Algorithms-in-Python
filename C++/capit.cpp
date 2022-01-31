#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string capitalizeTitle(string title) {
        vector<string> v;
        string ans = "";
        for(int i=0;i<title.size();i++){
            if(title[i] != ' '){
                ans += title[i];
            }else if(title[i] == ' '){
                v.push_back(ans);
                ans = "";
            }
        }
        return title;
    }
};

int main(){
    Solution s;
    string x = s.capitalizeTitle("First leTTeR of EACH Word");
    cout << x << endl;
    return 0;
}