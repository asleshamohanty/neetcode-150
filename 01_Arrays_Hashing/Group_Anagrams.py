# status: done
# difficulty: medium
# attempts: 2
# notes: map sorted string to vector of anagrams, then return the values of the map
# link: https://leetcode.com/problems/group-anagrams/description/

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mpp;
        for(string s:strs){
            string temp = s;
            sort(temp.begin(),temp.end());
            mpp[temp].push_back(s);
        }
        vector<vector<string>> result;
        for(auto it:mpp){
            result.push_back(it.second);
        }
        return result;
    }
};
