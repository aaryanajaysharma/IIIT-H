#include <stdio.h>
#include <stdlib.h>
#include "mpi.h"

int main(int argc, char *argv[])
{

    MPI_Init(&argc, &argv);

    int size;
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (size != 2)
    {
        printf("This application is meant to be run with 2 MPI processes.\n");
        MPI_Abort(MPI_COMM_WORLD, EXIT_FAILURE);
    }

    enum role_t
    {
        SENDER,
        RECIEVER
    };

    int my_rank;

    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

    switch (my_rank)
    {
    case SENDER:
    {
        int buffer_sent = 12345;
        printf("MPI process %d sending value %d.\n", my_rank, buffer_sent);
        MPI_Send(&buffer_sent, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
        break;
    }
    case RECIEVER:
    {
        int buffer_received;
        MPI_Recv(&buffer_received, 1, MPI_INT, SENDER, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("MPI process %d received value %d.\n", my_rank, buffer_received);
        break;
    }
    default:
        printf("I am not supposed to be here.\n");
        MPI_Abort(MPI_COMM_WORLD, EXIT_FAILURE);
    }
    MPI_Finalize();
    return EXIT_SUCCESS;
}
