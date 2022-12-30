/**
 * This function checks if the given command is valid or not 
 * Returns 0 if the command is invalid, i.e. contains some parse error regarding redirection symbols, i.e. it returns 0 if it contains |<> in a random manner (i.e. not in >>,>,<,|)
 * Also returns 0 if the command starts/ends with a redirection/piping sumbol
 * */

#include "feline.h"

int debug_isvalid_redirection = 0;

void parse_error(char *s) // prints the parse error location
{
    char *buffer = memalloc_string(MAX_BUFFER_LENGTH);
    sprintf(buffer, "Parse error: Error parsing near %s", s);
    print_error(buffer);
    free(buffer);
}

int is_redirection_or_piping(char *s) // returns 1 if it is a valid redirection or piping symbol
{
    if ((strcmp(s, ">>") == 0) || (strcmp(s, ">") == 0))
        return 1;
    else if (strcmp(s, "<") == 0)
        return 1;
    else if (strcmp(s, "|") == 0)
        return 1;
    return 0;
}

int contains_redirection_or_piping(char *s) // returns 1 if the string contains a redirection or piping symbol
{
    int check = 0;
    for (int i = 0; s[i] != '\0'; i++)
        if (is_redirection_or_piping_char(s[i]))
            return 1;
    if (check == 0)
        return 0;
}

int isvalid_redirection_or_piping(char *s) // returns 1 if it is a valid redirection word or a normal word not containing any redirections
{
    if (is_empty_string(s))
        return 1;
    if (contains_redirection_or_piping(s) == 0)
        return 1;
    return is_redirection_or_piping(s);
}

int isvalid_redirection(char **args) // returns 1 if the command provided has a redirection symbol and is valid
{
    int i = 0;
    if (debug_isvalid_redirection)
        printn_debug("CHECKING IF VALID");
    if (contains_redirection_or_piping(args[0]))
    {
        parse_error(args[0]);
        return 0;
    }
    if (debug_isvalid_redirection)
        printn_debug("DOES NOT CONTAIN");
    for (; !is_empty_string(args[i]); ++i)
    {
        if (debug_isvalid_redirection)
            printn_debug(args[i]);
        if (isvalid_redirection_or_piping(args[i]) == 0)
        {
            parse_error(args[i]);
            return 0;
        }
    }
    if (contains_redirection_or_piping(args[i - 1]))
    {
        parse_error(args[i - 1]);
        return 0;
    }
    return 1;
}

int is_redirection(char **args) // returns 1 if it is a valid redirection command
{
    if (debug_isvalid_redirection)
        printn_debug("CHECKING IF REDIRECTION");
    for (int i = 0; !is_empty_string(args[i]); i++)
    {
        if (debug_isvalid_redirection)
            printn_debug(args[i]);
        for (int j = 0; args[i][j] != '\0'; j++)
            if (args[i][j] == '<' || args[i][j] == '>')
                return 1;
    }
    return 0;
}
