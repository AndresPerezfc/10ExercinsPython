import re
from collections import Counter


def count_words(sentence):
    return Counter(word.lower() for word in re.compile("[0-9a-zA-Z]+(?:'[0-9a-zA-Z]+)?").findall(sentence))
