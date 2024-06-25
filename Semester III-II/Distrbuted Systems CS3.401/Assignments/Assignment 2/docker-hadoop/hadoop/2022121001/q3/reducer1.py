#!/usr/bin/python3
# Script for processing graph nodes with updated distances
import sys

def print_node_details(identifier, distance, adjacency):
    # Printing node information in a tab-separated format
    print(f"{identifier}\t{distance}\t{adjacency if adjacency else ''}")

def process_input_for_nodes():
    current_node = None
    lowest_distance = float('inf')
    adjacency_info = None

    for input_line in sys.stdin:
        elements = input_line.strip().split('\t')
        node, new_distance = elements[0], int(elements[1])
        adjacency = elements[2] if len(elements) > 2 else None

        # Check if we're still processing the same node
        if node != current_node:
            # Emit details for the previous node
            if current_node is not None:
                print_node_details(current_node, lowest_distance, adjacency_info)
            current_node, lowest_distance, adjacency_info = node, new_distance, adjacency
        else:
            # Update details if this is a shorter distance or new adjacency info
            lowest_distance = min(lowest_distance, new_distance)
            if adjacency and adjacency != '0':
                adjacency_info = adjacency

    # Emit details for the last node in the input
    if current_node is not None:
        print_node_details(current_node, lowest_distance, adjacency_info)

if __name__ == "__main__":
    process_input_for_nodes()
