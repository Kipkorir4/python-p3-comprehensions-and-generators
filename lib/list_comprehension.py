#!/usr/bin/env python3

def return_evens(num_list):
    return [i for i in num_list if i % 2 == 0]

# print(return_evens([1, 87, 34, 65, 78, 99]))
    

def make_exclamation(sentence_list):
   return [i+"!" for i in sentence_list]

# make_exclamation(["a", "b", "c"])