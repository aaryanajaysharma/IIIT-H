/**
 * This function implements echo command, that is, prints all the arguments to this function to stdout.
 * TODO: QUOTATIONS :: However, it deals with only this case: echo something, i.e. it doesn't deal with quotations and prints them as though they are the part of the word
 */

#include "feline.h"

int debug_exec_echo=0;

void exec_echo(char *arg, char **args)
{
    for (int i = 1; !is_empty_string(args[i]); i++)
    {
        print(args[i]);
        print(" ");
    }
    print("\n");
}