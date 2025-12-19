from src.palindrome import is_palindrome

def test_palindrome_simple():
    assert is_palindrome("А роза упала на лапу Азора") is True

def test_not_palindrome():
    assert is_palindrome("Это не палиндром") is False

def test_ignore_spaces_and_punctuation():
    assert is_palindrome("А роза, упала на лапу Азора!") is True

def test_empty_and_one_char():
    assert is_palindrome("") is True
    assert is_palindrome("x") is True

