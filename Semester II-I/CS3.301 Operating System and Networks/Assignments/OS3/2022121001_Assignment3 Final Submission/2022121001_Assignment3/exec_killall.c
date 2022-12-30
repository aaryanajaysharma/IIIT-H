/*
 *
 * This function kills all the running background processes at once
 */

#include "feline.h"

void exec_killall(char *arg, char **args)
{
    if (!is_empty_string(args[1]))
    {
        print_error("Invalid usage for overkill: too many arguments!!");
        return;
    }
    for (int i = 0; i < jobs_size; i++)
    {
        if (all_jobs[i].pid > 0)
        {
            kill(all_jobs[i].pid, 9);
            all_jobs[i].pid = -1;
        }
    }
}
