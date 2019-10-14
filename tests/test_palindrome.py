"""
Assignment 4: Palindrome Checker

The test module for the palindrome checker
"""

import pytest
from palindrome import is_palindrome

def test_is_string():
    """
    Test Requirement: `is_palindrome` raises a `ValueError` when not provided with a value
      that is  an instance of `str`.
    """

    with pytest.raises(ValueError):
        is_palindrome(1881)

def test_empty_string():
    """
    `(/1)` `is_palindrome` returns `False` when called with an empty string.
    """

    assert is_palindrome("") is None
    assert is_palindrome(" ") is None
