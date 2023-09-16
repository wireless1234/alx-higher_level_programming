#!/usr/bin/python3
"""
Module doctring
"""
def read_file(filename=""):
	with open(filename) as f:
		for line in f:
			print(line, end='')
