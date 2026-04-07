from text_stats_calculator import count_words, count_sentences, unique_words

# Тестируем подсчёт слов
assert count_words("Hello world!") == 2
assert count_words("") == 0
assert count_words("One") == 1

# Тестируем подсчёт предложений
assert count_sentences("Hello! How are you? Fine.") == 3
assert count_sentences("") == 0
assert count_sentences("Just one sentence.") == 1

# Тестируем уникальные слова
assert len(unique_words("Hello hello world")) == 2
assert len(unique_words("")) == 0
assert len(unique_words("A a A")) == 1