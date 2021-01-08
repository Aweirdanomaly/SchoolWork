# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:50:22 2019

@author: Carlos
"""
import math 


def clean_text(txt):
    """Takes in a string 'txt' and returns it without punctuation marks """
    s = []
    for x in txt:
        if x in ',."-?!/\*`~<>:;' :
            s += x
        elif x in "'":
            s += x
    for x in s:
        txt = txt.replace(x, '')
    txt = txt.lower()
    return txt.split()

def stem(s):
    """ Takes in 1-word string 's' and returns the stem of that string """
    if s[:3] == 'pre':
        return s[3:]
    elif s[-3:] == 'ing':
        return s[:-3]
    elif s[-3:] == 'ers':
        return s[:-3]    
    elif s[-2:] == 'er':
        return s[:-2]
    elif s[-2:] == 'es':
        return s[:-2] 
    elif s[-1] == 's':
        return s[:-1]
    elif s[:3] == 'anti':
        return s[4:]
    elif s[-2:] == 'en':
        return s[:-2] 
    else:
        return s
    
def compare_dictionaries(d1, d2):
    """ takes in 2 dictionaries 'd1' and 'd2' and returns their similarity score """
    score = 0
    total = 0
    for s in d1:
        total += d1[s]
    for s in d2:
        if s in d1:
            score += d2[s]*math.log(d1[s]/total) 
        else:
            score += d2[s]*math.log(.5/total)
    return score

def run_tests():
    """ tests the final project on several TextModels """
    source1 = TextModel('Bee Movie')
    source1.add_file('Bee Movie Script.txt')

    source2 = TextModel('Bible')
    source2.add_file('Bible.txt')

    new1 = TextModel('Shrek')
    new1.add_file('Shrek Script.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel("Qur'an Excerpt")
    new2.add_file("Qur'an Excerpt.txt")
    new2.classify(source1, source2)
    
    new3 = TextModel("Bee Movie Ending")
    new3.add_file("Bee Movie Ending.txt")
    new3.classify(source1, source2)
    
    new4 = TextModel("Bible Excerpt")
    new4.add_file("Bible Excerpt.txt")
    new4.classify(source1, source2)


class TextModel:
    """A class that stores the frequency and length of words in an object
    and prints those values """
    def __init__(self, model_name):
        """ constructor that initializes the three attributes  
            in every TextModel object, name, words, and word_lengths """

        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.commas = {}
        
    def __repr__(self):
        """ Return a string representation of the TextModel"""
        return('text model name: '+ self.name + '\n' + '  number of words: ' + str(len(self.words)) + '\n' + '  number of word lengths: ' + str(len(self.word_lengths))\
               + '\n' + '  number of stems: ' + str(len(self.stems)) + '\n' + '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n' + '  number of comma amounts per sentence: ' + str(len(self.commas)))
        
    def add_string(self, s):
        """Analyzes the string 's' and adds its pieces
        to all of the dictionaries in this text model.
        """
        c = s.split()
        v = 0
        p = 0
        for u in c: 
            if ',' in u:
                p += 1
            v += 1
            if '.' in u or '?' in u or '!' in u:
                if v in self.sentence_lengths:
                    self.sentence_lengths[v] += 1
                else:
                    self.sentence_lengths[v] = 1
                    
                if p in self.commas:
                    self.commas[p] += 1
                else:
                    self.commas[p] = 1
                v = 0
                p = 0
            
        word_list = clean_text(s)
        
        for w in word_list:

            if w in self.words:
                self.words[w] += 1
            else:
                self.words[w] = 1
                
            if len(w) in self.word_lengths:
                self.word_lengths[len(w)] += 1
            else:
                self.word_lengths[len(w)] = 1
            
            a = stem(w)
            if a in self.stems:
                self.stems[a] += 1
            else:
                self.stems[a] = 1
            
            
    def add_file(self, filename):
        """ take in a file 'filename' and a TextModel object 'self' and add
        'filemame' to 'self' via the add_string method """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        self.add_string(text)
        f.close()
        
    def save_model(self):
        """ take in TextModel object 'self' and write five files each with
        one with a 'self' attribute in it """
        file = open(self.name + '_words', 'w')
        file.write(str(self.words))
        file.close()
        
        file = open(self.name + '_word_lengths', 'w')
        file.write(str(self.word_lengths))
        file.close()
        
        file = open(self.name + '_stems', 'w')
        file.write(str(self.stems))
        file.close()
        
        file = open(self.name + '_sentence_lengths', 'w')
        file.write(str(self.sentence_lengths))
        file.close()
        
        file = open(self.name + '_commas', 'w')
        file.write(str(self.commas))
        file.close()

    def read_model(self):
        """ take in TextModel object 'self' and read two files with its 
        attributes within them. Then, assign 'self' those attributes """
        f = open(self.name + '_words', 'r')    
        d_str = f.read()           
        f.close()
        d = dict(eval(d_str))     
        self.words = d
        
        f = open(self.name + '_word_lengths', 'r')    
        d_str = f.read()           
        f.close()
        d = dict(eval(d_str)) 
        self.word_lengths = d
        
        f = open(self.name + '_stems', 'r')    
        d_str = f.read()           
        f.close()
        d = dict(eval(d_str))     
        self.stems = d
        
        f = open(self.name + '_sentence_lengths', 'r')    
        d_str = f.read()           
        f.close()
        d = dict(eval(d_str))     
        self.sentence_lengths = d
        
        f = open(self.name + '_commas', 'r')    
        d_str = f.read()           
        f.close()
        d = dict(eval(d_str))     
        self.commas = d
        
    def similarity_scores(self, other):
        """ computes and returns a list of log similarity scores measuring the similarity of self and other """
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        commas_score = compare_dictionaries(other.commas, self.commas)
        return [word_score, word_lengths_score, stems_score, sentence_lengths_score, commas_score]
    
    def classify(self, source1, source2):
        """ compares TextModel object (self) to two other TextModel
        objects 'source1' and 'source2' and determines which of these other 
        TextModels is the more likely source of the called TextModel """
        one = 0
        two = 0
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ' + source1.name + ':' + str(scores1) + '\n' + 'scores for ' + source2.name + ':' + str(scores2) )
        for n in range(len(scores1)):
            if scores1[n] > scores2[n]:
                one += 1
            elif scores2[n] > scores1[n]:
                two += 1
            if one > two:
                winner = source1.name
            elif two > one:
                winner = source2.name
            else:
                winner = "either one"

        print(self.name + ' is more likely to have come from ' + winner)
        
def test():
    """ tests the TextModel implementation """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

        