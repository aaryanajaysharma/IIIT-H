from mpi4py import MPI
import random
import array

def flatten(matrix):
    """Flatten a 2D matrix to a 1D array."""
    return [elem for row in matrix for elem in row]

def unflatten(array, rows, cols):
    """Unflatten a 1D array to a 2D matrix."""
    return [array[i * cols:(i + 1) * cols] for i in range(rows)]


def floyd_warshall_parallel(local_matrix, n, rank, size, rows_per_process, start_indices):
    comm = MPI.COMM_WORLD

    # Initialize the final_matrix on the root process
    final_matrix = None
    if rank == 0:
        final_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Run the Floyd-Warshall algorithm on each process
    for k in range(n):
        # Determine the process that contains the k-th row
        owner = next(i for i in range(size) if start_indices[i] <= k < start_indices[i] + rows_per_process[i])

        # Prepare the k-th row for broadcasting
        if rank == owner:
            row_k = array.array('i', local_matrix[k - start_indices[owner]])
        else:
            row_k = array.array('i', [0] * n)

        # Broadcast the k-th row to all processes
        comm.Bcast(row_k, root=owner)
        row_k = row_k.tolist()  # Convert back to list after broadcasting

        # Update the local rows
        for i in range(rows_per_process[rank]):
            for j in range(n):
                local_matrix[i][j] = min(local_matrix[i][j], local_matrix[i][k] + row_k[j])

    # Gather the updated rows from all processes
    if rank == 0:
        for i in range(size):
            if i == 0:
                final_matrix[:rows_per_process[i]] = local_matrix
            else:
                recv_data = array.array('i', [0] * (rows_per_process[i] * n))
                comm.Recv(recv_data, source=i)
                final_matrix[start_indices[i]:start_indices[i] + rows_per_process[i]] = unflatten(recv_data, rows_per_process[i], n)
    else:
        send_data = array.array('i', flatten(local_matrix))
        comm.Send(send_data, dest=0)

    return final_matrix


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        # Input: Read the graph's adjacency matrix
        n = int(input().strip())
        adj_matrix = [list(map(int, input().split())) for _ in range(n)]
        # Replace -1 with a large number to represent infinity
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][j] == -1:
                    adj_matrix[i][j] = 10**9

        # Calculate the number of rows each process will handle
        rows_per_process = [n // size + (1 if i < n % size else 0) for i in range(size)]
        # Calculate the starting index for each process
        start_indices = [sum(rows_per_process[:i]) for i in range(size)]
    else:
        adj_matrix = None
        n = None
        rows_per_process = None
        start_indices = None

    # Broadcast the size of the matrix and other information to all processes
    n = comm.bcast(n, root=0)
    rows_per_process = comm.bcast(rows_per_process, root=0)
    start_indices = comm.bcast(start_indices, root=0)

    # Allocate space for the local chunk of the matrix
    local_n = rows_per_process[rank]
    local_matrix = [[0 for _ in range(n)] for _ in range(local_n)]

    # Manually send and receive the appropriate chunks of the matrix
    if rank == 0:
        # Send the chunks to each process
        for i in range(1, size):
            send_data = array.array('i', flatten(adj_matrix[start_indices[i]:start_indices[i]+rows_per_process[i]]))
            comm.Send(send_data, dest=i)
        local_matrix = adj_matrix[:rows_per_process[0]]
    else:
        # Receive the chunk of the matrix
        recv_data = array.array('i', [0] * (local_n * n))
        comm.Recv(recv_data, source=0)
        local_matrix = unflatten(recv_data, local_n, n)

    # Run the parallel Floyd-Warshall algorithm
    final_matrix = floyd_warshall_parallel(local_matrix, n, rank, size, rows_per_process, start_indices)

    # Output the final matrix
    if rank == 0:
        for row in final_matrix:
            print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()