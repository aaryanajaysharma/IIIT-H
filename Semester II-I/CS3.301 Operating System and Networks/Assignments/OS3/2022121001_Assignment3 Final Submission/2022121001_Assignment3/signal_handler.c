/**
 * This function handles the two signals CTRL-C and CTRL-Z
 */

#include "feline.h"

int debug_signal_handler = 0;

void sigtstpHandler(int sig_num) // blocks the current running foreground process on pressing CTRL-Z
{
    ctrlz = 1;
    if (cur_fg.pid != -1 && !is_already_displayed_strz)
    {
        char *buffer = memalloc_string(MAX_LINE_LENGTH * 4);
        sprintf(buffer, "Process %s with id %d has been stopped", cur_fg.name, cur_fg.pid);
        print_n(buffer);
        free(buffer);
        all_jobs[jobs_size] = cur_fg;
        // all_jobs[jobs_size].type = STOPPED;
        jobs_size++;
        is_already_displayed_strz = 1;
    }
    cur_fg.pid = -1;
    signal(SIGTSTP, sigtstpHandler);
}

void sigintHandler(int sig_num) // exit the current running foreground process on pressing CTRL-C
{
    ctrlc = 1;
    if (cur_fg.pid != -1) // if in some other process (condition can be replaced by (getpid() != shellPID) ), give it a control c
    {
        cur_fg.pid = -1;
        return;
    }
    if (debug_signal_handler)
        printn_debug("To exit shell, please type exit");
    signal(SIGINT, sigintHandler);
    fflush(stdout);
}
