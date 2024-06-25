#!/usr/bin/python3
# -*-coding:utf-8 -*

# Mapper script for graph distance updates
import sys

def parse_and_emit(line):
    parts = line.strip().split('\t')
    node_id = parts[0]
    current_distance = int(parts[1])
    links = parts[2] if len(parts) > 2 else None

    # Emit the node with its current distance
    print(f"{node_id}\t{current_distance}\t{'' if links is None else links}")

    # If there are links, process each neighbor
    if links:
        for link in links.split(' '):
            adjacent, dist = link.split(':', 1)
            new_distance = current_distance + int(dist)
            print(f"{adjacent}\t{new_distance}")

def main():
    for input_line in sys.stdin:
        parse_and_emit(input_line)

if __name__ == "__main__":
    main()
