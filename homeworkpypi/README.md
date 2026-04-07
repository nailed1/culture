# Text Stats Calculator

A simple package to calculate word/sentence counts and unique words from a given text.

## Installation

```bash
pip install text-stats-calculator
```

## Usage

```python
from text_stats_calculator import count_words, count_sentences, unique_words

text = "Hello world! How are you?"
print(count_words(text))        # 5
print(count_sentences(text))    # 2
print(unique_words(text))       # {'hello', 'world', 'how', 'are', 'you'}
```

## Functions

- `count_words(text)` - Count total number of words in a string
- `count_sentences(text)` - Count total number of sentences in a string
- `unique_words(text)` - Return a set of unique words in a string

## License

MIT
