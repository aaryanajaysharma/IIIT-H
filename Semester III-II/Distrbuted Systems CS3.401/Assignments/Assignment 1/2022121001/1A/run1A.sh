
#!/bin/bash
for i in {1..12}
do
    for j in {1..5}
    do
        mpirun -np $i --use-hwthread-cpus --oversubscribe python3 1A.py < ../test_cases/1A/$j.in > $j.out
        diff $j.out ../test_cases/1A/$j.out > $j.diff
    done
done