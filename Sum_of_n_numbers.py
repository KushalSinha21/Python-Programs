#Given an integer n, find and print the sum of numbers from 1 to n.
n = int(input())
i = 0
sum = 0
while (i <= n):
    sum = sum + i
    i = i + 1
print( sum)