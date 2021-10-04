"""Count words in file."""


# put your code here.
def word_count(filename):

    word_counts = {}

    file = open(filename)
    for line in file:
        words = line.strip().split(" ")
        for word in words: 
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

    

print(word_count("twain.txt"))