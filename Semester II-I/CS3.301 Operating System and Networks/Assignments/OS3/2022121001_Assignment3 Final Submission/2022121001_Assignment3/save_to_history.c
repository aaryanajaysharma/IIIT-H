/**
 * This file contains two functions 
 * save_to_history: Saves the buffer in a file history.txt
 * initialize_history: initialises the history path
 * If the file does not exist, it is created and a new line is inserted
 */

#include "feline.h"

int debug_history = 0;

void initialize_history() // make a new file and put a \n in it
{
    strcpy(history_path, home);
    strcat(history_path, "/history.txt");
    struct stat buffer;
    if (stat(history_path, &buffer) != 0) //if the file does not exist
    {
        FILE *fout = fopen(history_path, "a"); // open the file in append mode
        if (!fout)
            file_error();
        fprintf(fout, "\n");
        fclose(fout);
    }
}

void save_to_history(char *buffer) // save the current command into the file
{
    // 
    if (is_empty_string(buffer))
        return;
    FILE *fout = fopen(history_path, "a");
    if (!fout)
        file_error();
    if (debug_history)
        printn_debug(buffer);
    fprintf(fout, "%s\n", buffer);
    fclose(fout);
}

void add_prev_history()
{
    FILE *in = fopen(history_path, "r");
    if (!in)
        file_error();
    size_t sz = 0;
    char *line = memalloc_string(MAX_LINE_LENGTH);
    while (getline(&line, &sz, in) != -1)
    {
        if (!is_empty_string(line))
        {
            while (*line == ' ' || *line == '\t' || *line == '\n')
                line++;
            while (line[strlen(line) - 1] == ' ' || line[strlen(line) - 1] == '\n' || line[strlen(line) - 1] == '\r' || line[strlen(line) - 1] == (char)10)
                line[strlen(line) - 1] = '\0';
            if (debug_history)
            {
                printn_debug(line);
                for (int i = 0; i <= strlen(line); i++)
                    printf("%d\n", line[i]);
            }
            add_history(line);
        }
    }
}