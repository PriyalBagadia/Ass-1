# Write a Python program to count the frequency of words in a file.

from collections import Counter
import re

def count_word_frequency(file_path):
    word_counter = Counter()
    
    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            word_counter.update(words)
    
    return word_counter

file_path = 'example.txt'

word_frequencies = count_word_frequency(file_path)

for word, frequency in word_frequencies.items():
    print(f'{word}: {frequency}')
