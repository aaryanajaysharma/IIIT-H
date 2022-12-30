/**
 * This function displays the name and pid of all children killed or stopped within the next execution of the command
 * Runs on pressing enter
 */

#include "feline.h"

int debug_display_killed_children = 0;

void print_process_details(struct ongoing_processes proc, int status)
{
    char *buffer = memalloc_string(MAX_LINE_LENGTH * 4);
    if (WIFEXITED(status))
        sprintf(buffer, "%s with pid %d exited\nnormally with status %d", proc.name, proc.pid, WEXITSTATUS(status));
    else
        sprintf(buffer, "%s with pid %d exited\nabnormally (terminated by a signal) with error status %d", proc.name, proc.pid, WEXITSTATUS(status));
    print_n(buffer);
    free(buffer);
}

void display_killed_children()
{
    int pid, status;
    while (1)
    {
        int pid = waitpid(-1, &status, WNOHANG | WUNTRACED); // WNOHANG is for killed children; WUNTRACED is for stopped children
        if (pid <= 0)
            break;
        if (WIFEXITED(status) || WIFSIGNALED(status))
            for (int i = 0; i < jobs_size; i++)
                if (all_jobs[i].pid == pid)
                {
                    print_process_details(all_jobs[i], status);
                    all_jobs[i].pid = -1;
                }
    }
}