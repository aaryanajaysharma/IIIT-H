# Operating system & networks
## Assignment 5

### Question 1

You have been asked by the student council to monitor the use of washing machines in OBH. You have to report the events of the day in the format provided by the council with some statistics. In your conclusion line, you have to report if more washing machines are needed or not. More washing machines are needed if at least 25% of the students who came to the machines returned without getting their clothes washed.

During the entire day:
* `N` students will come to get their clothes washed
* There are `M` functioning washing machines
* The time at which the `i`-th student comes is T_i seconds after the execution of the program
* The time taken to wash the `i`-th student's clothes is W_i seconds
* The patience of the `i`-th student is P_i seconds, after which he leaves without getting his clothes washed

#### Approach

We have used semaphore and mutex to simulate the event. We have used a counting semaphore to make sure that at most `M` student can use the washing machine at a time. We have used a mutex to calculate the total time wasted by the students who left without getting their clothes washed and those who had to wait to get their clothes washed.

#### Assumptions

* A buffer of 0.1 seconds is added to `ts.tv_nsec` to account for the time taken by the system to execute the intermediate instructions/code

#### Known issues and limitations

* The code does not run as expected on macOS. The reason perhaps is due to `sem_init` function inter-alia being deprecated and not supported on macOS. The code has been tested on Ubuntu 22.10 & onlineGDB, and is working as expected.

#### Variables
* `mutex` is used on the variable `total_time_wasted` as it is a shared variable among thread which can cause race condition.

* `semaphore` is used to make sure that at most `M` student can use the washing machine at a time.