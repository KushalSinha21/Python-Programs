#You are given an integer ‘N’, your task is to find and return the N’th Fibonacci number using matrix exponentiation.
#Since the answer can be very large, return the answer modulo 10^9 +7.
def multiply(a, b): 
    mod = int(1e9 + 7) 
    c = [[0 for i in range(2)] for j in range(2)]
    for i in range(2): 
        for j in range(2):
            for k in range(2): 
                c[i][k] = (c[i][k] + a[i][j] * b[j][k]) % mod
    return c # Function to calclate n'th power of a matrix.
def matrix_power(coef, n):
    res = [[1, 0], [0, 1]] # While loop till n > 0. 
    while n > 0: 
        if (n % 2 != 0):
            res = multiply(res, coef) # Multiply coef with coef and update n to n//2. 
        coef = multiply(coef, coef) 
        n //= 2 
    return res 
def fibonacciNumber(n):
    coef = [[0, 1], [1, 1]] # Calculating the (n-1)th power of the coef matrix. 
    res = matrix_power(coef, n - 1) # Return the bottom right element of the resultant matrix. 
    return res[1][1]
