#Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
#Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.#
n=input()
le=len(n)
n=int(n)
sum_even=0
sum_odd=0
for i in range(1,le+1):
   if((n%10)%2==0):
           sum_even+=n%10
   else:
           sum_odd+=n%10
   n=n//(10)
print(sum_even,sum_odd)