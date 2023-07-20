#Given an array that might contain duplicate elements, find the maximum possible distance between occurrences of two repeating elements i.e. elements having the same value. 
# If there are no duplicate elements in the array, return 0.
from os import *
from sys import *
from collections import *
from math import *

def maxDistance(arr, n): 
      
    mp = {} 
  
    maxDict = 0
    for i in range(n): 
  
        if arr[i] not in mp.keys(): 
            mp[arr[i]] = i 
  
        else: 
            maxDict = max(maxDict, i-mp[arr[i]]) 
  
    return maxDict 
n=int(input())
arr =list(int(i) for i in input().strip().split(' '))
print(maxDistance(arr, n))