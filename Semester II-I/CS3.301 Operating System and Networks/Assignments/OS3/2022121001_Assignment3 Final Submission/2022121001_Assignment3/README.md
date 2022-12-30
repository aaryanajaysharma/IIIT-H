
# feline.sh


/ᐠ. ｡.ᐟ\ᵐᵉᵒʷˎˊ˗

A basic shell implemented in c, for and by a cat lover. —ฅ/ᐠ. ̫ .ᐟ\ฅ —



## Usage
In the root directory of the project, run the following commands:
```bash
$ make clean
$ make
$ ./feline
```

To quit the shell, type `exit` or `quit`

## Features

- [x] Basic shell prompt
- [x] Basic command execution
- [x] History
- [x] Command line editing
- [x] Command line history
- [x] Tab completion
- [x] Input/output redirection
- [x] Piping
- [x] I/O redirection within pipes
- [x] Signal handling
- [x] Cool ASCII cat art


## File Structure
Files | Description | Status 
--- | --- | --- 
`feline.h` | Header file | Done
`Makefile` | Makefile | Done
`README.md` | This file | Done
`main.c` | Main file | Done
`interpret_command.c` | Interprets command | Done
`aux_ls_[...].c` | Auxiliary functions for ls | Done
`display_[...].c` | Displays output | Done
`exec_[...].c` | Executes commands | Done
`save_history.c` | Saves history | Done
`check_bg.c` | Checks for background processes | Done
`string_splitters.c` | Splits strings | Done
`read_command.c` | Reads command | Done
`set_ip_op_redir.c` | Sets input/output redirection | Done
`pipe_handler.c` | Handles piping | Done
`signal_handler.c` | Handles signals | Done


## Limitations

- [ ] fg, bg, jobs, sig commands not implemented
- [ ] pinfo command not implemented
- [ ] Nightswatch not implemented
- [ ] No ctrl+D support (not working for some reason)