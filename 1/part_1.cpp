#include <bits/stdc++.h>

using namespace std;

void part_1() {
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

void part_2() {
    long long sum = 0;
    while (true) {
        map<string, int> digits;
        digits["one"] = 1;
        digits["two"] = 2;
        digits["three"] = 3;
        digits["four"] = 4;
        digits["five"] = 5;
        digits["six"] = 6;
        digits["seven"] = 7;
        digits["eight"] = 8;
        digits["nine"] = 9;
        string s;
        cin >> s;
        int first = 0;
        int last = 0;
        int p_first = 0;
        int p_last = 0;
        for (int left = 0; left < s.size(); left++) {
            if (s[left] >= 48 && s[left] <= 57) {
                first = s[left] - '0';
                p_first = left;
                break;
            }
        }
        for (auto right = s.size() - 1; right >= 0; right--) {
            if (s[right] >= 48 && s[right] <= 57) {
                last = s[right] - '0';
                p_last = right;
                break;
            }
        }



    }
}

int main() {
    part_2();
}