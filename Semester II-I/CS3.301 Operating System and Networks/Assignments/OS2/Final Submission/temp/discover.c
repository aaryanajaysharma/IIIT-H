// Create a custom discover command which emulates the basics of the find command. The command should search for files in a directory hierarchy.

// The command will have the following optional command line arguments: discover <target_dir> <type_flags> <file_name>
// target directory specified using ‘.’, ‘..’, ‘~’ or directory_name or directory_path. [if this argument is not present, consider the current directory as the target directory]

// the following type flags can be used with the command
// -d → searches for all directories
// -f → searches for all files
// name of the file/directory to be found in the given directory hierarchy.
// If neither the file type nor the file name is provided as a command line argument, print all the contents of the target directory.

# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <unistd.h>
# include <sys/types.h>
# include <sys/stat.h>
# include <dirent.h>
# include <pwd.h>
# include <grp.h>


// implement the discover command here using scandir() and alphasort() functions

void discover(char *target_dir, char *type_flags, char *file_name)
{
    printf("\n");
    struct dirent **namelist;
    int n;
    n = scandir(target_dir, &namelist, NULL, alphasort);
    if (n < 0)
        perror("scandir");
    else {
        while (n--) {
            printf("%s\n", namelist[n]->d_name);
            struct stat fileStat;
            if(stat(namelist[n]->d_name,&fileStat) < 0)    
                return;
            if(S_ISDIR(fileStat.st_mode))
            {
                discover(namelist[n]->d_name, type_flags, file_name);
            }
            else
            {
                printf("%s" , namelist[n]->d_name);
            }
            free(namelist[n]);
        }
        free(namelist);
    }
    printf("\n");
}

int main(int argc, char *argv[])
{
    char *target_dir, *type_flags, *file_name;
    if(argc == 1)
    {
        target_dir = ".";
        type_flags = NULL;
        file_name = NULL;
    }
    else if(argc == 2)
    {
        if(strcmp(argv[1], "-d") == 0 || strcmp(argv[1], "-f") == 0)
        {
            target_dir = ".";
            type_flags = argv[1];
            file_name = NULL;
        }
        else
        {
            target_dir = argv[1];
            type_flags = NULL;
            file_name = NULL;
        }
    }
    else if(argc == 3)
    {
        if(strcmp(argv[1], "-d") == 0 || strcmp(argv[1], "-f") == 0)
        {
            target_dir = ".";
            type_flags = argv[1];
            file_name = argv[2];
        }
        else
        {
            target_dir = argv[1];
            type_flags = argv[2];
            file_name = NULL;
        }
    }
    else if(argc == 4)
    {
        target_dir = argv[1];
        type_flags = argv[2];
        file_name = argv[3];
    }
    else
    {
        printf("Usage: discover <target_dir> <type_flags> <file_name>");
        exit(1);
    }
    discover(target_dir, type_flags, file_name);
    return 0;
}
