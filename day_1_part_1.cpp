#include <bits/stdc++.h>

using namespace std;

int main() {
    long long sum = 0;
    while (true) {
        string s;
        int first = 0;
        int last = 0;
        cin >> s;
        for (int left = 0; left < s.size(); left++) {
            if (s[left] >= 48 && s[left] <= 57) {
                first = s[left] - '0';
                break;
            }
        }
        for (auto right = s.size() - 1; right >= 0; right--) {
            if (s[right] >= 48 && s[right] <= 57) {
                last = s[right] - '0';
                break;
            }
        }
        sum = sum + (first * 10) + last;
        cout << sum << endl;
    }
}