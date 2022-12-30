
# feline.sh


/ᐠ. ｡.ᐟ\ᵐᵉᵒʷˎˊ˗

A basic shell implemented in c, for and by a cat lover. —ฅ/ᐠ. ̫ .ᐟ\ฅ —



## Usage
In the root directory of the project, run the following commands:
```bash
$ make clean
$ make
$ ./feline.sh
```

To quit the shell, type `exit` or `quit`

## Features

- [x] Basic shell prompt
- [x] Basic command execution
- [x] Basic history
- [x] Basic command line editing
- [x] Basic command line history
- [x] Basic tab completion
- [x] Basic ASCII cat art


## File Structure
Files | Description | Status | Notes
--- | --- | --- | ---
`feline.h` | Header file | Done |
`Makefile` | Makefile | Done |
`README.md` | This file | Done |
`main.c` | Main file | Done |
`interpret_command.c` | Interprets command | Done |
`aux_ls_[...].c` | Auxiliary functions for ls | Done |
`display_[...].c` | Displays output | Done |
exec_[...].c | Executes commands | Done |
`save_history.c` | Saves history | Done |
`check_bg.c` | Checks for background processes | Done |
`string_splitters.c` | Splits strings | Done |
`read_command.c` | Reads command | Done |