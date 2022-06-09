// https://leetcode.com/problems/fibonacci-number

class Solution {
public:
    int fib(int n) {
        vector<int> res(n+1, 0);
        res[0]=0;
        res[1]=1;
        for(int i=2; i<=n; i++){
            res[i]=res[i-1]+res[i-2];
        }
        return res[n];
    }
};