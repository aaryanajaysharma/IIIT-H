// write a program which outputs a dfa which beats another fsa in  rock paper scissor game with probability 0.5

// 0 = r , 1 = p , 2 = s
#include <iostream>
#include <ctime>
using namespace std;

struct Matrix
{
    char state;
    int transitions[3];
};

int it = 0;

#define AVGSCORE 80

Matrix output[1000];

clock_t start;


void buildDFA(Matrix *, int);

bool ifWin(char, char);

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    Matrix input[n];

    for (int i = 0; i < n; i++)
        cin >> input[i].state >> input[i].transitions[0] >> input[i].transitions[1] >> input[i].transitions[2];

    start = clock();

    buildDFA(input, n);

    return 0;
}

void setTransitions(Matrix *m, int n)
{
    output[it].transitions[0] = it + 1;
    output[it].transitions[1] = it + 1;
    output[it].transitions[2] = it + 1;
}

char whatToPlay(char c)
{
    switch (c)
    {
    case 'R':
        return 'P';
        break;
    case 'P':
        return 'S';
        break;
    case 'S':
        return 'R';
        break;
    }

    return ' ';
}

void buildDFA(Matrix *m, int n)
{
    int kForME;
    int kForOpp[n];

    for (int i = 0; i < n; i++)
    {
        output[i].state = whatToPlay(m[i].state);

        if (output[i].state == 'R')
            kForME = 0;
        else if (output[i].state == 'P')
            kForME = 1;
        else
            kForME = 2;

        if (m[i].state == 'R')
            kForOpp[i] = 0;
        else if (m[i].state == 'P')
            kForOpp[i] = 1;
        else
            kForOpp[i] = 2;

        for (int j = 0; j < 3; j++)
        {
            if (j == kForOpp[i])
                output[i].transitions[kForOpp[i]] = m[i].transitions[kForME];
            else
                output[i].transitions[j] = rand() % n + 1;
        }
    }

    float prevavg = 0;
    float avg = 0;
    int score = 0;
    Matrix betterDFA[n];

    do
    {
        for (int j = 0; j < n; j++)
        {
            Matrix MyCurrState = output[0];
            Matrix OpponentCurrState = m[j];

            for (int i = 0; i < 200; i++)
            {
                char MyCurrMove = MyCurrState.state;
                char OpponentCurrMove = OpponentCurrState.state;

                if (ifWin(MyCurrMove, OpponentCurrMove))
                    score++;

                int kForMyTransition;
                if (OpponentCurrState.state == 'R')
                    kForMyTransition = 0;
                else if (OpponentCurrState.state == 'P')
                    kForMyTransition = 1;
                else
                    kForMyTransition = 2;

                int kForOpponentTransition;
                if (MyCurrState.state == 'R')
                    kForOpponentTransition = 0;
                else if (MyCurrState.state == 'P')
                    kForOpponentTransition = 1;
                else
                    kForOpponentTransition = 2;

                MyCurrState = output[MyCurrState.transitions[kForMyTransition]];
                OpponentCurrState = m[OpponentCurrState.transitions[kForOpponentTransition] - 1];
            }
        }

        prevavg = avg;
        avg = score / 200.00;

        if(avg > prevavg)
        {
            for(int i = 0; i < n; i++)
                betterDFA[i] = output[i];
        }

        if (avg > AVGSCORE)
            break;
        else
            for (int i = 0; i < n; i++)
                for (int j = 0; j < 3; j++)
                    if (j != kForOpp[i])
                    {
                        char choose[] = {'R', 'P', 'S'};
                        output[i].state = rand() % 3;
                        output[i].transitions[j] = rand() % n + 1;
                    }
    } while (avg < AVGSCORE && (float)(clock() - start) / CLOCKS_PER_SEC < 0.99);

    cout << n << endl;
    for (int i = 0; i < n; i++)
        cout << betterDFA[i].state << " " << betterDFA[i].transitions[0] << " " << betterDFA[i].transitions[1] << " " << betterDFA[i].transitions[2] << endl;
}

bool ifWin(char my, char opp)
{
    if (my == 'P' && opp == 'R' || my == 'S' && opp == 'P' || my == 'R' && opp == 'S')
        return true;
    return false;
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