/**
 * This function displays the feline shell prompt using colors
 * It also takes care when the current working directory is inside the shell home directory by displaying it as ~/...
 */

#include "feline.h"

int debug_display_shell_prompt = 0;

char *display_shell_prompt()
{
    //Getting the username and system name
    char *username = memalloc_string(MAX_USERNAME_SIZE);
    char *system_name = memalloc_string(MAX_SYSTEM_NAME);
    char *current_directory = memalloc_string(MAX_CURRENT_DIR);

    //initialisation
    gethostname(system_name, MAX_SYSTEM_NAME);
    getlogin_r(username, MAX_USERNAME_SIZE);
    getcwd(current_directory, MAX_CURRENT_DIR); // this would give the absolute working directory
    if (debug_display_shell_prompt)
    {
        char *buffer = memalloc_string(MAX_BUFFER_LENGTH);
        sprintf(buffer, "Absolute working directory: %s", current_directory);
        printn_debug(buffer);
        free(buffer);
    }

    // now check whether it is reducible by checking whether it is in home directory
    if (strncmp(current_directory, home, strlen(home)) == 0)
    {
        char *s = current_directory;
        *s++ = '~';
        for (int j = strlen(home); current_directory[j] != '\0'; j++)
            *s++ = current_directory[j];
        *s = '\0';
    }
    if (debug_display_shell_prompt)
    {
        char *buffer = memalloc_string(MAX_BUFFER_LENGTH);
        sprintf(buffer, "Relative working directory: %s", current_directory);
        printn_debug(buffer);
        free(buffer);
    }

    // now write the prompt into the buffer
    char *buffer = memalloc_string(MAX_CURRENT_DIR + MAX_SYSTEM_NAME + MAX_USERNAME_SIZE + 38);
    sprintf(buffer, "\033[0m<\033[0;32m%s@%s:\033[0m\033[0;34m%s\033[0m> ", username, system_name, current_directory);
    if (debug_display_shell_prompt)
        print_debug(buffer);
    free(username);
    free(system_name);
    free(current_directory);
    return buffer;
}
