/**
 * This function clears the history file of the program. Strangely enough, it does not clear the add_history_line's history(i.e. the one we get on pressing the up arrow)
 */

#include "feline.h"

void exec_clearhistory(char *arg, char **args)
{
    if (!is_empty_string(args[1]))
    {
        print_error("Invalid usage: Too many arguments!");
        return;
    }
    remove(history_path);
    initialize_history();
}