#!/usr/bin/env python3

def return_evens(num_list):
    return[num for num in num_list if num %2==0]
numbers=[0,1,3,5,7,8,9]
even_numbers=return_evens(numbers)
print(even_numbers)
pass

def make_exclamation(sentence_list):
    return [sentence +'!' for sentence in sentence_list]
print(make_exclamation(['Hey cate', 'Are you good', 'Am good']))
pass