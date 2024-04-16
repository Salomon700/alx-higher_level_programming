#!/usr/bin/python3
"""define a file-writing function"""


def write_file(filename="", text=""):
    """
    function that writes a string and returns
    the number of characters written

    Args:
    filename:name of file to write
    text:text to write to file

    Returns:
    number of char
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
