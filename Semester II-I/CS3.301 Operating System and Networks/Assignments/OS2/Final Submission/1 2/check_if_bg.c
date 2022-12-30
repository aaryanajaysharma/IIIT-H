/**
 * This function checks whether the given parsed string (separated by spaces) can qualify as a background process or not, i.e. it should have an & as its last item. 
 * It also modifies the string and removes the trailing \0 and & character
 * If & appears in the middle of the argument, it would be ignored
 */

#include "feline.h"

int debug_check_if_bg = 0;

int check_if_bg(char **args)
{
    int argc = 0;
    for (; !is_empty_string(args[argc]); argc++)
        if (debug_check_if_bg)
            printn_debug(args[argc]);
    args[argc] = NULL; //nullify the last argument
    if (strcmp(args[argc - 1], "&") == 0)
    {
        args[argc - 1] = NULL; //nullify the & argument too
        return 1;
    }
    return 0;
}