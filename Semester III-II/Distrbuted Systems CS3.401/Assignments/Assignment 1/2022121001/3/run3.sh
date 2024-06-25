
#!/bin/bash
for i in {1..4}
do
    for j in {1..5}
    do
        echo "Running 3.py with $i processes on ../test_cases/3/$j.in"
        # mpirun -np $i ./a.out < ../test_cases/3/$j.in > $j.out
        mpirun -np $i --use-hwthread-cpus --oversubscribe python3 GoL.py < ../test_cases/3/$j.in > $j.out
        diff $j.out ../test_cases/3/$j.out > $j.diff
    done
done