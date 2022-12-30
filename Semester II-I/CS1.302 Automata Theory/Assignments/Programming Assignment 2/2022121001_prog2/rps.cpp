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
#define show(x)                     \
    for (int i = 0; i < sz(x); i++) \
    cout << x[i] << "\n"
using namespace std;

/*
Strategy:
1. Find the maximum occuring move of the opponent.
2. Find the move that beats the maximum occuring move of the opponent using next_beating_state.
3. Play the move that beats the maximum occuring move of the opponent.
4. Generate the next state of the opponent using the move that we played in step 3.
5. Check if all the state equal.
6. If all the states are equal, then transition to the winning state.
7. If not, then transition to the next state.
8. Repeat steps 1-7 until all the states are equal or we create a fsm of size 900.
9. If states are not equal, find the majority state and transition to the winning state of the majority state.
*/

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

pair<int, int> majority_state(int S[], int n)
{
    unordered_map<int, int> freq;
    for (int i = 0; i < n; i++)
    {
        freq[S[i]]++;
    }
    int max_freq = 0;
    int max_state = 0;
    // declare a map iterator
    unordered_map<int, int>::iterator it = freq.begin();
    for (it = freq.begin(); it != freq.end(); it++)
    {
        if (it->second > max_freq)
        {
            max_freq = it->second;
            max_state = it->first;
        }
    }
    return make_pair(max_state, max_freq);
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
char next_beating_move(int S[], int n, int fsm[][4])
{
    // count most frequent state in column 0
    unordered_map<char, int> freq;
    freq['R'] = 0;
    freq['P'] = 0;
    freq['S'] = 0;
    for (int i = 0; i < n; i++)
    {
        freq[(char)fsm[S[i] - 1][0]]++;
    }
    int max_freq = 0;
    char max_state = 'R';
    // declare a map iterator
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

void next_state(int S[], int n, char played_state, int fsm[][4])
{
    if (played_state == 'R')
    {
        for (int i = 0; i < n; i++)
        {
            S[i] = fsm[S[i] - 1][1];
        }
    }
    else if (played_state == 'P')
    {
        for (int i = 0; i < n; i++)
        {
            S[i] = fsm[S[i] - 1][2];
        }
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            S[i] = fsm[S[i] - 1][3];
        }
    }
}

vector<vector<int> >  winning_fsm_creation(int fsm[][4]);

bool check_equal_states(int S[], int n)
{
    int first = S[0];
    for (int i = 1; i < n; i++)
    {
        if (S[i] != first)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
    int n;
    cin >> n;
    int fsm1[n][4];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= 3; j++)
        {
            string s;
            cin >> s;
            if (s[0] == 'R' || s[0] == 'P' || s[0] == 'S')
            {
                fsm1[i][j] = int(s[0]);
            }
            else
            {
                fsm1[i][j] = stoi(s);
            }
        }
    }
    int S[n]; // S is the initial/current state of the opponent FSM
    for (int i = 1; i <= n; i++)
    {
        S[i - 1] = i;
    }

    vector<vector<int> > fsm;
    while (majority_state(S, n).second < n/2 && fsm.size() <= 368)
    {
        char played_state = next_beating_move(S, n, fsm1);
        next_state(S, n, played_state, fsm1);
        if (played_state == 'R')
        {
            vector<int> temp;
            temp.push_back('R');
            temp.push_back(-1);
            temp.push_back(-1);
            temp.push_back(fsm.size() + 2);
            fsm.pb(temp);
        }
        else if (played_state == 'P')
        {
            vector<int> temp;
            temp.push_back('P');
            temp.push_back(fsm.size() + 2);
            temp.push_back(-1);
            temp.push_back(-1);
            fsm.pb(temp);
        }
        else
        {
            vector<int> temp;
            temp.push_back('S');
            temp.push_back(-1);
            temp.push_back(fsm.size() + 2);
            temp.push_back(-1);
            fsm.pb(temp);
        }
    }

    // asssume the majority state is the current state and transistion to the winning state that beats the majority state
    int current_state = majority_state(S, n).first;
    swap(fsm1[0], fsm1[current_state - 1]);
    for (int i = 0; i < n; i++)
    {
        for (int j = 1; j < 4; j++)
        {
            if (fsm1[i][j] == 1)
                fsm1[i][j] = current_state;
            else if (fsm1[i][j] == current_state)
                fsm1[i][j] = 1;
        }
    }
    vector<vector<int> > winning_fsm = winning_fsm_creation(fsm1);
    int fsm_size = fsm.size();
    for (int i = 0; i < winning_fsm.size(); i++)
    {
        for (int j = 1; j < 4; j++)
        {
            if (winning_fsm[i][j] != -1)
            {
                winning_fsm[i][j] += fsm_size;
            }
        }
        fsm.pb(winning_fsm[i]);
    }
    for (int i = 0; i < fsm.size(); i++)
    {
        for (int j = 1; j < 4; j++)
        {
            if (fsm[i][j] == -1)
            {
                fsm[i][j] = i + 1;
            }
            if(fsm[i][j]>fsm.size()) fsm[i][j] = 1;
        }
    }
    display_fsm(fsm, fsm.size());
}

vector<vector<int> > winning_fsm_creation(int fsm[][4])
{
    vector<vector<int> > winning_fsm;
    unordered_set<int> visited;
    int next_state = 1;
    while (visited.count(next_state) == 0)
    {
        visited.insert(next_state);
        char opponent_move = (char)fsm[next_state - 1][0];
        char fsm_move = beats(opponent_move);
        // now we know what to play, and what we play will determine the opponents next move and state
        if (fsm_move == 'R')
        {
            if (next_state == fsm[next_state - 1][1])
            {
                vector<int> temp;
                temp.pb('R');
                temp.pb(-1);
                temp.pb(-1);
                temp.pb(winning_fsm.size() + 1);
                winning_fsm.pb(temp);
            }
            else
            {
                next_state = fsm[next_state - 1][1];
                if (visited.count(next_state) == 1)
                {
                    vector<int> temp;
                    temp.pb('R');
                    temp.pb(-1);
                    temp.pb(-1);
                    temp.pb(next_state);
                    winning_fsm.pb(temp);
                }
                else
                {
                    vector<int> temp;
                    temp.pb('R');
                    temp.pb(-1);
                    temp.pb(-1);
                    temp.pb(winning_fsm.size() + 2);
                    winning_fsm.pb(temp);
                }
            }
        }
        else if (fsm_move == 'P')
        {
            if (next_state == fsm[next_state - 1][2])
            {
                vector<int> temp;
                temp.pb('P');
                temp.pb(winning_fsm.size() + 1);
                temp.pb(-1);
                temp.pb(-1);
                winning_fsm.pb(temp);
            }
            else
            {
                next_state = fsm[next_state - 1][2];
                if (visited.count(next_state))
                {
                    vector<int> temp;
                    temp.pb('P');
                    temp.pb(next_state);
                    temp.pb(-1);
                    temp.pb(-1);
                    winning_fsm.pb(temp);
                }
                else
                {
                    vector<int> temp;
                    temp.pb('P');
                    temp.pb(winning_fsm.size() + 2);
                    temp.pb(-1);
                    temp.pb(-1);
                    winning_fsm.pb(temp);
                }
            }
        }
        else
        {
            if (next_state == fsm[next_state - 1][3])
            {
                vector<int> temp;
                temp.pb('S');
                temp.pb(-1);
                temp.pb(winning_fsm.size() + 1);
                temp.pb(-1);
                winning_fsm.pb(temp);
            }
            else
            {
                next_state = fsm[next_state - 1][3];
                if (visited.count(next_state))
                {

                    vector<int> temp;
                    temp.pb('S');
                    temp.pb(-1);
                    temp.pb(next_state);
                    temp.pb(-1);
                    winning_fsm.pb(temp);
                }
                else
                {
                    vector<int> temp;
                    temp.pb('S');
                    temp.pb(-1);
                    temp.pb(winning_fsm.size() + 2);
                    temp.pb(-1);
                    winning_fsm.pb(temp);
                }
            }
        }
    }
    return winning_fsm;
}

/*
3
R 1 2 1
S 3 2 2
P 3 3 1

4
R 2 3 3
P 4 1 1
S 1 2 1
R 1 1 3
*/

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
// fsm will beat the opponent's fsm1

// int fsm[n+900][4];
// // initialize coloumn 1, 2, 3 of fsm with -1
// for (int i = 0; i < n+900; i++)
// {
//     for (int j = 1; j <= 3; j++)
//     {
//         fsm[i][j] = -1;
//     }
// }
// int row = 0;
// bool flag = false;
// while(majority_state(S, n).second <= n/2){
//     char played_state = next_beating_move(S, n, fsm1);
//     next_state(S, n, played_state, fsm1);

//     fsm[row][0] = int(played_state);
//     if(played_state == 'R'){
//         fsm[row][3] = row+2;
//     }
//     else if (played_state == 'P')
//     {
//         fsm[row][1] = row+2;
//     }
//     else
//     {
//         fsm[row][2] = row+2;
//     }
//     row++;
//     if(row > 900){
//         flag = true;
//         fsm[row][0] = 'R';
//         fsm[row][1] = 1;
//         break;
//     }
// }

// int current_state = majority_state(S, n).first;
// int winnig_fsm[100][4];
// for (int i = 0; i < row; i++)
// {
//     for (int j = 1; j < 4; j++)
//     {
//         if(fsm[i][j] == -1){
//             fsm[i][j] = i+1;
//         }
//     }
// }