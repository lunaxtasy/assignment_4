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

    assert is_palindrome("") is False

def test_a_is_a_palindrome():
    """
    `(/1)` `is_palindrome` returns `True` if called with `"a"`.
    """

    assert is_palindrome("a") is True

def test_bb_is_a_palindrome():
    """
    `(/1)` `is_palindrome` returns `True` if called with `"bb"`.
    """

    assert is_palindrome("bb") is True

def test_abc_is_not_a_palindrome():
    """
    `(/1)` `is_palindrome` returns `False` is called with `"abc"`.
    """

    assert is_palindrome("abc") is False

def test_laval_is_a_palindrome():
    """
    `(/1)` `is_palindrome` returns `True` when called with `"laval"`.
    """

    assert is_palindrome("laval") is True

def test_toronto_is_not_a_palindrome():
    """
    `(/1)` `is_palindrome` returns `False` when called with `"toronto"`.
    """

    assert is_palindrome("toronto") is False
