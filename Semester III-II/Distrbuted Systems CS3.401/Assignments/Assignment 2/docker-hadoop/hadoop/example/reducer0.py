#!/usr/bin/python3
# -*-coding:utf-8 -*

# Initial graph node distance setting for shortest path calculation
import sys

INITIAL_DISTANCE = 200000
SOURCE = 1

def process_line(line):
    parts = line.strip().split('\t')
    node_id, connections = parts[0], parts[1]
    distance = 0 if int(node_id) == SOURCE else INITIAL_DISTANCE

    # Generate adjacency list representation
    adjacency_representation = ['{neighbor}:1'.format(neighbor=n) for n in connections.split(',')]

    print(f"{node_id}\t{distance}\t{' '.join(adjacency_representation)}")

def main():
    for line in sys.stdin:
        process_line(line)

if __name__ == "__main__":
    main()
