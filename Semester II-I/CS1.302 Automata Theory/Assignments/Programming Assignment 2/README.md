# Automata Theory Q2

Report for the second programming  assignment of the Automata Theory course.

## Strategy

* Find the maximum occuring move of the opponent.
* Find the move that beats the maximum occuring move of the opponent using next_beating_state function.
* Play the move that beats the maximum occuring move of the opponent.
* Generate the next state of the opponent using the move that we played in step 3.
* Check if all the state equal.
* If all the states are equal, then transition to the winning state.
    * If not, then transition to the next state.
    * A variation of this was also tested where we continue this greedy approach until we reach a state where a single state has more than 50% of the total states. This was found to be better than the original strategy.
    * Another variant of this is where we stop at 1000/e. We get this from optimal stopping theory. This was found to be almost equal in performance to the original strategy.
* Repeat steps 1-7 until all the states are equal or we create a fsm of size 900.
* Find the majority state and transition to the winning state of the majority state.
