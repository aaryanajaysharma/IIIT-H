/**
 * This function exits out of all the processes and then exits the shell normally and successfully
 */

#include "feline.h"

void exec_exit(char *str, char **args)
{
    exec_killall(str, args);
    print_n("Exiting the shell now...");
    exit(EXIT_SUCCESS);
}