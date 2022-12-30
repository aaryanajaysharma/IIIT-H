import time
import os
# import random
import sys


def clear_console():
    """
    Clears the console using a system command based on the user's operating system.

    """

    if sys.platform.startswith('win'):
        os.system("cls")
    elif sys.platform.startswith('linux'):
        os.system("clear")
    elif sys.platform.startswith('darwin'):
        os.system("clear")
    else:
        print("Unable to clear terminal. Your operating system is not supported.\n\r")


def resize_console(rows, cols):
    """
    Re-sizes the console to the size of rows x columns

    :param rows: Int - The number of rows for the console to re-size to
    :param cols: Int - The number of columns for the console to re-size to
    """

    if cols < 32:
        cols = 32

    if sys.platform.startswith('win'):
        command = "mode con: cols={0} lines={1}".format(cols + cols, rows + 5)
        os.system(command)
    elif sys.platform.startswith('linux'):
        command = "\x1b[8;{rows};{cols}t".format(rows=rows + 3, cols=cols + cols)
        sys.stdout.write(command)
    elif sys.platform.startswith('darwin'):
        command = "\x1b[8;{rows};{cols}t".format(rows=rows + 3, cols=cols + cols)
        sys.stdout.write(command)
    else:
        print("Unable to resize terminal. Your operating system is not supported.\n\r")


file = open("config.txt", 'r')
line1 = file.readline()
mnk = line1.split()
cols = int(mnk[0])
rows = int(mnk[1])
numberOfAliveCells = int(mnk[2])
file.close()


def create_initial_grid():
    file = open("config.txt", 'r')
    file.readline()
    m = cols
    n = rows
    k = numberOfAliveCells
    matrix = [[0 for x in range(m)] for y in range(n)]
    for _ in range(k):
        line = file.readline()
        xy = line.split()
        x = int(xy[0])
        y = int(xy[1])
        i = n - y
        j = x - 1
        matrix[i][j] = 1
    file.close()
    # for p in range(n):
    #     for q in range(m):
    #         print(matrix[p][q], end=" ")
    #     print()
    # print(m, n, k)
    # time.sleep(5)
    return matrix


def get_live_neighbors(row, col, grid):
    """
    Counts the number of live cells surrounding a center cell at grid[row][cell].

    :param row: Int - The row of the center cell
    :param col: Int - The column of the center cell
    :param rows: Int - The number of rows that the Game of Life grid has
    :param cols: Int - The number of columns that the Game of Life grid has
    :param grid: Int[][] - The list of lists that will be used to represent the Game of Life grid
    :return: Int - The number of live cells surrounding the cell at grid[row][cell]
    """

    life_sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Make sure to count the center cell located at grid[row][col]
            if not (i == 0 and j == 0):
                if row + i >= 0 and row+i < rows and col + j >= 0 and col+j < cols:
                    life_sum += grid[row + i][col + j]
    return life_sum


def print_grid(grid, generation):
    """
    Prints to console the Game of Life grid

    :param rows: Int - The number of rows that the Game of Life grid has
    :param cols: Int - The number of columns that the Game of Life grid has
    :param grid: Int[][] - The list of lists that will be used to represent the Game of Life grid
    :param generation: Int - The current generation of the Game of Life grid
    """

    clear_console()

    # A single output string is used to help reduce the flickering caused by printing multiple lines
    output_str = ""

    # Compile the output string together and then print it to console
    output_str += "Iteration {0} - To exit the program input -1 or press <Ctrl-C> \n\r".format(generation)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                output_str += "0 "
            else:
                output_str += "1 "
        output_str += "\n\r"
    print(output_str, end=" ")


def grid_changing(grid, next_grid):
    """
    Checks to see if the current generation Game of Life grid is the same as the next generation Game of Life grid.

    :param rows: Int - The number of rows that the Game of Life grid has
    :param cols: Int - The number of columns that the Game of Life grid has
    :param grid: Int[][] - The list of lists that will be used to represent the current generation Game of Life grid
    :param next_grid: Int[][] - The list of lists that will be used to represent the next generation of the Game of Life
    grid
    :return: Boolean - Whether the current generation grid is the same as the next generation grid
    """

    for row in range(rows):
        for col in range(cols):
            # If the cell at grid[row][col] is not equal to next_grid[row][col]
            if not grid[row][col] == next_grid[row][col]:
                return True
    return False

# def run_game():
#     """
#     Asks the user for input to setup the Game of Life to run for a given number of generations.
#
#     """
#
#     clear_console()
#
#     # Get the number of rows and columns for the Game of Life grid
#     clear_console()
#
#     # Get the number of generations that the Game of Life should run for
#     iteration = input("Number of iteration: ")
#     resize_console(rows, cols)
#
#     # Create the initial random Game of Life grids
#     current_generation = create_initial_grid()
#     next_generation = create_initial_grid()
#
#     # Run Game of Life sequence
#     gen = 1
#     for gen in range(1, iteration + 1):
#         if not grid_changing(rows, cols, current_generation, next_generation):
#             break
#         print_grid(rows, cols, current_generation, gen)
#         create_next_grid(rows, cols, current_generation, next_generation)
#         time.sleep(1 / 5.0)
#         current_generation, next_generation = next_generation, current_generation
#
#     print_grid(rows, cols, current_generation, gen)
#     return input("<Enter> to exit or r to run again: ")
