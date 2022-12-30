/**
 * This function parses the string based on a single separator (a function similar to strok command)
 * The ending of the char** is given by a '\0' character.
 * 
 * ASSUMPTIONS:
 * 1. No consecutive separators exist
 *    -- In case this happens the output for "I;am;a;a;;po" would be {"I","am","a","a","po"}
 * 2. All white spaces are spaces
 * 3. Here the redirection symbols and piping symbols are parsed as a separate token if the parameter redirection is set to 1
 *    -- output for "cat a.txt>l.txt" is parsed as {"cat","a.txt",">","l.txt"}"
 */

#include "feline.h"

int debug_string_splitter = 0;

int is_sep(char c, char sep) // Checks if the given character is a separator and returns 1
{
    return (c == sep);
}

char **string_splitter(char *buffer, char sep, int redirection) //splits the buffer based on the separator
{
    char **result = (char **)malloc(MAX_COMMANDS_PER_LINE * sizeof(char *));
    if (!result)
        memory_error();
    while (is_sep(buffer[0], sep))
        buffer++;
    if (debug_string_splitter)
    {
        print_debug("Buffer after removing all leading separators: ");
        printn_debug(buffer);
    }
    while (is_sep(buffer[strlen(buffer) - 1], sep))
        buffer[strlen(buffer) - 1] = '\0';
    if (debug_string_splitter)
    {
        print_debug("Buffer after removing all trailing separators: ");
        printn_debug(buffer);
    }
    if (strcmp(buffer, "") == 0)
    {
        if (debug_string_splitter)
            printn_debug("Buffer is empty! ");
        result[0] = (char *)memalloc_string(MAX_BUFFER_LENGTH * sizeof(char));
        result[0][0] = '\0';
        return result;
    }
    if (debug_string_splitter)
        printn_debug("Arguments are");
    int rowno = 0;
    for (int i = 0; i < strlen(buffer); i++)
    {
        if (buffer[i] == ' ')
            continue;
        result[rowno] = (char *)memalloc_string(MAX_BUFFER_LENGTH * sizeof(char));
        int j = 0;
        while (buffer[i] != '\0' && !is_sep(buffer[i], sep))
        {
                result[rowno][j++] = buffer[i++];
        }
        if (j != 0)
        {
            result[rowno][j] = '\0';
            if (debug_string_splitter)
            {
                char *s = memalloc_string(100);
                sprintf(s, "%d. %s", rowno, result[rowno]);
                printn_debug(s);
                free(s);
            }
            rowno++;
        }
    }
    result[rowno] = (char *)memalloc_string(MAX_BUFFER_LENGTH * sizeof(char));
    result[rowno][0] = '\0';
    return result;
}
