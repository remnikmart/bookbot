from collections import Counter

def get_num_chars(text: str) -> dict:
    return Counter(text.lower())

def get_num_words(text: str) -> int:
    return sum(1 for l in text.splitlines() for w in l.split(" ") if w)
