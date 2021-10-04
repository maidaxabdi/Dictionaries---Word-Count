"""Count words in file."""

import sys
# put your code here.
def word_count(file_name):

    word_counts = {}

    file = open(file_name)
    for line in file:
        words = line.strip().split(" ")
        for word in words: 
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def tokenize(file_name):
    new_list = []
    file = open(file_name)
    for line in file:
        words = line.strip().split(" ")
        new_list.append(words)
    
    return new_list

def count_words(words):
    word_counts = {}
    for word in words: 
        print(word)
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts

def print_word_counts(word_counts):
    return word_counts.items()

print(tokenize("test.txt"))
print(count_words(["apple", "berry", "cherry", "apple"]))
print(print_word_counts({'apple': 2, 'berry': 1, 'cherry': 1}))