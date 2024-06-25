#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

for line in sys.stdin:
    # Supprimer les espaces
    line = line.strip()
    # recupérer les mots
    words = line.split()

    # operation map, pour chaque mot, generer la paire (mot, 1)
    for word in words:
        print("%s\t%d" % (word, 1))
