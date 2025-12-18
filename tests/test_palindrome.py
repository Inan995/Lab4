from src.palindrome import is_palindrome

def test_palindrome_simple():
    # Проверяем палиндром: "А роза упала на лапу Азора"
    assert is_palindrome("А роза упала на лапу Азора") is True

def test_not_palindrome():
    assert is_palindrome("Не палиндром") is False
