from mpi4py import MPI
import array

def compute_multibrot(c, d, max_iter):
    z = 0
    for i in range(max_iter):
        z = z**d + c
        if abs(z) > 2:
            return 0
    return 1

def flatten(matrix):
    return [elem for row in matrix for elem in row]

def unflatten(arr, rows, cols):
    return [arr[i * cols:(i + 1) * cols] for i in range(rows)]

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        N, M, D, K = [int(x) for x in input().split()]
    else:
        N = M = D = K = None

    N = comm.bcast(N, root=0)
    M = comm.bcast(M, root=0)
    D = comm.bcast(D, root=0)
    K = comm.bcast(K, root=0)

    x_min, x_max = -1.5, 1
    y_min, y_max = -1, 1

    rows_per_proc = M // size
    extra_rows = M % size
    max_rows = rows_per_proc + (1 if rank < extra_rows else 0)
    start_row = rank * rows_per_proc + min(rank, extra_rows)
    end_row = start_row + max_rows

    partial_result = [[0 for _ in range(N)] for _ in range(max_rows)]
    for i in range(start_row, end_row):
        for j in range(N):
            x = x_min + j * (x_max - x_min) / (N - 1)
            y = y_min + i * (y_max - y_min) / (M - 1)
            c = complex(x, y)
            partial_result[i - start_row][j] = compute_multibrot(c, D, K)

    send_data = array.array('i', flatten(partial_result))
    send_counts = comm.gather(len(send_data), root=0)

    if rank == 0:
        recv_data = array.array('i', [0] * (N * M))
        displacements = [sum(send_counts[:i]) for i in range(size)]
    else:
        recv_data = None
        displacements = None

    comm.Gatherv(send_data, [recv_data, send_counts, displacements, MPI.INT], root=0)

    if rank == 0:
        full_result = unflatten(recv_data, M, N)
        for row in full_result:
            print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
