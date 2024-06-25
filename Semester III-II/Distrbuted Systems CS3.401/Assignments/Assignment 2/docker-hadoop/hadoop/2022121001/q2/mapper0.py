#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

for line in sys.stdin:
    person, friend = line.strip().split()
    print(f'{person}\t{friend}')
    print(f'{friend}\t{person}')  # Ensure the friendship is bidirectional

