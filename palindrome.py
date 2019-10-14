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

    #determines if string is empty or just a white space, sets logic to False

    if not word.strip():
        palin_answer = False

    #creating deque, also eliminating possibility of case-in-middle_of_word issue

    characters = deque(word.lower())

    #checking deque length, lengths of 1 are palindromes by their nature, either
    # as one letter or the middle letter.
    #Lengths of greater than or equal to 2 require matching

    if len(characters) == 1:
        palin_answer = True
    else:
        while len(characters) > 1:
            #pop first and last characters in string and compare. True if they match
            beginning = characters.popleft()
            end = characters.pop()

            #logic for determining palindrome
            palin_answer = bool(beginning == end)

    return palin_answer
