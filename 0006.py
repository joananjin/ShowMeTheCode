import os
import re
from collections import Counter

if __name__ == '__main__':
    for filename in os.listdir('./texts'):
        if not filename.startswith('.'):
            text = open('./texts/' + filename, 'r')
            words = re.findall(r'[A-Za-z]+', text.read())
            words = Counter(words)
            stop_words = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 's', 'is', 'are', 'a', 'with', 'as', 'an',
                          'was', 'were']
            for i in stop_words:
                words[i] = 0
            print Counter(words).most_common()[0][0]
