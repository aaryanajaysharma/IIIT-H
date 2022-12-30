/**
 * This function handles the redirection symbol, that is, it sets the input and output files
 * */

#include "feline.h"

int debug_set_ip_op_redirection = 0;

void set_ip_op_redirection(char **args)
{
    for (int i = 0; !is_empty_string(args[i]); i++)
    {
        if (strcmp(args[i], "<") == 0) // Redirect for input
        {
            if (debug_set_ip_op_redirection)
                printn_debug("Redirect for input");
            int fd_input = open(args[i + 1], O_RDONLY, 0);
            if (fd_input < 0)
                file_error();
            dup2(fd_input, 0);
            close(fd_input);
            args[i] = NULL;
        }
        else if (!strcmp(args[i], ">")) // Redirect for output for writing
        {
            if (debug_set_ip_op_redirection)
                printn_debug("Redirect for output for writing");
            int fd_write = open(args[i + 1], O_WRONLY | O_TRUNC | O_CREAT, 0644);
            if (fd_write < 0)
                file_error();
            dup2(fd_write, 1);
            close(fd_write);
            args[i] = NULL;
        }
        else if (!strcmp(args[i], ">>")) // Redirect for output for appending
        {
            if (debug_set_ip_op_redirection)
                printn_debug("Redirect for output for appending");
            int fd_append = open(args[i + 1], O_APPEND | O_RDWR | O_CREAT, 0644);
            if (fd_append < 0)
                file_error();
            dup2(fd_append, 1);
            close(fd_append);
            args[i] = NULL;
        }
    }
}