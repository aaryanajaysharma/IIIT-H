/**
 * This auxillary function displays a single line corresponding to a file when the command ls -l is called
 */

// The -l option is given, the following information is displayed for each file: file mode, number of links, owner name, group name, number of bytes in the file, abbreviated
// month, day-of-month file was last modified, hour file last modified, minute file last modified, and the pathname.

#include "feline.h"

int deb_display_line_ls = 0;
void display_line_ls(char *filepath, char *filename)
{
    struct stat file_status;
    if (stat(filepath, &file_status) != 0)
    {
        if (deb_display_line_ls)
            printn_debug(filepath);
        perror("Error while reading file status ");
        return;
    }
    display_permissions_ls(file_status.st_mode);
    char *buffer = memalloc_string(MAX_BUFFER_LENGTH);
    struct passwd *pw = getpwuid(file_status.st_uid); // If pw != 0, pw->pw_name contains the user name
    struct group *gr = getgrgid(file_status.st_gid);  // If gr != 0, gr->gr_name contains the group name
    if (pw == 0)
    {
        print_error("Error : User  not found");
        return;
    }
    if (gr == 0)
    {
        print_error("Error : Group  not found");
        return;
    }
    // co
    sprintf(buffer, "%2zu %s %s %7zu", file_status.st_nlink, pw->pw_name, gr->gr_name, file_status.st_size);
    print(buffer);
    char date[16];
    // strftime(date, 16, "%b %2d %2I:%2M", gmtime(&(file_status.st_mtime)));
    strftime(date, 16, "%b %2d %2h:%2M", localtime(&(file_status.st_mtime)));
    sprintf(buffer, " %s %s", date, filename);
    // color blue for directories, green for executables, 
    if (S_ISDIR(file_status.st_mode))
        print_blue(buffer);
    else if (file_status.st_mode & S_IXUSR)
        print_green(buffer);
    else
        print(buffer);
    print_n(buffer);
    free(buffer);
}
