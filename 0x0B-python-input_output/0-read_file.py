#!/usr/bin/python3

def read_file(filename=""):
    """print contents of a file to stdout"""
    with open('my_file_0.txt', encoding = 'utf-8') as f:
        print(f.read(), end= " ")
