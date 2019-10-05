#!/usr/bin/python3
"""
    This module contains a function text indententation
"""


def text_indentation(text):
    """This function function indent a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text.replace("?", "?\n\n")
    new_text = new_text.replace(".", ".\n\n")
    new_text = new_text.replace(":", ":\n\n")
    print("\n".join([i.strip() for i in new_text.split("\n")]), end="")
