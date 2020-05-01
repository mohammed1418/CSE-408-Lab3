# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:50:10 2020

@author: hp
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter a positive integer: "))
total = 0
for i in range(num):
    total += fibonacci(i)
print("Sum of first", num, "fibonacci integers is", total)