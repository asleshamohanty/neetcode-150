# status: done
# difficulty: easy
# attempts: 1
# notes: using hash set for fast lookup
# link: https://leetcode.com/problems/contains-duplicate/description/

class Solution {
public:
    bool containsDuplicate(vector<int>& nums){
    unordered_set<int> s;
    for(int num : nums){
        if(s.find(num) != s.end()){ // O(1) average
            return true;
        }
        s.insert(num); // O(1) average
    }
    return false;
}
};