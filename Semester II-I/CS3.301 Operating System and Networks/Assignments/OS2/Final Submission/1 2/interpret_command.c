/**
 * Considers a command stored in the buffer and breaks it down into individual commands and then into argumnets and executes them based on whether it is builtin or not
 * It takes in an extra command, forcebg
 * if forcebg==1 then no matter there is & or not it would be executed in the background
 */

#include "feline.h"

int debug_interpret_command = 0;

void interpret_command(char *cmd, int forcebg)
{
    char **cmds = string_splitter(cmd, ';', 0); // get each command separated by semicolons and no need to split based on redirections
    for (int i = 0; !is_empty_string(cmds[i]); i++)
    {
        ctrlc = 0;
        ctrlz = 0;
        is_already_displayed_strz = 0;
        char *btemp, **temp;
        if (jobs_size >= MAX_JOBS) // If the number of jobs exceeds the MAX_JOBS, then killall
            exec_killall(btemp, temp);
        if (debug_interpret_command)
            print_debug(cmds[i]);
        char **args = string_splitter(cmds[i], ' ', 1); // get each command separated by semicolons and  split based on redirections
        if (is_empty_string(args[0]))                       // that is, no command has been given
            continue;
        if (execute_builtin_no_output(args) == 1) // if it is a builtin command that has no output and hence need not be forked and messed up, execute
            continue;
        else
            isbg = check_if_bg(args);
        int pid = fork();
        if (pid == 0) // child process
        {
            if (isbg)
                setpgid(0, 0);
            if (execute_builtin_commands(args) == 0) // Check whether it is a builtin command and execute it
                if (execvp(args[0], args) < 0)       // If the command does not exist
                    perror("No command found");
            fflush(stdout);
            exit(0);
        }
        else
        {
            if (!isbg)
            {
                cur_fg.pid = pid; // change details of the foreground process
                strcpy(cur_fg.name, cmds[i]);
                // cur_fg.type = FOREGROUND;
                int status;
                waitpid(pid, &status, WUNTRACED); // wait, till it gets over
                cur_fg.pid = -1;                        //cur_fg.type = INVALID;
            }
            else
            {
                all_jobs[jobs_size].pid = pid; // add the background process to the list of processes
                strcpy(all_jobs[jobs_size].name, cmds[i]);
                // all_jobs[jobs_size].type = BACKGROUND;
                jobs_size++;
            }
        }
        free(args);
    }
    free(cmds);
}