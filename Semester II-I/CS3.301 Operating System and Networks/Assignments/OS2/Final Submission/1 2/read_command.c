/**
 * This function reads a line(ending with EOL or '\n') from the command prompt, and removes all leading and trailing spaces(' ' '\v' and '\t') and consecutive white spaces too
 * TODO: except inside the quotes
 */

#include "feline.h"

int iswhitespace(char ch)
{
    if (ch == ' ' || ch == '\v' || ch == '\t')
        return 1;
    else
        return 0;
}

int isendofline(char ch)
{
    if (ch == '\0' || ch == '\n')
        return 1;
    else
        return 0;
}

char *read_command()
{
    char *buffer = memalloc_string(MAX_LINE_LENGTH);
    char ch = ' ';
    int cur = 0;
    while (iswhitespace(ch) && !isendofline(ch))
        read(0, &ch, 1);
    if (isendofline(ch))
    {
        buffer[0] = '\0';
        return buffer;
    }
    buffer[cur++] = ch;
    while (!isendofline(ch))
    {
        read(0, &ch, 1);
        if (iswhitespace(ch) && !isendofline(ch))
        {
            buffer[cur++] = ch;
            while (iswhitespace(ch) && !isendofline(ch))
                read(0, &ch, 1);
        }
        buffer[cur++] = ch;
    }
    cur--;
    while (iswhitespace(buffer[cur]) || isendofline(buffer[cur]))
        cur--;
    buffer[cur + 1] = '\0';
    for (int i = 0; i <= cur; i++)
        if (iswhitespace(buffer[i]))
            buffer[i] = ' ';
    return buffer;
}
