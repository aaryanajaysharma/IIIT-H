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
* Open the file using open() system call.
* Check if the file is opened successfully, if not print error message and exit.
* Create a directory named “Assignment” using mkdir() system call.
* Extract the file name from the path of the file using strtok() or strsep() function.
* Create a new file in the Assignment directory using open() system call.
* Check if the file is created successfully, if not print error message and exit.
* Reverse the specified range of contents of the file chunk by chunk.
    * Read the contents of the file chunk by chunk from start_position to beginning of the file.
    * Reverse the contents of the chunk.
    * Write the contents of the chunk to the new file.
    * Read the contents of the file chunk by chunk from start_position to end_position and write it to the file as it is.
    * Read the contents of the file chunk by chunk from end of the file to end_position.
    * Reverse the contents of the chunk.
    * Write the contents of the chunk to the new file.
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
        printSystem("Error: Invalid number of arguments");
        exit(EXIT_FAILURE);
    }

    // Open the file using open() system call
    int readFileDescriptor = open(argv[1], O_RDONLY);
    // Check if the file is opened successfully
    if (readFileDescriptor == -1)
    {
        perror("Invadid file path");
        exit(EXIT_FAILURE);
    }
    long long unsigned int readFileSize = lseek(readFileDescriptor, 0, SEEK_END);
    // Create a directory named “Assignment” using mkdir() system call
    int mkdirStatus = mkdir("Assignment", S_IRWXU); // masks = S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH
    // Check if the directory is created successfully

    struct stat di;
    // if directory doesn't exist
    if (stat("./Assignment", &di) == -1)
    {
        // If it does not exist, and still encounters error creating it
        if (mkdirStatus == -1)
        {
            perror("Error: Directory not created");
            exit(EXIT_FAILURE);
        }
    }

    // Extract the file name from the path of the file
    char *token;
    char *rest = argv[1];
    char *saveptr;
    do
    {
        saveptr = token;
    } while ((token = strsep(&rest, "/")) != NULL);
    // printf("%s" , saveptr);
    char writeFilePath[250] = "./Assignment/2_";
    // concat writeFilePath and saveptr as new string using strlcat and print the concatenated string
    strlcat(writeFilePath, saveptr, sizeof(writeFilePath));

    // Create a new file in the Assignment directory using open() system call
    int writeFileDescriptor = open(writeFilePath, O_WRONLY | O_CREAT, S_IRWXU | O_TRUNC, 0600);
    // Check if the file is created successfully
    if (writeFileDescriptor == -1)
    {
        perror("File could not be created");
        exit(EXIT_FAILURE);
    }

    // Reverse the specified contents of the file chunk by chunk

    // Convert the start_position and end_position to long long unsigned int
    char *chunk = (char *)malloc(ChunkSize);
    int chunkSize = ChunkSize;
    char *chunkReverse = (char *)malloc(ChunkSize);
    float progress = 0;
    char progressString[12];
    off_t totalBytesRead = 0;
    off_t totalBytesWritten = 0;
    off_t totalFileSize = readFileSize;
    off_t start_position = atoll(argv[2]); // convert string to long long int
    off_t end_position = atoll(argv[3]);
    lseek(readFileDescriptor, start_position, SEEK_SET);
    // * Read the file chunk by chunk from start_position to beginning of the file, reverse the chunks, and write it to the new file
    // * then read the file chunk by chunk from start_position to end_position, and write it to the file as it is
    // * Then read the file chunk by chunk from end of file to end_position, reverse the chunks, and write it to the file
    while (totalBytesRead < start_position)
    {
        if (totalBytesRead + ChunkSize > start_position)
        {
            chunkSize = start_position - totalBytesRead;
        }
        lseek(readFileDescriptor, -chunkSize, SEEK_CUR);
        read(readFileDescriptor, chunk, chunkSize);
        lseek(readFileDescriptor, -chunkSize, SEEK_CUR);
        for (int i = 0; i < chunkSize; i++)
        {
            chunkReverse[chunkSize - i - 1] = chunk[i];
        }
        write(writeFileDescriptor, chunkReverse, chunkSize);
        totalBytesRead += chunkSize;
        totalBytesWritten += chunkSize;
        progress = (float)totalBytesWritten * 100 / totalFileSize;
        sprintf(progressString, "\r%3.2f%%", progress);
        printSystem(progressString);
    }

    // Write the specified portion of the file as it is
    lseek(readFileDescriptor, start_position, SEEK_SET);
    while (totalBytesRead < end_position)
    {
        if (totalBytesRead + ChunkSize > end_position)
        {
            chunkSize = end_position - totalBytesRead;
        }
        read(readFileDescriptor, chunk, chunkSize);
        write(writeFileDescriptor, chunk, chunkSize);
        totalBytesRead += chunkSize;
        totalBytesWritten += chunkSize;
        progress = (float)totalBytesWritten * 100 / totalFileSize;
        sprintf(progressString, "\r%3.2f%%", progress);
        printSystem(progressString);
    }

    // Read the file chunk by chunk from end of file to end_position, reverse the chunks, and write it to the file
    lseek(readFileDescriptor, 0, SEEK_END);
    while (totalBytesRead < totalFileSize)
    {
        if (totalBytesRead + ChunkSize > totalFileSize)
        {
            chunkSize = totalFileSize - totalBytesRead;
        }
        lseek(readFileDescriptor, -chunkSize, SEEK_CUR);
        read(readFileDescriptor, chunk, chunkSize);
        lseek(readFileDescriptor, -chunkSize, SEEK_CUR);
        for (int i = 0; i < chunkSize; i++)
        {
            chunkReverse[chunkSize - i - 1] = chunk[i];
        }
        write(writeFileDescriptor, chunkReverse, chunkSize);
        totalBytesRead += chunkSize;
        totalBytesWritten += chunkSize;
        progress = (float)totalBytesWritten * 100 / totalFileSize;
        sprintf(progressString, "\r%3.2f%%", progress);
        printSystem(progressString);
    }

    // Close the file using close() system call
    close(readFileDescriptor);
    close(writeFileDescriptor);
    return 0;
}

/*
Example:
For 3 7,

Input: "0123456789abc"
Output: "2103456cba987"

012345789
0 0: 987543210
3 4: 210398754
6 7: 543210798
3 7: 2103456987
*/