# Eval Script for automata assignment
To use the script do the following

- run `test_case_generator.sh` , this will add randomized test cases to the `test_cases` folder

- store your programs inside `student programs` in the following format

```
    student_programs
        ----Roll_Number
            ----program.cpp

```


- results will be stored in results.csv, as well as shown on the terminal. Count of MLE/TLEs will be shown as "Total ERR:"

- TLEs/MLEs are automatically given a score of 0 for that input.

- Average is just the mean no. of wins over all (round, initial state, input) triplets. Weighted Average is the weighted average with weights being the number of states in the test case, note that we will be using the normal average and NOT the weighted one, the latter is only there for you to understand how well your program is performing against larger test cases

