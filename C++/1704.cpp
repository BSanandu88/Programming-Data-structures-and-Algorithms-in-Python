// You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

// Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

// Return true if a and b are alike. Otherwise, return false.

 
 class Solution {
public:
    bool halvesAreAlike(string s) {
        int n = s.length();
        string s1 = s.substr(0,n/2);
        string s2 = s.substr(n/2,n);
        //cout << s1 << " " << s2 << endl;
        vector<char> v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int count1 = 0,count2 = 0;
        for(int i=0;i<s1.length();i++){
            for(int j=0;j<v.size();j++){
                if(s1[i] == v[j]) count1 += 1;
            }
        }
        for(int i=0;i<s2.length();i++){
            for(int j=0;j<v.size();j++){
                if(s2[i] == v[j]) count2 += 1;
            }
        }
        if(count1 == count2) return true;
        return false;
    }
};