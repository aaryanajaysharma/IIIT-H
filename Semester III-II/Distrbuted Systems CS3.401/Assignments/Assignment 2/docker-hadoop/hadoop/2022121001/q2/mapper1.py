#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

for line in sys.stdin:
    line_check = line.strip()
    if '\t' not in line_check:
        continue
    person, friends = line.strip().split('\t')
    person = int(person)
    friends = friends.split(',')
    friends = [int(f) for f in friends]
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            # convert int to str to avoid TypeError: unhashable type: 'list'
            print(f'{str(sorted([friends[i], friends[j]]))}\t{person}')
