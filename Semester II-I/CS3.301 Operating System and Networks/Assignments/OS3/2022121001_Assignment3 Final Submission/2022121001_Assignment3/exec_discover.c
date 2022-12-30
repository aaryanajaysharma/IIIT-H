/*
discover() emulates the basics of the find command.
The command should search for files in a directory hierarchy recursively.
*/

#include "feline.h"

int debug_discover = 0;

void invalid_usage_discover(char *s)
{
    print_error(s);
    print_error("Usage: discover -d dir -n name -m min -M max -t type");
    exit(0);
}

char* itoa(int n)
{
    char *buffer = memalloc_string(10);
    sprintf(buffer, "%d", n);
    return buffer;
}

void discover_file(char *dir, char *name, int min, int max, char *type)
{
    DIR *d = opendir(dir);
    if (d == NULL)
        return;
    struct dirent *entry;
    while ((entry = readdir(d)) != NULL)
    {
        if (entry->d_type == DT_DIR)
        {
            if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
                continue;
            char *path = memalloc_string(strlen(dir) + strlen(entry->d_name) + 2);
            sprintf(path, "%s/%s", dir, entry->d_name);
            discover_file(path, name, min, max, type);
            free(path);
        }
        else
        {
            if (strcmp(entry->d_name, name) == 0)
            {
                char *path = memalloc_string(strlen(dir) + strlen(entry->d_name) + 2);
                sprintf(path, "%s/%s", dir, entry->d_name);
                struct stat st;
                stat(path, &st);
                if (st.st_size >= min && st.st_size <= max)
                {
                    if (strcmp(type, "f") == 0 && entry->d_type == DT_REG)
                        print_n(path);
                    else if (strcmp(type, "d") == 0 && entry->d_type == DT_DIR)
                        print_n(path);
                    else if (strcmp(type, "l") == 0 && entry->d_type == DT_LNK)
                        print_n(path);
                }
                free(path);
            }
        }
    }
    closedir(d);
}

void discover_dir(char *dir, char *name, int min, int max, char *type)
{
    DIR *d = opendir(dir);
    if (d == NULL)
        return;
    struct dirent *entry;
    while ((entry = readdir(d)) != NULL)
    {
        if (entry->d_type == DT_DIR)
        {
            if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
                continue;
            char *path = memalloc_string(strlen(dir) + strlen(entry->d_name) + 2);
            sprintf(path, "%s/%s", dir, entry->d_name);
            discover_dir(path, name, min, max, type);
            free(path);
        }
        else
        {
            if (strcmp(entry->d_name, name) == 0)
            {
                char *path = memalloc_string(strlen(dir) + strlen(entry->d_name) + 2);
                sprintf(path, "%s/%s", dir, entry->d_name);
                struct stat st;
                stat(path, &st);
                if (st.st_size >= min && st.st_size <= max)
                {
                    if (strcmp(type, "f") == 0 && entry->d_type == DT_REG)
                        print_n(dir);
                    else if (strcmp(type, "d") == 0 && entry->d_type == DT_DIR)
                        print_n(dir);
                    else if (strcmp(type, "l") == 0 && entry->d_type == DT_LNK)
                        print_n(dir);
                }
                free(path);
            }
        }
    }
    closedir(d);
}

void exec_discover(char *arg, char **args)
{
    int is_flags_read[5] = {0, 0, 0, 0, 0};
    char *dir = memalloc_string(MAX_LINE_LENGTH);
    char *name = memalloc_string(MAX_LINE_LENGTH);
    char *type = memalloc_string(MAX_LINE_LENGTH);
    int min = 0, max = 0;
    for (int i = 1; !is_empty_string(args[i]); i++)
    {
        if (debug_discover)
            printn_debug(args[i]);
        if (strcmp(args[i], "-d") == 0 && is_flags_read[0] == 0)
        {
            i++;
            if (is_empty_string(args[i]))
                invalid_usage_discover("Invalid usage: No directory provided");
            strcpy(dir, args[i]);
            is_flags_read[0] = 1;
        }
        else if (strcmp(args[i], "-n") == 0 && is_flags_read[1] == 0)
        {
            i++;
            if (is_empty_string(args[i]))
                invalid_usage_discover("Invalid usage: No name provided");
            strcpy(name, args[i]);
            is_flags_read[1] = 1;
        }
        else if (strcmp(args[i], "-m") == 0 && is_flags_read[2] == 0)
        {
            i++;
            if (is_empty_string(args[i]))
                invalid_usage_discover("Invalid usage: No min provided");
            min = atoi(args[i]);
            if (!min)
                invalid_usage_discover("Invalid usage: Invalid min");
            is_flags_read[2] = 1;
        }
        else if (strcmp(args[i], "-M") == 0 && is_flags_read[3] == 0)
        {
            i++;
            if (is_empty_string(args[i]))
                invalid_usage_discover("Invalid usage: No max provided");
            max = atoi(args[i]);
            if (!max)
                invalid_usage_discover("Invalid usage: Invalid max");
            is_flags_read[3] = 1;
        }
        else if (strcmp(args[i], "-t") == 0 && is_flags_read[4] == 0)
        {
            i++;
            if (is_empty_string(args[i]))
                invalid_usage_discover("Invalid usage: No type provided");
            strcpy(type, args[i]);

            if (strcmp(type, "f") != 0 && strcmp(type, "d") != 0)
                invalid_usage_discover("Invalid usage: Invalid type");
            is_flags_read[4] = 1;
        }
        else
            invalid_usage_discover("Invalid usage: Invalid flag");
    }
    if (is_flags_read[0] == 0 || is_flags_read[1] == 0 || is_flags_read[2] == 0 || is_flags_read[3] == 0 || is_flags_read[4] == 0)
        invalid_usage_discover("Invalid usage: Missing flag");
    if (debug_discover)
    {
        printn_debug(dir);
        printn_debug(name);
        printn_debug(type);
        printn_debug(itoa(min));
        printn_debug(itoa(max));
    }
    if (strcmp(type, "f") == 0)
        discover_file(dir, name, min, max, type);
    else
        discover_dir(dir, name, min, max, type);
}

