/**
 * This function brings a background/stopped process to the foreground
 **/

#include "feline.h"

int debug_exec_fg = 0;

void exec_fg(char *str, char **args)
{
    if (is_empty_string(args[1]))
    {
        print_error("Invalid usage: job number not found! \nUsage: fg jobno");
        return;
    }
    if (!is_empty_string(args[2]))
    {
        print_error("Invalid usage: Too many arguments! \nUsage: fg jobno");
        return;
    }
    if (debug_exec_fg)
        printn_debug(args[1]);
    int job_no;
    job_no = atoi(args[1]);
    if (job_no <= 0)
    {
        print_error("Invalid usage: Invalid job number! \nUsage: fg jobno");
        return;
    }
    int c = 0, st;
    char s;
    for (int i = 0; i < jobs_size; i++)
    {
        if (all_jobs[i].pid > 0)
        {
            c++;
            if (c == job_no)
            {
                if (debug_exec_fg)
                {
                    s = getchar();
                    printn_debug("PROCESS FOUND");
                }
                if (all_jobs[i].pid <= 0)
                {
                    print_error("Error: Invalid pid");
                    return;
                }
                kill(all_jobs[i].pid, SIGCONT); //SIGCONT continues in background a process previously stopped by SIGSTOP or SIGTSTP.
                if (debug_exec_fg)
                {
                    s = getchar();
                    printn_debug("KILLED THE PROCESS");
                    char *buffer = memalloc_string(MAX_LINE_LENGTH);
                    sprintf(buffer, "JOBNO: %d  PID: %d", c, all_jobs[i].pid);
                    print(buffer);
                    free(buffer);
                }

                //if it is not a background process, wait, till it gets over
                cur_fg = all_jobs[i];
                int sct;
                all_jobs[i].pid = -1;
                while (waitpid(cur_fg.pid, &sct, WNOHANG) != cur_fg.pid)
                {
                    if (debug_exec_fg)
                        printn_debug("WAITING ");
                    if (ctrlc)
                    {
                        if (debug_exec_fg)
                            printn_debug("CTRL C encountered in the fg function!");
                        ctrlc = 0;
                        signal(SIGINT, sigintHandler);
                        if (cur_fg.pid > 0)
                            kill(cur_fg.pid, SIGINT);
                        break;
                    }
                    if (ctrlz)
                    {
                        if (debug_exec_fg)
                            printn_debug("CTRL Z encountered in the fg function!");
                        ctrlz = 0;
                        signal(SIGTSTP, sigtstpHandler);
                        char buffer[4096];
                        if (is_already_displayed_strz == 0)
                        {
                            if (cur_fg.pid > 0)
                                kill(cur_fg.pid, SIGSTOP);
                            sprintf(buffer, "Process %s with id %d has been stopped\n", cur_fg.name, cur_fg.pid);
                            if (debug_exec_fg)
                                printn_debug("printed by the fg function!");
                            print_n(buffer);
                            all_jobs[jobs_size] = cur_fg;
                            cur_fg.pid = -1;
                            is_already_displayed_strz = 1;
                        }
                        break;
                    }
                }
                if (debug_exec_fg)
                {
                    s = getchar();
                    printn_debug("WAITING OVER");
                }
                all_jobs[i].pid = -1;
                return;
            }
        }
    }
    print_error("Error: Job number does not exist");
}