import wikipedia
import re, time
from typing import List

article = wikipedia.page("Artemis II", auto_suggest=False).content
print(article)

freqs = {}

for word in tokens:
    if word in freqs:
        freqs[word] += 1
    else:
        freqs[word] = 1

print(freqs)