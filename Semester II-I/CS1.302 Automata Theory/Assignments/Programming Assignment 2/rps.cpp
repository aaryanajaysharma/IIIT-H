#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <deque>
#include <numeric>
#include <assert.h>
#include <iomanip>
#define watch(x) cout << #x << " = " << x << "\n"
#define pb __emplace_back
#define sz(x) int(x.size())
#define all(x) x.begin(), x.end()
#define ll long long int
#define ld long double
#define show(x)                     \
    for (int i = 0; i < sz(x); i++) \
    cout << x[i] << "\n"
using namespace std;

void display_fsm(int fsm[][4], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (j == 0){
                cout << (char) fsm[i][j] << " ";
            }
            else
            {
                cout << fsm[i][j] << " ";
            }
        }
        cout << "\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
    unordered_map<char, char> beats;
    beats['R'] = 'P';
    beats['P'] = 'S';
    beats['S'] = 'R';
    int n;
    cin >> n;
    // n = 30;
    // vector<vector<int> > fsm;
    int fsm1[n][4];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= 3; j++)
        {
            string s;
            cin >> s;
            if (s[0] == 'R' || s[0] == 'P' || s[0] == 'S')
            {
                fsm1[i][j] = int (s[0]);
            }
            else
            {
                // cout << stoi(s) << " ";
                fsm1[i][j] = stoi(s);
            }
        }
    }
    // cout << "\n";
    // display_fsm(fsm, n);
    // cout << "\n";
    // random_shuffle(fsm, fsm + n);
    // display_fsm(fsm, n);
    // cout << "\n";
    // initialize array a with numbers 1 to n
    // n = 999;
    // int fsm[n][4];
    // int a[n];
    // iota(a, a + n, 1);
    // random_shuffle(a, a + n);
    // for (int i = 0; i < n; i++)
    // {
    //     fsm[i][1] = a[i];
    // }
    // random_shuffle(a, a + n);
    // for (int i = 0; i < n; i++)
    // {
    //     fsm[i][2] = a[i];
    // }
    // random_shuffle(a, a + n);
    // for (int i = 0; i < n; i++)
    // {
    //     fsm[i][3] = a[i];
    // }
    // // initialize array a with n/3 'R', n/3 'P' and n/3 'S' and shuffle it
    // char b[n];
    // for (int i = 0; i < n / 3; i++)
    // {
    //     b[i] = 'R';
    // }
    // for (int i = n / 3; i < 2 * n / 3; i++)
    // {
    //     b[i] = 'P';
    // }
    // for (int i = 2 * n / 3; i < n; i++)
    // {
    //     b[i] = 'S';
    // }
    // random_shuffle(b, b + n);
    // for (int i = 0; i < n; i++)
    // {
    //     fsm[i][0] = (int) b[i];
    // }
    // count most frequent state in column 0 and 
    int count_R = 0, count_P = 0, count_S = 0;
    for (int i = 0; i < n; i++)
    {
        if (fsm1[i][0] == 'R')
        {
            count_R+=1;
        }
        else if (fsm1[i][0] == 'P')
        {
            count_P+=1;
        }
        else
        {
            count_S+=1;
        }
    }
    // fsm will be the opponent's fsm1
    int fsm[n][4];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= 3; j++)
        {
            if(j == 0){
                fsm[i][j] = (int) beats[(char)fsm1[i][j]];
            }
            else{
                fsm[i][j] = fsm1[i][j];
            }
        }
    }
    cout << n << "\n";
    display_fsm(fsm, n);
}

/*
3
R 1 2 1
P 3 2 2
S 3 3 1

4
R 2 3 3
P 4 1 1
S 1 2 1
R 1 1 3
*/