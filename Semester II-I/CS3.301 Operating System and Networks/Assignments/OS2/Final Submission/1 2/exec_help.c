/**
 * This function displays the list of all builtin commands supported by the shell
 */

#include "feline.h"

void exec_help(char *arg, char **args)
{
    print_n("List of commands supported: ");
    print_n("exit");
    print_n("quit");
    print_n("echo");
    print_n("pwd");
    print_n("ls");
    print_n("history");
    print_n("clearhistory");
    print_n("cd");
}