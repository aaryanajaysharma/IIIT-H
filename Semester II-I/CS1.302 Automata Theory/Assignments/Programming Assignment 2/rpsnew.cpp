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
#define pb emplace_back
#define sz(x) int(x.size())
#define all(x) x.begin(), x.end()
#define ll long long int
#define ld long double
#define show(x) for(int i = 0; i < sz(x); i++) cout << x[i] << "\n"
using namespace std;
int index = 1;
unordered_map<int, set<int> > state_map;

void display_fsm(int fsm[][4], int n);
void display_fsm(vector<vector<int> > fsm, int n);
char beats(char c);
char next_beating_move(set<int> S, int n, int fsm[][4]);
void input_fsm(int fsm[][4], set<int> S, int n);
void fsm_construction(set<int> S[], char played_move);

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
    int n;
    cin >> n;
    int fsm[n][4];
    set<int> S;
    input_fsm(fsm, S, n);
    char played_move = next_beating_move(S, n, fsm);
    fsm_construction(S, played_move);
    display_fsm(fsm, n);
    return 0;
}


void fsm_construction(set<int> S, char played_move){
    char opponent_move = 'R';
    if(state_map.count(index))
        state_map[index] = S;
    

}

void input_fsm(int fsm[][4], set<int> S, int n){
    for (int i = 0; i < n; i++)
    {
        char state;
        cin >> state;
        fsm[i][0] = (int) state;
        S.insert(i+1);
        for (int j = 1; j < 4; j++)
        {
            int transition;
            cin >> transition;
            fsm[i][j] = transition;
        }
    }
}

void display_fsm(int fsm[][4], int n)
{
    cout << n << "\n";
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (j == 0)
            {
                cout << (char)fsm[i][j] << " ";
            }
            else
            {
                if(j < 3)
                cout << fsm[i][j] << " ";
                else
                cout << fsm[i][j];
            }
        }
        cout << "\n";
    }
}

void display_fsm(vector<vector<int> > fsm, int n)
{
    cout << n << "\n";
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (j == 0)
            {
                cout << (char)fsm[i][j] << " ";
            }
            else
            {
                if(j < 3)
                cout << fsm[i][j] << " ";
                else
                cout << fsm[i][j];
            }
        }
        cout << "\n";
    }
}
char beats(char c)
{
    if (c == 'R')
    {
        return 'P';
    }
    else if (c == 'P')
    {
        return 'S';
    }
    else
    {
        return 'R';
    }
}

char next_beating_move(set<int> S, int n, int fsm[][4])
{
    unordered_map<char, int> freq;
    freq['R'] = 0;
    freq['P'] = 0;
    freq['S'] = 0;
    for(auto it = S.begin(); it != S.end(); it++)
    {
        freq[(char)fsm[*it - 1][0]]++;
    }
    int max_freq = 0;
    char max_state = 'R';
    unordered_map<char, int>::iterator it = freq.begin();
    for (it = freq.begin(); it != freq.end(); it++)
    {
        if (it->second > max_freq)
        {
            max_freq = it->second;
            max_state = it->first;
        }
    }
    return beats(max_state);
}