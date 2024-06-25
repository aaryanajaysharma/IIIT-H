
#!/bin/bash
for i in {1..12}
do
    for j in {1..7}
    do
        # mpirun -np $i ./a.out < ../test_cases/2/$j.in > $j.out
        mpirun -np $i --use-hwthread-cpus --oversubscribe python3 2.py < ../test_cases/2/$j.in > $j.out
        diff $j.out ../test_cases/2/$j.out > $j.diff
    done
done