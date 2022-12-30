# import example
import cellular_automata as CA

initialGrid = CA.create_initial_grid()
rows = CA.rows
cols = CA.cols
nextGrid = [[0 for x in range(CA.cols)] for y in range(CA.rows)]


def rule():
    for row in range(rows):
        for col in range(cols):
            if initialGrid[row][col - 1] == 1 or initialGrid[row][col] == 1:
                nextGrid[row][col] = 1


def main():
    """
    Setup the Cellular Automaton to run for a given number of iterations.
    """

    global nextGrid, initialGrid
    CA.clear_console()

    # Get the number of iterations that the Cellular Automaton should run for
    CA.print_grid(initialGrid, 0)
    iteration = int(input("Number of iteration: "))
    itr_real = 1
    while iteration is not -1:
        CA.resize_console(rows, cols)
        # Run Cellular Automaton sequence
        for itr in range(1, iteration+1):
            rule()
            CA.time.sleep(1 / 5.0)
            initialGrid, nextGrid = nextGrid, initialGrid
            CA.print_grid(initialGrid, itr_real)
            itr_real += 1
        # CA.print_grid(nextGrid, itr)
        file1 = open("output.txt", "w")
        for row in range(rows):
            for col in range(cols):
                if nextGrid[row][col] == 1:
                    file1.write('X')
                else:
                    file1.write('O')
            file1.write('\n')
        iteration = int(input("Number of iteration: "))
    file1.close()
    print("Output saved in output.txt.")


if __name__ == '__main__':
    main()
