#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

current_person = None
friends_list = []

for line in sys.stdin:
    person, friend = line.strip().split('\t')

    if person == current_person:
        friends_list.append(friend)
    else:
        if current_person:
            print(f'{current_person}\t{",".join(friends_list)}')
        current_person = person
        friends_list = [friend]

# Don't forget to output the last person's friends list
if current_person == person:
    print(f'{current_person}\t{",".join(friends_list)}')

