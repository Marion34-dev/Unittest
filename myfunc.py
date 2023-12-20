def cap_text(text):
    return text.title()


def add_numbers(a, b):
    return a + b


def find_max_length_word(sentence):
    words = sentence.split()
    if not words:
        return None
    return max(words, key=len)     # key=len specifies that length of each word should be used for comparison

