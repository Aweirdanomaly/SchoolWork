#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
import random
def create_dictionary(filename):
    """ takes in string 'filename' and returns Markov dictionary"""
    file = open(filename, 'r')
    text = file.read()
    words = text.split()
    d = {}
    current_word = '$'
    for next_word in words:
        if '.' in current_word or '?' in current_word or '!' in current_word:
            current_word = '$'
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]
        current_word = next_word
    return d
    
def generate_text(word_dict, num_words):
    """ takes in dictionary 'word_dict' and a positive integer 'num_words' 
    and returns a sentence using the Markov algorithm that is 'num_words' long"""
    current_word = '$'
    for x in range(num_words):
        if '.' in current_word or '?' in current_word or '!' in current_word:
            current_word = '$'
        wordlist = word_dict[current_word]
        next_word = random.choice(wordlist)
        print(next_word,end = ' ')
        current_word = next_word
    print()
        
