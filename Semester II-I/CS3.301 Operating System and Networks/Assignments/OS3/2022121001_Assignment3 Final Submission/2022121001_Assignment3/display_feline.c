// display_feline() function to display the feline logo for before the shell starts running for 3 seconds

#include "feline.h"

void display_feline()
{

    puts(

        "\033[1;35m    *               MMM8&&&            *\n"
        "                  MMMM88&&&&&    .\n"
        "                 MMMM88&&&&&&&\n"
        "     *           MMM88&&&&&&&&\n"
        "                 MMM88&&&&&&&&\n"
        "                  MMM88&&&&&&\n"
        "                    MMM8&&&      *\n"
        "          |\\___/|   meow\n"
        "         =) ^Y^ (=            .              '\n"
        "          \\  ^  /\n"
        "           )=*=(       *\n"
        "          /     \\n"
        "          |     |\n"
        "         /| | | | \n"
        "         \\| | |_|/\\\n"
        "  _/\\_//_// ___/\\_/\\_/\\_/\\_/\\_/\\_/\\_\n"
        "  |  |  |  | \\_) |  |  |  |  |  |  |\n"
        "  |  |  |  |  |  |  |  |  |  |  |  |  \n"
        "  |  |  |  |  |  |  |  |  |  |  |  |  \n"
        "  |  |  |  |  |  |  |  |  |  |  |  |  \n"
        "\033[0m");
    // clear screen
    sleep(5);
    print("\033[H\033[J");
}