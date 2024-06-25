#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

for line in sys.stdin:
    # Split the line into a list of friends
    u, v = line.strip().split()
    u, v = sorted([u, v], key=int)  # Ensure the smaller number comes first for consistency
    
    # Emit both directions of the friendship
    print(f'{u} {v}\t{v}')
    print(f'{v} {u}\t{u}')

