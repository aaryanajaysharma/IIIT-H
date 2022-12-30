/*
* This function displays the last 20 (max) or argument number of previous commands entered
*/

#include "feline.h"

int arr_imp = 0;

void tail(FILE *in, int n)
{
    n++;
    int count_of_lines = 0;
    size_t sz = 0;
    char *line = memalloc_string(MAX_LINE_LENGTH);
    if (fseek(in, 0, SEEK_END))
    {
        perror("fseek() failed");
        return;
    }
    unsigned long long pos = ftell(in); //total number of characters; i.e. the location of the last character
    while (pos > 0)
    {
        pos--;
        if (fseek(in, pos, SEEK_SET) >= 0)
        {
            if (fgetc(in) == '\n')
            {
                count_of_lines++;
                if (count_of_lines >= n)
                    break;
            }
        }
    }
    while (getline(&line, &sz, in) != -1)
        print(line);
}

void exec_history(char *arg, char **args)
{
    int lines_to_display = MAX_HISTORY_DISPLAY;
    if (!is_empty_string(args[1]))
    {
        if (!is_empty_string(args[2]))
        {
            print_n("Invalid usage: No number of lines mentioned \nUsage: history [n]");
            return;
        }
        int arg1 = atoi(args[1]);
        if (arg1 == 0)
        {
            print_n("Invalid usage: Invalid number of lines\nUsage: history [n]");
            return;
        }
        lines_to_display = arg1;
    }
    lines_to_display = (MAX_HISTORY_DISPLAY > lines_to_display) ? lines_to_display : MAX_HISTORY_DISPLAY;
    if (arr_imp)
    {
        for (int i = history_lines - lines_to_display; i < history_lines; i++)
            print_n(history[i]);
    }
    FILE *hist = fopen(history_path, "r");
    if (hist == NULL)
    {
        print_n("No commands read in history.txt");
        return;
    }
    tail(hist, lines_to_display);
    fclose(hist);
}
