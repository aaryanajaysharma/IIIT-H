/**
 * This file contains the display functions: 
 * - print: prints a given string to stdout without a trailing newline
 * - print_n: prints a given string to stdout with a trailing newline
 * - print_debug: prints a debugging statement without a \n at its end 
 * - printn_debug: prints a debugging statement with a \n at its end
 * - print_err: prints an error statement to stderr with a \n at its end
 * the following common basic error handling
 * - memory error
 * - file error
 * the utility shortcut functions
 * - is_empty_string: returns 1 if the string is NULL or has no character expect the '\0' character
 * -
 */

#include "feline.h"

// DISPLAY

void print(char *s)
{
    write(1, s, strlen(s));
}

void print_n(char *s)
{
    print(s);
    print("\n");
}

void print_debug(char *s)
{
    write(1, s, strlen(s));
    write(1, "\n", 2);
}

void printn_debug(char *s)
{
    write(1, s, strlen(s));
    write(1, "\n", 2);
}

void print_error(char *s)
{
    write(2, s, strlen(s));
    write(2, "\n", 2);
}

void print_blue(char *str)
{
    printf("\033[1;34m%s\033[0m\n", str);
}

void print_green(char *str)
{
    printf("\033[1;32m%s\033[0m\n", str);
}

void print_violet(char *str)
{
    printf("\033[1;35m%s\033[0m\n", str);
}

// ERROR

void memory_error()
{
    perror("Memory allocation error ");
    exit(1);
}

void file_error()
{
    perror("File opening error ");
    exit(1);
}

// OTHERS

int is_empty_string(char *str)
{
    if (str == NULL)
        return 1;
    if (str[0] == '\0')
        return 1;
    return 0;
}

char *memalloc_string(int length)
{
    char *s = (char *)malloc(length * sizeof(char));
    if (!s)
    {
        memory_error();
        exit(0);
    }
    return s;
}
