
#!/bin/bash
mpic++ 1B.cpp
for i in {1..12}
do
    for j in {1..6}
    do
        mpirun -np $i ./a.out < ../test_cases/1B/$j.in > $j.out
        diff $j.out ../test_cases/1B/$j.out
    done
done