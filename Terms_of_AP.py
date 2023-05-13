#Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.
x = int(input())
N = 1
count = 1
while(count <= x):
    sum = (3*N + 2)
    N += 1
    if( sum % 4 != 0):
        print(sum, end=" ")
        count += 1