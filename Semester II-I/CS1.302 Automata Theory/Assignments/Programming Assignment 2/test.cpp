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

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
    // create a 2d array with 3 rows and 4 columns
    vector<int> x = { 1, 2, 3, 4 };
    for (int i = 0; i < 4; i++)
    {
        cout << x[i] << "\n";
    }
    return 0;
}