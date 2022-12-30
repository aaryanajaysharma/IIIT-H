/**
 * This function implements the ls command by listing all items in a directory
 * USAGE: 
 * ls
 * ls -la
 * ls -al
 * ls -a
 * ls -l
 * ls dir
 * TODO: total block size
 * colorise output: 
 * green for executables
 * white for files
 * blue for directories
 */

#include "feline.h"

int debug_exec_ls = 0;

void exec_ls(char *arg, char **args)
{
    int l = 0, a = 0;
    char *current_dir = NULL;
    struct dirent **namelist;

    // get all the parameters
    for (int i = 1; !is_empty_string(args[i]); ++i)
    {
        if (l == 0 && a == 0 && (strcmp(args[i], "-la") == 0 || strcmp(args[i], "-al") == 0))
            l = a = 1;
        else if (l == 0 && strcmp(args[i], "-l") == 0)
            l = 1;
        else if (a == 0 && strcmp(args[i], "-a") == 0)
            a = 1;
        else if (is_empty_string(current_dir) && strcmp(args[i], "&") != 0)
            current_dir = args[i];
        else if (strcmp(args[i], "&") != 0)
        {
            print_error("Invalid usage: Invalid number/type of arguments");
            return;
        }
    }
    if (is_empty_string(current_dir)) // if no directory is given
        current_dir = ".";
    else if (strcmp(current_dir, "~") == 0)
        current_dir = home;
    else if (current_dir[0] == '~') // if the relative directory to home is given, get the full path and then do
    {
        char *path = memalloc_string(MAX_CURRENT_DIR);
        sprintf(path, "%s/%s", home, current_dir + 2);
        if (debug_exec_ls)
            printn_debug(path);
        strcpy(current_dir, path);
    }
    int n = scandir(current_dir, &namelist, NULL, alphasort);
    char *buffer = memalloc_string(MAX_BUFFER_LENGTH);
    if (n < 0)
        perror("scandir");
    else
    {
        if (l == 1)
        {
            // TODO: print total directory size
        }
        while (n--)
        {
            if ((a == 1) || (namelist[n]->d_name[0] != '.' && a == 0))
            {
                if (l == 0){
                    // color the output
                    struct stat st;
                    sprintf(buffer, "%s/%s", current_dir, namelist[n]->d_name);
                    stat(buffer, &st);
                    if (S_ISDIR(st.st_mode))
                        print_blue(namelist[n]->d_name);
                    else if (st.st_mode & S_IXUSR)
                        print_green(namelist[n]->d_name);
                    else
                        printf("%s\n", namelist[n]->d_name);
                }
                else
                {
                    char *file_path = memalloc_string(MAX_CURRENT_DIR);
                    sprintf(file_path, "%s/%s", current_dir, namelist[n]->d_name);
                    if (debug_exec_ls)
                        printn_debug(file_path);
                    display_line_ls(file_path, namelist[n]->d_name);
                }
            }
            free(namelist[n]);
        }
        free(namelist);
    }
    free(buffer);
    fflush(stdout);
}
