"""
Assignment 4: Palindrome checker

Palindrome checker main module
"""

from collections import deque

def is_palindrome(word):
    """
    This function checks to see if an entered string is a palindrome or not.

    Returns True for palindromes and False for non-palindromes and empty strings
    """

    #string checker, will raise ValueError if anything else but a string

    if isinstance(word, str) is False:
        raise ValueError

    #if string isn't empty, determines if entry is palindrome

    if not word.strip():
        palin_answer = False

    #creating deque

    characters = deque(word)

    #checking deque length, lengths of 1 are palindromes. Lengths of greater than 2 require matching

    if len(characters) == 1:
        palin_answer = True
    else:
        while len(characters) > 1:
            #pop first and last characters in string and compare. True if they match
            beginning = characters.popleft()
            end = characters.pop()

            if beginning == end:
                palin_answer = True
            else:
                palin_answer = False

    return palin_answer
