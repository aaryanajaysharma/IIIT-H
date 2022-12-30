/**
 * This function handles everything if there is at least a pipe
 * if there is no pipe, it returns -1 
 * otherwise it does everything required and returns a 0
*/

#include "feline.h"

int debug_pipe_handler = 0;
int fildes[2];

int pipe_handler(char *cmd)
{
    char s;
    char **pipe_commands = string_splitter(cmd, '|', 0);
    int no_of_pipes = -1, in_fd = dup(0), out_fd = dup(1);
    while (!is_empty_string(pipe_commands[no_of_pipes + 1]))
    {
        if (debug_pipe_handler)
            printn_debug(pipe_commands[no_of_pipes + 1]);
        no_of_pipes++;
    }
    if (!no_of_pipes) //no pipes, everything failed
        return -1;
    for (int i = 0, pid, status; i <= no_of_pipes; ++i)
    {
        if (debug_pipe_handler)
        {
            s = getchar();
            printn_debug("NOW IN LOOP");
        }
        if (i != 0)
        {
            if (debug_pipe_handler)
            {
                s = getchar();
                printn_debug("i not 0 setting up input");
            }
            close(fildes[1]);
            in_fd = dup(0);
            if (dup2(fildes[0], 0) == -1)
                fprintf(stderr, "Error: dup2 failed\n");
            close(fildes[0]);
        }
        if (i != no_of_pipes)
        {
            if (debug_pipe_handler)
            {
                s = getchar();
                printn_debug("i not tot -1 setting up output");
            }
            pipe(fildes);
            if (debug_pipe_handler)
            {
                s = getchar();
                printn_debug("pipe setup done");
            }
            out_fd = dup(1);
            if (debug_pipe_handler)
            {
                s = getchar();
                printn_debug("output setup done");
            }
            if (dup2(fildes[1], 1) == -1)
                fprintf(stderr, "Error: dup2 failed\n");
        }
        if (debug_pipe_handler)
        {
            s = getchar();
            char *buffer = memalloc_string(MAX_BUFFER_LENGTH);
            sprintf(buffer, "%d %d ", out_fd, in_fd);
            printn_debug(buffer);
        }
        pid = fork();
        if (pid == 0) //child process
        {
            if (debug_pipe_handler)
            {
                s = getchar();
                print_debug("Execute : ");
                printn_debug(pipe_commands[i]);
            }
            interpret_command(pipe_commands[i], 0);
            exit(0);
        }
        else //parent process
        {
            waitpid(pid, &status, WUNTRACED);
            dup2(in_fd, 0);
            dup2(out_fd, 1);
        }
    }
    return 0;
}