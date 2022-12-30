import subprocess
from FSM_sim import FST, eval
import os
import re
from csv import writer
directory = 'test_cases'


# sorts in proper alphanumeric order ( natural/version sort )
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


# create csv file with headers as rollno, and test_case_names
with open('results.csv', 'w') as f:
    f.write('Roll Number,')
    for file in sorted_alphanumeric(os.listdir(directory)):
        test_case_name = file.split('.')[0]
        f.write(test_case_name + ',')
    f.write("Weighted Average,")
    f.write("Plain Average")
    f.write('\n')

# iterate over files in
# that directory
directory_programs = 'student_programs'
# open student_programs/rollno/rps.cpp where rollno is directory
for directory_stud in sorted_alphanumeric(os.listdir(directory_programs)):
    # rollnumber is the name of the directory
    rollnumber = directory_stud
    print("rollnumber", rollnumber)
    # open student_programs/rollno/rps.cpp
    print("opening", directory_programs + "/" + rollnumber)
    for filename_stud in sorted_alphanumeric(os.listdir(directory_programs + '/' + directory_stud)):
        # compile rps.cpp to rps.out
        full_filename = ""
        if filename_stud.endswith('.cpp'):
            subprocess.call(['g++', directory_programs + '/' + directory_stud + '/' + filename_stud, '-o',
                             directory_programs + '/' + directory_stud + '/' + filename_stud[:-4] + '.out'])
            full_filename = directory_programs + '/' + directory_stud + '/' + filename_stud[:-4] + '.out'
            tot_ok = 0
            tot_notok = 0
            average = 0  # the weighted average, no longer required now
            tot_score = 0
            tot_num_states = 0
            count_test_cases = 0
            with open('results.csv', 'a') as csvfile:
                csvfile.write(rollnumber + ',')
                for filename in sorted_alphanumeric(os.listdir(directory)):
                    f = os.path.join(directory, filename)
                    # checking if it is a file
                    if os.path.isfile(f):
                        A, B = FST(), FST()
                        # open file for reading and parse it
                        num_states_A = 0
                        ok = 0
                        notok = 0
                        with open(f, 'r') as file:
                            # read the first line, gives the number of states in the FSM
                            num_states = int(file.readline())
                            num_states_A = num_states
                            for i in range(num_states):
                                # next lines will be of the type "R 1 2 2", then add a state using addState("R",1,2,1)
                                line = file.readline()
                                line = line.split()
                                A.addState(line[0], int(line[1]), int(line[2]), int(line[3]))
                        # run ./timeout -m 100000 -t 1 ./testprog < test_cases/test_case.txt 2>/dev/null
                        # and parse the output
                        output = subprocess.check_output(["./timeout", "-m", "100000", "-t", "1", full_filename],
                                                         stdin=open(f, "r"), stderr=open(os.devnull, "w"))
                        # if output is empty print TLE
                        if output == b'':
                            notok += 1
                            tot_notok += notok
                            tot_score += 0  # doesn't change
                            average *= tot_num_states
                            tot_num_states += num_states
                            average = average / tot_num_states
                            print("ERR!! - File:", filename, " Status= ", "TLE/MLE")
                            csvfile.write('0,')

                        else:
                            ok += 1
                            # parse this output
                            output = output.decode("utf-8")
                            # first line is the number of states
                            num_states = int(output.splitlines()[0])
                            for i in range(num_states):
                                # next lines will be of the type "R 1 2 2", then add a state using addState("R",1,2,1)
                                line = output.splitlines()[i + 1]
                                line = line.split()
                                B.addState(line[0], int(line[1]), int(line[2]), int(line[3]))
                            # compare the two FSMs
                            total_win = 0
                            run = 10000
                            total_runs = run * num_states_A
                            status = 1
                            for i in range(num_states_A):
                                ret = eval(A, B, i, 1, 10000)
                                total_win += ret[1]
                                status = ret[3]
                            # Scoring
                            if (status == 0):  # violating constraints
                                score = 0
                            else:
                                x = (total_win * 100) / total_runs
                                score = max(0, 2 * x - 100)
                            tot_score += score
                            count_test_cases += 1
                            csvfile.write(str(score) + ',')
                            average = (average * tot_num_states + score * num_states)
                            tot_num_states += num_states
                            average = average / tot_num_states
                            # take running average with weights as number of states

                            print("OK - File:", filename, " Score= ", score)
                            tot_ok += ok
                print("Total OK  : ", tot_ok)
                print("Total ERR : ", tot_notok)
                print("Weighted Average Score: ", average)
                print("Average Score: ", tot_score / count_test_cases)
                csvfile.write(str(average) + ',')
                csvfile.write(str(tot_score / count_test_cases) + ',')
                csvfile.write('\n')
