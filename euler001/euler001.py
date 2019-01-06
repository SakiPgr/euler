#!/usr/bin/env python3

# my solution to the problem
sum = 0

for i in range(1, 1000): 
    if i % 3 == 0 or i % 5 == 0:
        sum += i

# and my try on a python list comprehension
# sum = sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])

print(sum)

