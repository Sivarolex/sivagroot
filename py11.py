import re
from collections import Counter


text = input("Enter word: ")
words = re.findall(r'\w+',text.lower())
words_count = Counter(words)
most_common = max(words_count,key = words_count.get())
print(words_count)