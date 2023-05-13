#Write a python script which takes integer input from the user and checks if the number is divisible by 2 and 3 or not.
n = int(input())

if (n % 2 == 0):
    if (n % 3 == 0):
        print("Divisible by 2 and 3")
    else:
        print("Divisible by 2 but not divisible by 3")
else:
    if(n % 3 == 0):
        print("Divisible by 3 but not divisible by 2")
    else:
        print("Not Divisible by 2 and also not divisible by 3")