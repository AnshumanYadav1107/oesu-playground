from textkit.words import word_count, reverse_words


def test_word_count_simple_sentence():
    assert word_count("open source is fun") == 4


def test_word_count_empty_string():
    assert word_count("") == 0


def test_reverse_words():
    assert reverse_words("one two three") == "three two one"


# TODO: there are no tests for title_case yet. Want to add some?
