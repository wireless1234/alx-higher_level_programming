#!/usr/bin/python3
"""
This module contains one function
"""


def write_file(filename="", text=""):
    """
    This function writes into a file
    """
    with open(myfilename, 'w', encoding='UTF-8') as f:
        f.write(text)
