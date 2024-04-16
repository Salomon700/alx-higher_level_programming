#!/usr/bin/python3
"""define a file-appending function"""


def append_write(filename="", text=""):
    """
    function that appends a string to a text file and returns
       the number of characters

       Args:
           filename(str): name of file to append to
           text(str):string to append to file.
       Returns:
            number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
