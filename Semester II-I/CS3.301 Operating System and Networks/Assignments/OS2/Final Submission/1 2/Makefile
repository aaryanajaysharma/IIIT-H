feline: \
			main.o \
			signal_handler.o \
			print.o \
			display_prompt.o \
			display_killed_children.o \
			exec_cd.o \
			read_command.o \
			execute_builtin.o \
			execute_builtin_no_output.o \
			check_if_bg.o \
			exec_exit.o \
			exec_pwd.o \
			string_splitter.o \
			interpret_command.o \
			exec_echo.o \
			exec_ls.o \
			exec_cd.o \
			exec_discover.o \
			exec_killall.o \
			exec_foreground.o \
			aux_ls_display_line.o \
			aux_ls_display_permissions.o \
			exec_history.o \
			save_to_history.o \
			exec_clearhistory.o \
			display_feline.o \
			exec_help.o
	$(CC) -g -o feline $^  -L/usr/local/lib -I/usr/local/include -lreadline -Wall 

clean:
	@rm -f *.o feline history.txt

main.o: feline.h main.c
	$(CC) -g -c main.c  -L/usr/local/lib -I/usr/local/include -lreadline -Wall 

signal_handler.o: feline.h signal_handler.c
	$(CC) -g -c signal_handler.c 

print.o: feline.h print.c
	$(CC) -g -c print.c

display_feline.o: feline.h display_feline.c
	$(CC) -g -c display_feline.c

display_killed_children.o: feline.h display_killed_children.c
	$(CC) -g -c display_killed_children.c

display_prompt.o: feline.h display_prompt.c
	$(CC) -g -c display_prompt.c

check_if_bg.o: feline.h check_if_bg.c
	$(CC) -g -c check_if_bg.c

exec_cd.o: feline.h exec_cd.c
	$(CC) -g -c exec_cd.c

exec_discover.o: feline.h exec_discover.c
	$(CC) -g -c exec_discover.c

exec_echo.o: feline.h exec_echo.c
	$(CC) -g -c exec_echo.c

exec_ls.o: feline.h exec_ls.c
	$(CC) -g -c exec_ls.c

exec_exit.o: feline.h exec_exit.c
	$(CC) -g -c exec_exit.c

exec_pwd.o: feline.h exec_pwd.c
	$(CC) -g -c exec_pwd.c

exec_overkill.o: feline.h exec_killall.c
	$(CC) -g -c exec_killall.c

exec_foreground.o: feline.h exec_foreground.c
	$(CC) -g -c exec_foreground.c

exec_help.o: feline.h exec_help.c
	$(CC) -g -c exec_help.c

string_splitter.o: feline.h string_splitter.c
	$(CC) -g -c string_splitter.c

read_command.o: feline.h read_command.c
	$(CC) -g -c read_command.c

interpret_command.o: feline.h interpret_command.c
	$(CC) -g -c interpret_command.c

execute_builtin.o: feline.h execute_builtin.c
	$(CC) -g -c execute_builtin.c

execute_builtin_no_output.o: feline.h execute_builtin_no_output.c
	$(CC) -g -c execute_builtin_no_output.c

aux_ls_display_line.o: feline.h aux_ls_display_line.c
	$(CC) -g -c aux_ls_display_line.c

aux_ls_display_permissions.o: feline.h aux_ls_display_permissions.c
	$(CC) -g -c aux_ls_display_permissions.c

exec_history.o: feline.h exec_history.c
	$(CC) -g -c exec_history.c

exec_clearhistory.o: feline.h exec_clearhistory.c
	$(CC) -g -c exec_clearhistory.c

save_to_history.o: feline.h save_to_history.c
	$(CC) -g -c save_to_history.c

# execute_builtin.o: feline.h execute_builtin.c
# 	$(CC) -g -c execute_builtin.c