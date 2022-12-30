#include <sys/types.h> // for open()
#include <sys/stat.h>  // used for mkdir(), stat()
#include <fcntl.h>     // used for open
#include <unistd.h>    // used for write, lseek, STDOUT_FILENO
#include <errno.h>     // used for external variable errno used by perror()
#include <stdio.h>     // used for sprintf, perror
#include <stdlib.h>    // used for exit()
#include <string.h>    // strtok() or strsep()

#define ChunkSize 1048576 // 1048576 bytes = 1MB

/*
Program Outline:
* Define function printSystem() which prints to STDOUT using write() system call.
* Check if the number of command line arguments is 4, if not print error message and exit.
* Check whether directory exists, if not print error message.
* Initialize a file descriptors for new file and old file.
* Check if the files are opened successfully, if not print error message and exit.
* Check if the new file is the reverse of the old file using the newly opened file descriptors.
    * Take a chunck of the new file from the end and compare it with the chunk of the old file taken from the start.
    * If the chunks are not reverse of each other, print the No to STDOUT and break out of the loop.
    * If they are reverse of each other, continue to the next chunk until all chuncks are checked.
    * If all chunks are checked, print Yes to STDOUT and continue the program execution.
* Create structure of type stat to store the file information of new file.
* Check the permissions of the file using stat() system call.
    * For each of User, Group and Others, check if the file has read, write and execute permissions.
    * If the file has a particular permission, print the Yes to STDOUT.
    * If the file does not have a particular permissions, print the No to STDOUT.
* Repeat the above steps for the old file and directory.
* Close the file descriptors.
*/

void printSystem(char *str) // a replacement for printf() which uses write() system call
{
    int len = strlen(str);
    write(STDOUT_FILENO, str, len);
}

int main(int argc, char *argv[])
{
    // Check if the number of command line arguments is 4, if not print error message and exit.
    if (argc != 4)
    {
        printSystem("Error: Invalid number of arguments: ");
        printf("%d", argc);
        printSystem("\n");
        exit(EXIT_FAILURE);
    }
    
    struct stat di;
    // if directory doesn't exist
    if (stat(argv[3], &di) == -1)
    {
        perror("Error: Directory does not exist\n");
    }
    else{
        printSystem("Directory is created: Yes\n");
    }
    
    // Open the file using open() system call
    int newFileDescriptor = open(argv[1], O_RDONLY);
    // Check if the file is opened successfully
    if (newFileDescriptor == -1)
    {
        perror("Invadid file path");
        exit(EXIT_FAILURE);
    }
    int oldFileDescriptor = open(argv[2], O_RDONLY);
    // Check if the file is opened successfully
    if (oldFileDescriptor == -1)
    {
        perror("Invadid file path");
        exit(EXIT_FAILURE);
    }
    off_t readFileSize = lseek(newFileDescriptor, 0, SEEK_END);

    // Seek to the end of the file
    lseek(newFileDescriptor, 0, SEEK_END);
    lseek(oldFileDescriptor, 0, SEEK_SET);
    char *newFileChunk = (char *)malloc(ChunkSize);
    int chunkSize = ChunkSize;
    char *oldFileChunk = (char *)malloc(ChunkSize);

    // Read the file newFileChunk by newFileChunk
    int flag = 1; // flag to check if the file is actually reversed or not
    while (readFileSize > 0)
    {
        // Check if the newFileChunk size is greater than the file size
        if (chunkSize > readFileSize)
        {
            chunkSize = readFileSize;
        }
        // Seek to the current position of the file
        lseek(newFileDescriptor, -chunkSize, SEEK_CUR);
        // Read the file newFileChunk by newFileChunk
        read(newFileDescriptor, newFileChunk, chunkSize);
        read(oldFileDescriptor, oldFileChunk, chunkSize);
        lseek(oldFileDescriptor, chunkSize, SEEK_CUR);
        // Check if the newFileChunk is the reverse of the oldFileChunk, if not print "Whether file contents are reversed in newfile: No", else print "Whether file contents are reversed in newfile: Yes"
        for (int i = 0; i < chunkSize; i++)
        {
            if (newFileChunk[i] != oldFileChunk[chunkSize - i - 1])
            {
                printSystem("Whether file contents are reversed in newfile: No\n");
                flag = 0;
                break;
            }   
        }
        readFileSize -= chunkSize;
    }
    if (flag)
    {
        printSystem("Whether file contents are reversed in newfile: Yes\n");
    }

    printSystem("Information about the new file:\n");
    // Check the permissions for the new file
    struct stat st;
    if (stat(argv[1], &st) == -1)
    {
        perror("Error: File does not exist\n");
    }
    else
    {
        // Check if the user has read permissions on the new file
        if (st.st_mode & S_IRUSR)
        {
            printSystem("User has read permissions on newfile: Yes\n");
        }
        else
        {
            printSystem("User has read permissions on newfile: No\n");
        }
        // Check if the user has write permissions on the new file
        if (st.st_mode & S_IWUSR)
        {
            printSystem("User has write permission on newfile: Yes\n");
        }
        else
        {
            printSystem("User has write permission on newfile: No\n");
        }
        // Check if the user has execute permissions on the new file
        if (st.st_mode & S_IXUSR)
        {
            printSystem("User has execute permission on newfile: Yes\n");
        }
        else
        {
            printSystem("User has execute permission on newfile: No\n");
        }
        // Check if the group has read permissions on the new file
        if (st.st_mode & S_IRGRP)
        {
            printSystem("Group has read permissions on newfile: Yes\n");
        }
        else
        {
            printSystem("Group has read permissions on newfile: No\n");
        }
        // Check if the group has write permissions on the new file
        if (st.st_mode & S_IWGRP)
        {
            printSystem("Group has write permission on newfile: Yes\n");
        }
        else
        {
            printSystem("Group has write permission on newfile: No\n");
        }
        // Check if the group has execute permissions on the new file
        if (st.st_mode & S_IXGRP)
        {
            printSystem("Group has execute permission on newfile: Yes\n");
        }
        else
        {
            printSystem("Group has execute permission on newfile: No\n");
        }
        // Check if the others have read permissions on the new file
        if (st.st_mode & S_IROTH)
        {
            printSystem("Others has read permissions on newfile: Yes\n");
        }
        else
        {
            printSystem("Others has read permissions on newfile: No\n");
        }
        // Check if the others have write permissions on the new file
        if (st.st_mode & S_IWOTH)
        {
            printSystem("Others has write permission on newfile: Yes\n");
        }
        else
        {
            printSystem("Others has write permission on newfile: No\n");
        }
        // Check if the others have execute permissions on the new file
        if (st.st_mode & S_IXOTH)
        {
            printSystem("Others has execute permission on newfile: Yes\n");
        }
        else
        {
            printSystem("Others has execute permission on newfile: No\n");
        }
    }
    // Check permissions for the old file
    printSystem("Information about the old file:\n");
    struct stat st1;
    if(stat(argv[2], &st) == -1){
        perror("Error: File does not exist\n");
    }
    else
    {
        // Check if the user has read permissions on the old file
        if (st1.st_mode & S_IRUSR)
        {
            printSystem("User has read permissions on oldfile: Yes\n");
        }
        else
        {
            printSystem("User has read permissions on oldfile: No\n");
        }
        // Check if the user has write permissions on the old file
        if (st1.st_mode & S_IWUSR)
        {
            printSystem("User has write permission on oldfile: Yes\n");
        }
        else
        {
            printSystem("User has write permission on oldfile: No\n");
        }
        // Check if the user has execute permissions on the old file
        if (st1.st_mode & S_IXUSR)
        {
            printSystem("User has execute permission on oldfile: Yes\n");
        }
        else
        {
            printSystem("User has execute permission on oldfile: No\n");
        }
        // Check if the group has read permissions on the old file
        if (st1.st_mode & S_IRGRP)
        {
            printSystem("Group has read permissions on oldfile: Yes\n");
        }
        else
        {
            printSystem("Group has read permissions on newfile: No\n");
        }
        // Check if the group has write permissions on the old file
        if (st1.st_mode & S_IWGRP)
        {
            printSystem("Group has write permission on oldfile: Yes\n");
        }
        else
        {
            printSystem("Group has write permission on oldfile: No\n");
        }
        // Check if the group has execute permissions on old new file
        if (st1.st_mode & S_IXGRP)
        {
            printSystem("Group has execute permission on oldfile: Yes\n");
        }
        else
        {
            printSystem("Group has execute permission on oldfile: No\n");
        }
        // Check if the others have read permissions on the old file
        if (st1.st_mode & S_IROTH)
        {
            printSystem("Others has read permissions on oldfile: Yes\n");
        }
        else
        {
            printSystem("Others has read permissions on oldfile: No\n");
        }
        // Check if the others have write permissions on the old file
        if (st1.st_mode & S_IWOTH)
        {
            printSystem("Others has write permission on oldfile: Yes\n");
        }
        else
        {
            printSystem("Others has write permission on oldfile: No\n");
        }
        // Check if the others have execute permissions on the old file
        if (st1.st_mode & S_IXOTH)
        {
            printSystem("Others has execute permission on oldfile: Yes\n");
        }
        else
        {
            printSystem("Others has execute permission on oldfile: No\n");
        }
    }

    // check permission for the directory
    printSystem("Information about the directory:\n");
    struct stat st2;
    if(stat(argv[3], &st2) == -1){
        perror("Error: File does not exist\n");
    }
    else
    {
        // Check if the user has read permissions on the directory
        if (st2.st_mode & S_IRUSR)
        {
            printSystem("User has read permissions on directory: Yes\n");
        }
        else
        {
            printSystem("User has read permissions on directory: No\n");
        }
        // Check if the user has write permissions on the directory
        if (st2.st_mode & S_IWUSR)
        {
            printSystem("User has write permission on directory: Yes\n");
        }
        else
        {
            printSystem("User has write permission on directory: No\n");
        }
        // Check if the user has execute permissions on the directory
        if (st2.st_mode & S_IXUSR)
        {
            printSystem("User has execute permission on directory: Yes\n");
        }
        else
        {
            printSystem("User has execute permission on directory: No\n");
        }
        // Check if the group has read permissions on the directory
        if (st2.st_mode & S_IRGRP)
        {
            printSystem("Group has read permissions on directory: Yes\n");
        }
        else
        {
            printSystem("Group has read permissions on directory: No\n");
        }
        // Check if the group has write permissions on the directory
        if (st2.st_mode & S_IWGRP)
        {
            printSystem("Group has write permission on directory: Yes\n");
        }
        else
        {
            printSystem("Group has write permission on directory: No\n");
        }
        // Check if the group has execute permissions on the directory
        if (st2.st_mode & S_IXGRP)
        {
            printSystem("Group has execute permission on directory: Yes\n");
        }
        else
        {
            printSystem("Group has execute permission on directory: No\n");
        }
        // Check if the others have read permissions on the directory
        if (st2.st_mode & S_IROTH)
        {
            printSystem("Others has read permissions on directory: Yes\n");
        }
        else
        {
            printSystem("Others has read permissions on directory: No\n");
        }
        // Check if the others have write permissions on the directory
        if(st2.st_mode & S_IWOTH)
        {
            printSystem("Others has write permission on directory: Yes\n");
        }
        else
        {
            printSystem("Others has write permission on directory: No\n");
        }
        // Check if the others have execute permissions on the directory
        if (st2.st_mode & S_IXOTH)
        {
            printSystem("Others has execute permission on directory: Yes\n");
        }
        else
        {
            printSystem("Others has execute permission on directory: No\n");
        }
    }
    // close the file
    close(newFileDescriptor);
    close(oldFileDescriptor);
    return 0;
}