#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

current_key = None
mutual_friends = []

for line in sys.stdin:
    key, value = line.strip().split('\t')
    
    if key == current_key:
        # If the key hasn't changed, add the value to the list of mutual friends
        if value not in mutual_friends:
            mutual_friends.append(value)
    else:
        # If the key has changed (and it's not the first key), print the previous key and its mutual friends
        if current_key:
            print(f'{current_key}\t{" ".join(sorted(mutual_friends, key=int))}')
        current_key = key
        mutual_friends = [value]

# Don't forget to output the last key if needed!
if current_key == key:
    print(f'{current_key}\t{" ".join(sorted(mutual_friends, key=int))}')

