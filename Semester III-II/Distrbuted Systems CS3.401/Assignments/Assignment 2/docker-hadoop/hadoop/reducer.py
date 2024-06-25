#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

current_word = None
current_docs = set()

# Process each line output from the mapper.
for line in sys.stdin:
    word, doc_id = line.strip().split('\t', 1)

    # Check if the word has changed (since input is sorted by key).
    if current_word == word:
        # If the word is the same, add the doc_id to the set (to ensure uniqueness).
        current_docs.add(doc_id)
    else:
        # If the word has changed (and it's not the first word), print the current word and its doc IDs.
        if current_word is not None:
            print(f'{current_word}\t{" ".join(sorted(current_docs))}')
        current_word = word
        current_docs = {doc_id}

    # Don't forget to output the last word if needed!
    if current_word == word:
        print(f'{current_word}\t{" ".join(sorted(current_docs))}')
