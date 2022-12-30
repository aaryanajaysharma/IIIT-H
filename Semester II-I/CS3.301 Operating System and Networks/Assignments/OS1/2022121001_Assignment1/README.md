
# OS and Networks
___Assignment 1___

## Aim
**Question 1**

Our aim is to write a program that reverses the contents of the file and store the result in a new file in a directory named “Assignment”.
The program should take the path of the file as a command line argument.
And the output file should be saved in Assignment directory named as “1_<original file name>.c”.
We will be reversing the contents of the file chunk by chunk.
The chunk size is 10,48,576 bytes / 1024KB / 1MB.

**Question 2**

The aim of the program is to reverse the specified portion of the file.
The program takes 3 command line arguments:
- file_path
- start_position
- end_position
We need to reverse the contents of the file from the beginning of the file to the start_position, and from the end_position to the end of the file.
That is, we need to reverse the whole file except the specified portion.

**Question 3**

* Check if the newfile is the reverse of the original file (old_file).
* Check the permissions for the two files and the directory
* Check if the directory exists.

## Jusitification for chunk and chunk size
 We tried to reverse the file byte by byte, but the program was taking too much time to execute, therefore we chose to reverse the file chunk by chunk.
The size of the chunk was chosen to be 1MB, since we wanted the chunk size to be a power of 2, same as the block size of the disk / size of the word.
Also, anything larger than 1MB would occupy too much space in main memory, and anything smaller than 1MB would take too much time to execute.

## Assumptions
In question 1, 2 & 3, we assumed the file path to be relative to the working directory.

In question 2, we assumed from the first example, if m and n are given as argument to the program (where m <= n), then we need to reverse the contents of the file from the start to the (m)th byte of the file. Then from there, we keep the (m+1)th character to (n)th character as it is, and then reverse (n+1)th character to the last character. Therefore, always (n - m) characters remain in their place.

## Possible Limitations
The program was tested on Unix and Linux based Distribution Ubuntu. 
From the test results, we found that the program runs as excepted in Ubuntu, but may not produce the desired output if the file size is greater than chunk size (1MB) in Unix or similar systems.
This is because upon the program outputted undesirable in its initial few runs. It works perfectly in macOS v12.5, my current OS.

## Program Outline
**Question 1**
* Define function printSystem() which prints to STDOUT using write() system call.
* Check if the number of command line arguments is 2, if not print error message and exit.
* Open the file using open() system call.
* Check if the file is opened successfully, if not print error message and exit.
* Create a directory named “Assignment” using mkdir() system call.
* Check if the directory is created successfully, if not print error message and exit.
* Extract the file name from the path of the file using strtok() or strsep() function.
* Create a new file in the Assignment directory using open() system call.
* Check if the file is created successfully, if not print error message and exit.
* Reverse the contents of the file chunk by chunk.

**Question 2**
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
**Question 3**

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

## Notes

We have abstained from using strcat() and strtok() as the former is unsafe/prone to buffer overflow attacks, and the later is obsoleted by strsep() which handles delimiting characters properly. More information about this could be found in the man pages of the respective functions.
