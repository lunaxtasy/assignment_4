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

    #checks length of deque, returns False for no characters in string

    if len(deque(word)) < 1:
        palin_answer = False

    return palin_answer
