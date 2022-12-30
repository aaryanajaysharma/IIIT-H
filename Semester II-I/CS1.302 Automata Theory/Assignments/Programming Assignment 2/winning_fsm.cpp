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
#define show(x) for(int i = 0; i < sz(x); i++) cout << x[i] << "\n"
using namespace std;

void display_fsm(int fsm[][4], int n);
void display_fsm(vector<int* > fsm, int n);

/*

Given a finite state machine as follows:

3
S 3 1 1
R 2 1 2
P 3 3 2

The first line is the number of states in the FSM.

The next lines are the states, where the first character is the state name, and the next three are the transitions for the states R, P, and S respectively.

The first state is the initial state.

Program a function that takes a finite state machine as input and returns a finite state machine that beats the input finite state machine.

*/

char get_transition(char state, char input, int fsm[][4], int n);



vector<int*> wfsm(int fsm[][4], int n){
    vector<int*> winning_fsm;
    for (int i = 0; i < n; i++)
    {
        int* state = new int[4];
        state[0] = fsm[i][0];
        for (int j = 1; j < 4; j++)
        {
            state[j] = fsm[fsm[i][j] - 1][j];
        }
        winning_fsm.pb(state);
    }
    return winning_fsm;
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
    // n < 30
    int fsm[n][4];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= 3; j++)
        {
            if (j == 0)
            {
                char c;
                cin >> c;
                fsm[i][j] = (int) c;
            }
            else
            {
                int x;
                cin >> x;
                fsm[i][j] = x;
            }
        }
    }

    vector<int*> winning_fsm;
    unordered_set<int> visited;
    int next_state = 1;
    while(visited.count(next_state) == 0)
    {
        visited.insert(next_state);
        char opponent_move = (char) fsm[next_state - 1][0];
        char fsm_move = beats[opponent_move];
        // now we know what to play, and what we play will determine the opponents next move and state
        if(fsm_move == 'R')
        {
            if(next_state == fsm[next_state - 1][1])
            {
                int temp[4] = {'R', -1, -1, winning_fsm.size() + 1};
                winning_fsm.pb(temp);
            }
            else
            {
                next_state = fsm[next_state - 1][1];
                if(visited.count(next_state) == 1)
                {
                    int temp[4] = {'R', -1, -1, next_state};
                    winning_fsm.pb(temp);
                }
                else{
                    int temp[4] = {'R', -1, -1, winning_fsm.size() + 2};
                    winning_fsm.pb(temp);
                }
            }
        }
        else if(fsm_move == 'P')
        {
            if(next_state == fsm[next_state - 1][2])
            {
                int temp[4] = {'P', winning_fsm.size()+1, -1, -1};
                winning_fsm.pb(temp);
            }
            else
            {
                next_state = fsm[next_state - 1][2];
                if(visited.count(next_state))
                {
                    int temp[4] = {'P', next_state, -1, -1};
                    winning_fsm.pb(temp);
                }
                else
                {
                    int temp[4] = {'P', winning_fsm.size()+2, -1, -1};
                    winning_fsm.pb(temp);
                }
            }
        }
        else
        {
            if(next_state == fsm[next_state - 1][3])
            {
                int temp[4] = {'S', -1, winning_fsm.size()+1, -1};
                winning_fsm.pb(temp);
            }
            else
            {
                next_state = fsm[next_state - 1][3];
                if(visited.count(next_state)){
                    int temp[4] = {'S', -1, next_state, -1};
                    winning_fsm.pb(temp);
                }
                else{
                    int temp[4] = {'S', -1, winning_fsm.size()+2, -1};
                    winning_fsm.pb(temp);
                }
            }
        }
        
    }

    for (int i = 0; i < winning_fsm.size(); i++)
    {
        for (int j = 1; j < 4; j++)
        {
            if(winning_fsm[i][j] == -1)
            {
                winning_fsm[i][j] = i + 1;
            }
        }
    }

    cout << sz(winning_fsm) << "\n";
    display_fsm(winning_fsm, sz(winning_fsm));
    // vector<int*> w_fsm = wfsm(fsm, n);
    // cout << w_fsm.size() << "\n";
    // display_fsm(w_fsm, sz(w_fsm));
    return 0;
}


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

void display_fsm(vector<int*> fsm, int n)
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