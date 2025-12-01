#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Solution {
public:
    int scoreOfString(string s) {
        int score = 0;
        for (int i = 0; i < s.size() - 1; i++) {
            score += abs(s[i] - s[i + 1]);
        }
        return score;
    }
};

int main() {
    Solution sol;
    string s1 = "hello";
    cout << "Input : " << s1 << endl;
    cout << "Score : " << sol.scoreOfString(s1) << endl; 

    return 0;
}
