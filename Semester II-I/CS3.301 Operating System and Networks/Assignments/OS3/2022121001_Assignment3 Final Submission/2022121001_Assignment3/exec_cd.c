/**
 * This function implements the cd command by changing the directory to the path if mentioned or to the home directory (where the shell resides)
 */

#include "feline.h"

int debug_exec_cd = 0;

void exec_cd(char *arg, char **args)
{
    if (is_empty_string(args[1])) // no arguments
        chdir(home);
    else if (!is_empty_string(args[2])) // more than 1 argument
        print_error("cd: too many arguments!\nUsage: cd [path]");
    else if (strcmp(args[1], "~") == 0)
        chdir(home);
    else if (strcmp(args[1], ".") == 0)
        return;
    else if (args[1][0] == '~') // if relative to home address is given
    {
        char *path = memalloc_string(MAX_CURRENT_DIR * 4);
        sprintf(path, "%s/%s", home, args[1] + 2);
        if (debug_exec_cd)
            printn_debug(path);
        if (chdir(path) < 0)
            perror("Path error");
        free(path);
    }
    else if (chdir(args[1]) < 0)
        perror("Path error");
}