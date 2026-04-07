import re

def count_words(text: str) -> int:
    """Count total number of words in a string."""
    return len(re.findall(r'\b\w+\b', text))

def count_sentences(text: str) -> int:
    """Count total number of sentences in a string."""
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def unique_words(text: str) -> set:
    """Return a set of unique words in a string."""
    words = re.findall(r'\b\w+\b', text.lower())
    return set(words)