#!/usr/bin/env python3

def return_evens(num_list):
   return[ x for x in num_list if x % 2 ==0]

num_list = [0,1,3,5,7,9]
evens = return_evens(num_list)
print(evens)


def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]

sentence_list = ["Hello", "I'm doing great", "Python is fun"]
exclaimed_sentences = make_exclamation(sentence_list)
print(exclaimed_sentences)