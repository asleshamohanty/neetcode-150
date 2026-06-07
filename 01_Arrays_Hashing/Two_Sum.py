# status: done
# difficulty: easy
# attempts: 1
# notes: unordered map to store the index of the complement, if found return the indices, else add the current number and index to the map
# link: https://leetcode.com/problems/two-sum/description/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int,int> mpp;
        int n=nums.size();
        for(int i=0;i<n;i++){
            int n2 = target - nums[i];
            if(mpp.find(n2)!=mpp.end()){ //!= means found
                return {mpp[n2], i};
            }
            else mpp[nums[i]] = i;
        }
        return {};
    }
};
