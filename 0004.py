import re
from collections import Counter

# FILESOURCE = 'words.txt'
#
# pattern = r'[A-Za-z]+'
# with open(FILESOURCE) as f:
#     r = re.findall(pattern, f.read())
#     print Counter(r).most_common()
words = re.findall(r'[A-Za-z]+', open('words.txt').read().lower())
print type(words)
print Counter(words).most_common(10)