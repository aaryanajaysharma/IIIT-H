#!/usr/bin/python3
# -*-coding:utf-8 -*

# Simplified mapper script for processing graph data
import sys

def process_line(input_line):
    elements = input_line.strip().split()
    if len(elements) > 1:
        key_node = elements[0]
        adjacent_nodes = ','.join(elements[1:])
        output = f"{key_node}\t{adjacent_nodes}"
        print(output)

def main():
    for line in sys.stdin:
        process_line(line)

if __name__ == "__main__":
    main()
