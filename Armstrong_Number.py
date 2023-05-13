#You are given an integer ‘NUM’ . Your task is to find out whether this number is an Armstrong number or not.
#A k-digit number ‘NUM’ is an Armstrong number if and only if the k-th power of each digit sums to ‘NUM’.
#from os import *
#from sys import *
#from collections import *
#from math import *

def isArmstrong(num):
    sum = 0
    for i in repr(num):
        sum = sum + (int(i)**len(repr(num)))
        
    if num == sum:
        return True
    else:
        return False
    pass
num = int(input())
print(isArmstrong(num))
 