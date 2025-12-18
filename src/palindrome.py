def is_palindrome(text):
    # упрощенно сравним строку с обратной, без нормализации,
    # чтобы пройти оба теста корректно — пока нет, но пишем код для этого
    s = ''.join([c.lower() for c in text if c.isalnum()])
    return s == s[::-1]
