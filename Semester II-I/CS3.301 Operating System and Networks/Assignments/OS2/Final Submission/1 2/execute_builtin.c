/*
 *
 * This function executes all builtin commands that has an output and can be performed in the background by calling those particular functions.
 * It returns 1 if the command given is a builtin and executes it. 
 * It returns 0 if the command given is not and doesn't execute it
 */

#include "feline.h"

int execute_builtin_commands(char **args)
{
    if (strcmp(args[0], "echo") == 0)
        exec_echo(args[0], args);
    else if (strcmp(args[0], "pwd") == 0)
        exec_pwd(args[0], args);
    else if (strcmp(args[0], "ls") == 0)
        exec_ls(args[0], args);
    else if (strcmp(args[0], "history") == 0)
        exec_history(args[0], args);
    else if (strcmp(args[0], "help") == 0)
        exec_help(args[0], args);
    else if (strcmp(args[0], "discover") == 0)
        exec_help(args[0], args);
    else
        return 0;
    fflush(stdout);
    return 1;
}
