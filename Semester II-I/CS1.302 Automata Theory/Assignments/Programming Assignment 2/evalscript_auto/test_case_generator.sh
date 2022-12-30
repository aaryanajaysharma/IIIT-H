#!/bin/sh
# This script is used to generate test_cases, which will be added to test_cases folder 
# and will be used to test the correctness of the program.
for i in `seq 1 1000`
do
    # generate a random number between 1 and 30
    # use the shuf command to generate a random number
    number=`gshuf -i 1-30 -n 1`
    # create a file with name test_case_$i.txt inside the folder test_cases
    filename="test_cases/test_case_$i.txt"
    rm -f filename
    touch $filename
    # write the random number into the file
    echo $number > $filename
    # next, we append lines to the file of the form "R/P/S i j k" where i, j, k are random numbers between 1 and 3
    for j in `seq 1 $number`
    do
        # generate a random number between 1 and 3
        a=$(($RANDOM % $number + 1))
        b=$(($RANDOM % $number + 1))
        c=$(($RANDOM % $number + 1))
        # append the line to the file
        # choose a random letter between R/P/S
        letter=$((RANDOM % 3 + 1))
        if [ $letter -eq 1 ]
        then
            echo "R $a $b $c" >> $filename
        elif [ $letter -eq 2 ]
        then
            echo "P $a $b $c" >> $filename 
        else
            echo "S $a $b $c" >> $filename 
        fi
    done
done
echo "Done"
