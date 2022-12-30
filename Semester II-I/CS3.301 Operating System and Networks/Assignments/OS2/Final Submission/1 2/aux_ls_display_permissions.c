/**
 * This auxillary function to ls which displays the file permissions corresponding to the mode given
 */

#include "feline.h"

void display_permissions_ls(int mode)
{
    char buffer[MAX_BUFFER_LENGTH];
    char *s = buffer;

    //for the file type
    if (S_ISREG(mode))
        *s++ = '-';
    else if (S_ISDIR(mode))
        *s++ = 'd';
    else if (S_ISCHR(mode))
        *s++ = 'c';
    else if (S_ISBLK(mode))
        *s++ = 'b';
    else if (S_ISFIFO(mode))
        *s++ = 'f';
    else if (S_ISLNK(mode))
        *s++ = 'l';
    else
        *s++ = 's';

    //for all the permissions
    *s++ = (mode & S_IRUSR) ? 'r' : '-';
    *s++ = (mode & S_IWUSR) ? 'w' : '-';
    *s++ = (mode & S_IXUSR) ? 'x' : '-';
    *s++ = (mode & S_IRGRP) ? 'r' : '-';
    *s++ = (mode & S_IWGRP) ? 'w' : '-';
    *s++ = (mode & S_IXGRP) ? 'x' : '-';
    *s++ = (mode & S_IROTH) ? 'r' : '-';
    *s++ = (mode & S_IWOTH) ? 'w' : '-';
    *s++ = (mode & S_IXOTH) ? 'x' : '-';
    *s++ = ' ';
    *s++ = '\0';
    print(buffer);
}