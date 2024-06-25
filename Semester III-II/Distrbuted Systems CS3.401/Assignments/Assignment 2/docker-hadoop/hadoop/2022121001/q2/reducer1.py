#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

current_pair = None
mutual_friends = []

for line in sys.stdin:
    pair_str, mutual_friend = line.strip().split('\t')

    if pair_str == current_pair:
        mutual_friends.append(mutual_friend)
    else:
        if current_pair:
            mutual_friends = sorted(mutual_friends)
            current_pair = current_pair.replace(',', '').strip('[]')
            print(f'{current_pair}\t{" ".join(mutual_friends)}')
        current_pair = pair_str
        mutual_friends = [mutual_friend]

# Don't forget to output the last pair if needed!
if current_pair == pair_str:
    mutual_friends = sorted(mutual_friends)
    current_pair = current_pair.replace(',', '').strip('[]')
    print(f'{current_pair}\t{" ".join(mutual_friends)}')
