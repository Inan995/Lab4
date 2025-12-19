def is_palindrome(text):
    """
    Проверяет, является ли строка палиндромом.
    Игнорирует регистр, пробелы и знаки препинания.
    """
    filtered = []
    for ch in text.lower():
        if ch.isalnum():
            filtered.append(ch)
    normalized = ''.join(filtered)
    return normalized == normalized[::-1]

