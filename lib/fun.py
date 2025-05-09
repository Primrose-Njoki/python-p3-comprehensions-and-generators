squared_minus_one = list()
for n in range(2,8):
    squared_minus_one.append((n ** 2) -1)

print(squared_minus_one)
pass

squared_minus_one=[(n**2)-1  for n in range(2,8)]
print (squared_minus_one)

one_to_three =range(1,5)
squared_lc=[n**2 for n in one_to_three]
print(squared_lc)

import sys 

list_comprehension =[n for n in range(100000)]
generator_expression = (n for n in range(100000))
sys.getsizeof(generator_expression)
sys.getsizeof(list_comprehension)
