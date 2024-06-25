#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

# Process each line input.
for line in sys.stdin:
    # Split the line into document ID and text.
    doc_id, text = line.strip().split('\t', 1)  # Ensure you're using the correct tab character here.
    words = text.split()
    for word in words:
        # Emit the word and the document ID.
        print(f'{word}\t{doc_id}')
