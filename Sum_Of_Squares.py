#You are given an integer 'N'. You need to find the sum of squares of the first 'N' natural numbers.
def sumOfSquares(n):
    sum = n * (n+1) * (2*n+1) // 6
    return sum
n = int(input())
print(sumOfSquares(n))