#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.
     >>> text_indentation("Hello. How are you? Good: I hope!")
    Hello.
    <BLANKLINE>
    How are you?
    <BLANKLINE>
    Good:
    <BLANKLINE>
    I hope!
    >>> text_indentation(123)
    Traceback (most recent call last):
        ...

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".:?":
        text = text.replace(char, "{}\n\n".format(char))
    print("\n".join([line.strip() for line in text.split("\n")]))

