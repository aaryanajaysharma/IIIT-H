```
xv6 is a re-implementation of Dennis Ritchie's and Ken Thompson's Unix
Version 6 (v6).  xv6 loosely follows the structure and style of v6,
but is implemented for a modern RISC-V multiprocessor using ANSI C.

ACKNOWLEDGMENTS

xv6 is inspired by John Lions's Commentary on UNIX 6th Edition (Peer
to Peer Communications; ISBN: 1-57398-013-7; 1st edition (June 14,
2000)). See also https://pdos.csail.mit.edu/6.828/, which
provides pointers to on-line resources for v6.

The following people have made contributions: Russ Cox (context switching,
locking), Cliff Frey (MP), Xiao Yu (MP), Nickolai Zeldovich, and Austin
Clements.

We are also grateful for the bug reports and patches contributed by
Takahiro Aoyagi, Silas Boyd-Wickizer, Anton Burtsev, Ian Chen, Dan
Cross, Cody Cutler, Mike CAT, Tej Chajed, Asami Doi, eyalz800, Nelson
Elhage, Saar Ettinger, Alice Ferrazzi, Nathaniel Filardo, flespark,
Peter Froehlich, Yakir Goaron,Shivam Handa, Matt Harvey, Bryan Henry,
jaichenhengjie, Jim Huang, Matúš Jókay, Alexander Kapshuk, Anders
Kaseorg, kehao95, Wolfgang Keller, Jungwoo Kim, Jonathan Kimmitt,
Eddie Kohler, Vadim Kolontsov , Austin Liew, l0stman, Pavan
Maddamsetti, Imbar Marinescu, Yandong Mao, , Matan Shabtay, Hitoshi
Mitake, Carmi Merimovich, Mark Morrissey, mtasm, Joel Nider,
OptimisticSide, Greg Price, Jude Rich, Ayan Shafqat, Eldar Sehayek,
Yongming Shen, Fumiya Shigemitsu, Cam Tenny, tyfkda, Warren Toomey,
Stephen Tu, Rafael Ubal, Amane Uehara, Pablo Ventura, Xi Wang, Keiichi
Watanabe, Nicolas Wolovick, wxdao, Grant Wu, Jindong Zhang, Icenowy
Zheng, ZhUyU1997, and Zou Chang Wei.

The code in the files that constitute xv6 is
Copyright 2006-2020 Frans Kaashoek, Robert Morris, and Russ Cox.

ERROR REPORTS

Please send errors and suggestions to Frans Kaashoek and Robert Morris
(kaashoek,rtm@mit.edu). The main purpose of xv6 is as a teaching
operating system for MIT's 6.S081, so we are more interested in
simplifications and clarifications than new features.

BUILDING AND RUNNING XV6

You will need a RISC-V "newlib" tool chain from
https://github.com/riscv/riscv-gnu-toolchain, and qemu compiled for
riscv64-softmmu. Once they are installed, and in your shell
search path, you can run "make qemu".
```

# Report

### Team
* Aaryan Ajay Sharma (2022121001)
* Kritika Gautam (2021101125)

This is the fourth assignment for the course **Operating Systems and Networks** of Monsoon 2022.

Xv6 is a simplified operating system developed at MIT. Its main purpose is to explain the main concepts of the operating system by studying an example Kernel. xv6 is a re-implementation of Dennis Ritchie's and Ken Thompson's Unix Version 6 (v6). xv6 loosely follows the structure and style of v6, but is implemented for a modern RISC-V multiprocessor using ANSI C.

As part of the assignment, we have fulfilled the following specifications:

# Specification 1 (System Call Tracing)

To add a new system call `trace` which is called using the user program `strace`.

SYNTAX: `strace mask command [args]`

    - `mask`: a bit mask of the system calls to trace.
    - `command`: the command to execute.
    - `args`: the arguments to the command.

1. Added `$U/_strace` to the `UPROGS` in the Makefile.

2. Added a variable `mask` in `kernel/proc.h` and initialized it in the `fork()` function in `kernel/proc.c` to make a copy of the trace mask from the parent to the child process.

    ```cpp
    np->mask = p->mask;
    ```

3. Implemented a `sys_trace()` function in `kernel/sysproc.c`.
   This function implements the new system call to assign the value for a new variable `mask`.

   ```cpp
    uint64
    sys_trace()
    {
        int mask;

        if(argint(0, &mask) < 0)
        return -1;

        myproc()->mask = mask;
        return 0;
    }
    ```

4. Modified `syscall()` function in `kernel/syscall().c` to print the trace output and `syscall_names` and `syscall_num` arrays to help with this.

    ```cpp
    void
    syscall(void)
    {
    int num;
    struct proc *p = myproc();
    num = p->trapframe->a7;

    int length = syscalls_num[num];
    int a[length];

    for (int i = 0; i < length; i++)
        a[i] = argraw(i);


    if(num > 0 && num < NELEM(syscalls) && syscalls[num]) {
        p->trapframe->a0 = syscalls[num]();
        if(p->mask & 1 << num) {
        printf("%d: syscall %s (", p->pid, syscall_names[num]);
        for (int i = 0; i < length; i++)
            printf("%d ", a[i]);
        printf("\b) -> %d\n", p->trapframe->a0);
        }
    } else {
        printf("%d %s: unknown sys call %d\n",
                p->pid, p->name, num);
        p->trapframe->a0 = -1;
    }
    }
    ```

5. Created a user program in `user/strace.c` to generate the user-space stubs for the system call.

    ```cpp
    int main(int argc, char *argv[]) {
        char *nargv[MAXARG];

        if(argc < 3 || (argv[1][0] < '0' || argv[1][0] > '9')){
            fprintf(2, "Usage: %s mask command\n", argv[0]);
            exit(1);
        }

        if (trace(atoi(argv[1])) < 0) {
            fprintf(2, "%s: trace failed\n", argv[0]);
            exit(1);
        }

        for(int i = 2; i < argc && i < MAXARG; i++){
            nargv[i-2] = argv[i];
        }

        exec(nargv[0], nargv);

        exit(0);
    }
    ```

6. Added a new stub to `user/usys.pl`, which makes the `Makefile` invoke the script `user/usys.pl` and produce `user/usys.S`, and a syscall number to `kernel/syscall.h`.

7. Output is shown on the console.

# Specification 2 (Scheduling Mechanisms)

## First Come First Serve (FCFS)

First Come First Serve (FCFS) is a scheduling algorithm that is used to assign a process to a CPU. The process that is assigned to the CPU is the one that arrives first.

1. Revamped the Makefile to support `SCHEDULER` macro for the compilation of the specified scheduling algorithm. Here

    ```makefile
    ifndef SCHEDULER
        SCHEDULER:=RR
    endif
    ```

    ```makefile
    CFLAGS+=-D$(SCHEDULER)
    ```

2. Added a variable `createTime` to `struct proc` in `kernel/proc.h`.

3. Initialised `createTime` to 0 in `allocproc()` function in `kernel/proc.c`.

4. Implemented scheduling functionality in `scheduler()` function in `kernel/proc.c`, where the process with the least `createTime` is selected from all the available processes.

    ```cpp
    #ifdef FCFS

    struct proc* firstProcess = 0;

    for (p = proc; p < &proc[NPROC]; p++)
    {
    acquire(&p->lock);
    if (p->state == RUNNABLE)
    {
        if (!firstProcess || p->createTime < firstProcess->createTime)
        {
            if (firstProcess)
                release(&firstProcess->lock);

            firstProcess = p;
            continue;
        }
    }
    release(&p->lock);
    }

    if (firstProcess)
    {
    firstProcess->state = RUNNING;

    c->proc = firstProcess;
    swtch(&c->context, &firstProcess->context);

    c->proc = 0;
    release(&firstProcess->lock);
    }
    ```

5. `yield()` in `kernel/trap.c` has been disabled to prevent the process from restarting after the clock interrupts in FCFS. The same has been done for PBS as well. Now, `yield()` only gets invoked when it's MLFQ and RR.

## Priority Based Scheduling (PBS)

Priority Based Scheduling (PBS) is a scheduling algorithm that is used to assign a process to a CPU. The process that is assigned to the CPU is the one with the highest priority.

1. Added variables `staticPriority`, `runTime`, `startTime`, `numScheduled`, and `sleepTime` to `struct proc` in `kernel/proc.h`.

    ```cpp
    uint creation_time;   // Time of creation
    uint startTime;    // Time of start
    uint exitTime;     // Time of exit
    uint runTime;      // Time spent running
    uint waitTime;     // Time spent waiting
    uint sleepTime;    // Time spent sleeping
    uint totalRunTime; // Total time spent running
    uint num_runs;     // Number of runs
    uint priority;     // Process priority
    ```

2. Initialised the above variables with default values in `allocproc()` function in `kernel/proc.c`.

    ```cpp
    p->pid = allocpid();
    p->state = USED;
    p->createTime = ticks;
    p->runTime = 0;
    p->sleepTime = 0;
    p->totalRunTime = 0;
    p->num_runs = 0;
    p->priority = 60;
    ```

3. Added the scheduling functionality for PBS.

    ```cpp
    nice = ((10 * p->sleepTime) / (p->sleepTime + p->runTime));
    ```

    ```cpp
    int t = (p->priority - nice + 5) < 100 ? (p->priority - nice + 5) : 100; // calculate priority
    int process_dp = 0 > t ? 0 : t;
    ```

    ```cpp
    #ifdef PBS
        for (p = proc; p < &proc[NPROC]; p++) {
            acquire(&p->lock); // lock the chosen process

            if (p->state == RUNNABLE)
                if (
                    NodeProc == 0 ||
                    dynamic_priority > process_dp ||
                    (dynamic_priority == process_dp && NodeProc->num_runs > p->num_runs) ||
                    (dynamic_priority == process_dp &&
                        NodeProc->num_runs == p->num_runs &&
                        NodeProc->createTime > p->createTime)) {

                    if (NodeProc)
                        release(&NodeProc->lock); // release the lock of the previous process

                    dynamic_priority = process_dp; // set the dynamic priority
                    NodeProc = p;                  // set the process with the highest priority
                    continue;
                }
            release(&p->lock); // release the lock
        }
        if (NodeProc) {                             // if there is a process with the highest priority
            NodeProc->state = RUNNING;              // set the process with the highest priority to running
            NodeProc->startTime = ticks;            // set the start time of the process with the highest priority
            NodeProc->num_runs++;                   // increase the number of runs of the process with the highest priority
            NodeProc->runTime = 0;                  // set the run time of the process with the highest priority to 0
            NodeProc->sleepTime = 0;                // set the sleep time of the process with the highest priority to 0
            c->proc = NodeProc;                     // set the current process to the process with the highest priority
            swtch(&c->context, &NodeProc->context); // switch to the process with the highest priority
            // Process is done running for now.
            // It should have changed its p->state before coming back.
            c->proc = 0;              // no longer running
            release(&NodeProc->lock); // release the lock of the process with the highest priority
        }
    #endif
    ```

4. Added a new function `set_priority()` in `kernel/proc.c`.

    ```cpp
    int set_priority(int new_priority, int pid) {
        int t = -1;
        struct proc *p;
        for (p = proc; p < &proc[NPROC]; p++) {
            acquire(&p->lock); // lock the process
            if (p->pid == pid) { // if the process is found
                t = p->priority; // save the old priority
                p->priority = new_priority; // set the new priority
                release(&p->lock); // unlock the process
                if (t > new_priority) // if the new priority is lower
                    yield(); // yield the CPU
                break;
            }
            release(&p->lock); // unlock the process
        }
        return t;
    }
    ```

5. Created a new user program `user/setpriority.c`.

    ```cpp
    int main(int argc, char *argv[])
    {
        #ifdef PBS
        if(argc < 3 || (argv[1][0] < '0' || argv[1][0] > '9')){
            fprintf(2, "Usage: %s command\n", argv[0]);
            exit(1);
        }

        int t = set_priority(atoi(argv[1]), atoi(argv[2]));

        if (t < 0) {
            fprintf(2, "%s: set_priority failed\n", argv[0]);
            exit(1);
        }
        else if (t == 101) {
            fprintf(2, "%s: pid %s not found\n", argv[2]);
            exit(1);
        }
        #endif

        exit(0);
    }
    ```

6. Added `sys_set_priority()` system call in `kernel/sysproc.c`.

    ```cpp
    uint64
    sys_set_priority()
    {
    int priority, pid;
    int oldpriority = 101;
    if(argint(0, &priority) < 0 || argint(1, &pid) < 0)
        return -1;

    for(struct proc *p = proc; p < &proc[NPROC]; p++)
    {
        acquire(&p->lock);

        if(p->pid == pid && priority >= 0 && priority <= 100)
        {
        p->sleepTime = 0;
        p->runTime = 0;
        oldpriority = p->priority;
        p->priority = priority;
        }

        release(&p->lock);
    }
    if(oldpriority > priority)
    yield();
    return oldpriority;
    }
    ```

## Lottery Based Scheduler
* A process is assigned some tickets when it is created. The scheduler generates a random number and based on that decides which process is to be scheduled.
* Most of the scheduler logic code resides in proc.c.

* Flow:
    * The scheduler finds out the total tickets of the RUNNABLE processes. (The different states of the process can be found in proc.h.)

    * If non-zero RUNNABLE processes are found, then scheduler generates a random number (rand.c). The random number generator used is linear feedback shift register random number generator. Information about this can be found [here](https://en.wikipedia.org/wiki/Linear-feedback_shift_register)).
    * The scheduler then finds the process to be scheduled by adding the tickets of the RUNNABLE processes and then selecting that process at which the total tickets count becomes just greater than the random number.

## Multilevel Feedback Queue (MLFQ)

Multilevel Feedback Queue (MLFQ) is a scheduling algorithm that is used to assign a process to a CPU. The process that is assigned to the CPU is the one with the highest priority. The priority of the process is determined by the number of times it has been assigned to the CPU. The priority of the process is increased by one when it is assigned to the CPU (CPU Bursts). The priority of the process is decreased by one when it is finished executing (IO Bursts).

This scheduling algorithm hasn't been implemented.

# Specification 3 (Copy-on-Write)

## Basic Idea
The idea behind Copy On Write (COW) is that when a new process is created as a child of another the two processes will point at the same pages in physical memory and the pages of the parent process will not be coppied until one of the processes needs to write something.

## Visual Representation
![COW](https://raw.githubusercontent.com/ThodBaniokos/Copy-On-Write-XV6/main/img/Copy%20On%20Write%20Example%201.png)

# Benchmark Testing

A benchmarking script was created (`user/schedulertest.c`). On executing the script on the 3 scheduling algorithms, the following were observed:
```
LBS - Average rtime 17,  wtime 150
FCFS - Average rtime 78,  wtime 81
PBS - Average rtime 38,  wtime 115
```
