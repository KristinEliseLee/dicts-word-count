import sys
import collections


def remove_punctuation(word):
    """Takes a word and removes non alpha characters from beginning and ending
    as well as uncapitalizes any letters"""
    if word.isalpha():
        return word.lower()
    else:
        if word[0].isalpha() is False:
            word = word[1:]
        if len(word) > 0:
            if word[-1].isalpha() is False:
                word = word[:-1]
        return word.lower()


def get_word_count(filepath):
    """Takes a file path and returns a dictionary of how many times each space
    separated word occurs
    """
    word_count = collections.Counter()
    with open(filepath) as file:
        for line in file:
            line = line.rstrip()
            words = line.split()
            for index in range(len(words)):
                words[index] = remove_punctuation(words[index])
            word_count.update(words)

    return word_count


def print_word_count(count_dictionary):
    """Takes a dictionary and prints how many times each space separated word
    occurs in dictionary
    """

    for word in count_dictionary:
        print(f"{word} {count_dictionary[word]}")


def print_sorted_word_count(count_dictionary):
    """Takes a dictionary and prints key value pairs sorted by word count and
    then alphabetically
    """

    word_tuples = list(count_dictionary.items())
    word_tuples.sort()
    word_tuples.sort(key=lambda word: word[1], reverse=True)
    for word, count in word_tuples:
        print(f"{word} {count}")


print_sorted_word_count(get_word_count(sys.argv[1]))
