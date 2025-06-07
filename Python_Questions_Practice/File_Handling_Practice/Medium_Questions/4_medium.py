# Write a function that accepts a filename and a word, and returns the number of times the word appears in the file.

def count_word_in_file(filename, word):
    count = 0

    with open(filename, "r") as file:
        for line in file:
            line = line.lower()
            count += line.count(word.lower())
    return count

filename = "Text files/error.txt"
word = "error"
print(count_word_in_file(filename, word))