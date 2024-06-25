#!/usr/bin/python3
# -*-coding:utf-8 -*

# Reducer script for updating node distances and paths
import sys

def emit_node_info(node, dist, paths):
    print(f"{node}\t{dist}\t{paths}")

def update_node_distance_and_path():
    prev_node = None
    min_distance = None
    path_info = None

    for line in sys.stdin:
        parts = line.strip().split('\t')
        node_id, distance = parts[0], int(parts[1])
        paths = parts[2] if len(parts) > 2 else None

        if node_id != prev_node:
            if prev_node is not None:
                emit_node_info(prev_node, min_distance, path_info)

            prev_node, min_distance, path_info = node_id, distance, paths
        else:
            if distance < min_distance:
                min_distance = distance
            if paths is not None and paths != '0':
                path_info = paths

    if prev_node is not None:
        emit_node_info(prev_node, min_distance, path_info)

if __name__ == '__main__':
    update_node_distance_and_path()
