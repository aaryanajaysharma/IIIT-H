/**
 * This code executes all builtin commands that do not produce an output that can be sent anywhere or cannot be done in a child process
 * It returns 1 if the command is executed. 
 * It returns 0 if the command is not executed
 */

#include "feline.h"

int execute_builtin_no_output(char **args)
{
    if (strcmp(args[0], "exit") == 0)
        exec_exit(args[0], args);
    else if (strcmp(args[0], "quit") == 0)
        exec_exit(args[0], args);
    else if (strcmp(args[0], "cd") == 0)
        exec_cd(args[0], args);
    else if (strcmp(args[0], "overkill") == 0)
        exec_killall(args[0], args);
    else if (strcmp(args[0], "clearhistory") == 0)
        exec_clearhistory(args[0], args);
    else
        return 0;
    return 1;
}
