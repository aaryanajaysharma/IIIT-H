/**
 * The main function that contains the driver loop
 */

#include "feline.h"

int readline_allowed = 1;
int history_array_imp = 0;

void initialize_all()
{
    shellPID = getpid();
    getcwd(home, MAX_CURRENT_DIR);
    initialize_history();
    add_prev_history();
    signal(SIGINT, sigintHandler);
    signal(SIGTSTP, sigtstpHandler);
    jobs_size = 0;
    cur_fg.pid = -1;
}

int main()
{
    display_feline();
    initialize_all();
    char *buffer, *prompt;
    char **temp = NULL;
    while (1)
    {
        ctrlc = 0;
        ctrlz = 0;
        is_already_displayed_strz = 0;
        if (jobs_size >= MAX_JOBS) // If the number of jobs exceeds the MAX_JOBS, then overkill
            exec_killall(buffer, temp);
        display_killed_children();
        prompt = display_shell_prompt();
        if (readline_allowed == 1)
        {
            buffer = readline(prompt);
            if (is_empty_string(buffer)) // Ctrl+D recieved exiting
                continue;
            add_history(buffer);
        }
        else
        {
            print(prompt);
            buffer = read_command();
        }
        interpret_command(buffer, 0);
        save_to_history(buffer);
        if (!history_array_imp)
            strcpy(history[history_lines++], buffer); //Updating the history array with input buffer
    }
    free(buffer);
}
