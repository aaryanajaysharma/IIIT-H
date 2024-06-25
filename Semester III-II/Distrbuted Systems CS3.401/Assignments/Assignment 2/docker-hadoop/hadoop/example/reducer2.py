#!/usr/bin/python3
# -*-coding:utf-8 -*

# Simple passthrough reducer script for data formatting
import sys

def process_and_emit(input_line):
    cleaned_line = input_line.strip()
    print(cleaned_line)

def main():
    for line in sys.stdin:
        process_and_emit(line)

if __name__ == "__main__":
    main()
