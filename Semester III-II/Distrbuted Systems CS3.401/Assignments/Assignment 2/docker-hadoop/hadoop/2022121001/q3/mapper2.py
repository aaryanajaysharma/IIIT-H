#!/usr/bin/python3
# -*-coding:utf-8 -*

# Mapper script for filtering nodes based on distance threshold
import sys

def filter_nodes_based_on_distance(input_text):
    parts = input_text.strip().split('\t')
    node_identifier = parts[0]
    distance_value = int(parts[1])

    # Emit node if its distance is within the specified threshold
    if distance_value <= 10:
        print(f"{node_identifier}\t{distance_value}")

def process_input():
    for line in sys.stdin:
        filter_nodes_based_on_distance(line)

if __name__ == "__main__":
    process_input()
