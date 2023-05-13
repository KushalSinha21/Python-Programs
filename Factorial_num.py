#You are given an integer ‘N’. You have to print the value of Factorial of ‘N’. The Factorial of a number ‘N’ is defined as the product of all numbers from 1 to ‘N’.
def fact(n):
    n_fact = 1
    for i in range (1,n+1):
        n_fact *= i
    return n_fact
n = int(input())
a = fact(n)
print(a)