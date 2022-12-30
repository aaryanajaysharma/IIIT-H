#include <sys/types.h> // for open()
#include <sys/stat.h>  // used for mkdir(), stat()
#include <fcntl.h>     // used for open
#include <unistd.h>    // used for write, lseek, STDOUT_FILENO
#include <errno.h>     // used for external variable errno used by perror()
#include <stdio.h>     // used for sprintf, perror
#include <stdlib.h>    // used for exit()
#include <string.h>    // strtok() or strsep()

#define ChunkSize 1048576 // 1048576 bytes = 1MB

// Program Outline

// * Define function printSystem() which prints to STDOUT using write() system call.
// * Check if the number of command line arguments is 2, if not print error message and exit.
// * Open the file using open() system call.
// * Check if the file is opened successfully, if not print error message and exit.
// * Create a directory named “Assignment” using mkdir() system call.
// * Check if the directory is created successfully, if not print error message and exit.
// * Extract the file name from the path of the file using strtok() or strsep() function.
// * Create a new file in the Assignment directory using open() system call.
// * Check if the file is created successfully, if not print error message and exit.
// * Reverse the contents of the file chunk by chunk.

void printSystem(char *str) // a replacement for printf() which uses write() system call
{
    int len = strlen(str);
    write(STDOUT_FILENO, str, len);
}

int main(int argc, char *argv[])
{
    // Check if the number of command line arguments is 2
    if (argc != 2)
    {
        printSystem("Error: Invalid number of arguments");
        exit(EXIT_FAILURE);
    }

    // Open the file using open() system call
    long long unsigned int readFileDescriptor = open(argv[1], O_RDONLY);
    // Check if the file is opened successfully
    if (readFileDescriptor == -1)
    {
        perror("Invadid file path");
        exit(EXIT_FAILURE);
    }
    off_t readFileSize = lseek(readFileDescriptor, 0, SEEK_END);
    // Create a directory named “Assignment” using mkdir() system call
    int mkdirStatus = mkdir("Assignment", S_IRWXU); // masks = S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH
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
    // char *fileName = strtok(argv[1], "/");
    char *token;
    char *rest = argv[1];
    char *saveptr;
    do
    {
        saveptr = token;
    } while ((token = strsep(&rest, "/")) != NULL);
    // printf("%s" , saveptr);
    char writeFilePath[250] = "./Assignment/1_";
    // concatanate writeFilePath and saveptr as new string using strlcat and print the concatenated string
    strlcat(writeFilePath, saveptr, sizeof(writeFilePath));

    // Create a new file in the Assignment directory using open() system call
    long long unsigned int writeFileDescriptor = open(writeFilePath, O_RDWR | O_CREAT, O_TRUNC, S_IRUSR | S_IWUSR);
    // Check if the file is created successfully
    if (writeFileDescriptor == -1)
    {
        perror("File could be not created");
        exit(EXIT_FAILURE);
    }

    // Reverse the contents of the file chunk by chunk

    // Seek to the end of the file
    lseek(readFileDescriptor, 0, SEEK_END);
    char *chunk = (char *)malloc(ChunkSize);
    int chunkSize = ChunkSize;
    char *chunkReverse = (char *)malloc(ChunkSize);
    float progress = 0;
    char progressString[12];
    off_t totalBytesRead = 0;
    off_t totalBytesWritten = 0;
    off_t totalFileSize = readFileSize;

    // Read the file chunk by chunk
    while (readFileSize > 0)
    {
        // Check if the chunk size is greater than the file size
        if (chunkSize > readFileSize)
        {
            chunkSize = readFileSize;
        }
        // Seek to the current position of the file
        lseek(readFileDescriptor, -chunkSize, SEEK_CUR);
        // Read the file chunk by chunk
        read(readFileDescriptor, chunk, chunkSize);
        lseek(readFileDescriptor, -chunkSize, SEEK_CUR);
        // Reverse the chunk
        for (int i = 0; i < chunkSize; i++)
        {
            chunkReverse[i] = chunk[chunkSize - i - 1];
        }
        // Write the reversed chunk to the file
        write(writeFileDescriptor, chunkReverse, chunkSize);
        // Update the file size
        readFileSize -= chunkSize;
        // Update the total bytes read
        totalBytesRead += chunkSize;
        // Update the total bytes written
        totalBytesWritten += chunkSize;
        // Update and print the progress
        progress = (float)(totalBytesRead) / totalFileSize;
        sprintf(progressString, "\r%.2f%%", progress * 100);
        printSystem(progressString);
    }
    // Close the file
    close(readFileDescriptor);
    close(writeFileDescriptor);
    return 0;
}
