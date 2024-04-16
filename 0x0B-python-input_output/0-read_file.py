#!/usr/bin/python3
"""define a textx file-reading function"""


def read_file(filename=""):
    """print contents of a file to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end=" ")
