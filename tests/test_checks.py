from textkit.checks import is_palindrome


def test_palindrome_true():
    assert is_palindrome("level")


def test_palindrome_false():
    assert not is_palindrome("python")


def test_palindrome_with_spaces():
    assert is_palindrome("nurses run")


# TODO: is_anagram has no tests at all.
